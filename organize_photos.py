import os
import shutil
import time
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime
from PIL import Image, ExifTags
from pillow_heif import register_heif_opener
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut, GeocoderServiceError
import hachoir.parser
import hachoir.metadata
import logging
from translations import translations

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("photo_organizer.log"),
        logging.StreamHandler()
    ]
)

# Register HEIC opener
register_heif_opener()

# Initialize Geocoder
geolocator = Nominatim(user_agent="photo_organizer_script")

# Cache for location to avoid API rate limits
location_cache = {}
# Lock for geocoding to strictly enforce rate limits across threads
geocoding_lock = threading.Lock()

def get_decimal_coordinates(info):
    """Converts GPS coordinates to decimal degrees."""
    try:
        lat = None
        lon = None
        
        if 'GPSLatitude' in info and 'GPSLatitudeRef' in info:
            d, m, s = info['GPSLatitude']
            d = float(d)
            m = float(m)
            s = float(s)
            lat = d + (m / 60.0) + (s / 3600.0)
            if info['GPSLatitudeRef'] == 'S':
                lat = -lat

        if 'GPSLongitude' in info and 'GPSLongitudeRef' in info:
            d, m, s = info['GPSLongitude']
            d = float(d)
            m = float(m)
            s = float(s)
            lon = d + (m / 60.0) + (s / 3600.0)
            if info['GPSLongitudeRef'] == 'W':
                lon = -lon
                
        return lat, lon
    except Exception as e:
        logging.error(f"Error converting GPS coordinates: {e}")
        return None, None

def get_location_name(lat, lon, language='zh'):
    """Reverse geocodes coordinates to a city/location name. Thread-safe."""
    t = translations[language]
    if not lat or not lon:
        return t['unknown_location']
    
    key = f"{lat:.2f},{lon:.2f},{language}" # Include language in cache key
    
    # Check cache first
    with geocoding_lock:
        if key in location_cache:
            return location_cache[key]

        try:
            # Sleep to respect rate limits (1 per second for Nominatim)
            time.sleep(1.1)
            loc_lang = 'zh-cn' if language == 'zh' else 'en'
            location = geolocator.reverse((lat, lon), language=loc_lang, exactly_one=True)
            if location:
                address = location.raw.get('address', {})
                # Construct a more detailed address string: Province_City_District
                parts = []
                
                # State/Province
                province = address.get('state')
                if province: parts.append(province)
                
                # City
                city = address.get('city') or address.get('town') or address.get('county')
                if city and city not in parts: # Avoid duplicate if city == province
                    parts.append(city)
                    
                # District (optional, add if you want more granularity)
                district = address.get('district') or address.get('suburb')
                if district: parts.append(district)
                
                if not parts:
                    loc_name = t['unknown_location']
                else:
                    loc_name = "_".join(parts)

                # Clean up name for file system
                loc_name = "".join([c for c in loc_name if c.isalnum() or c in (' ', '_', '-')]).strip()
                location_cache[key] = loc_name
                return loc_name
        except (GeocoderTimedOut, GeocoderServiceError) as e:
            logging.warning(f"Geocoding error: {e}")
        except Exception as e:
            logging.error(f"Unexpected geocoding error: {e}")

        return t['unknown_location']

def get_image_metadata(file_path):
    """Extracts date and location from image files."""
    try:
        image = Image.open(file_path)
        exif = image.getexif()
        
        date_taken = None
        lat, lon = None, None

        if exif:
            # Get Date
            date_str = exif.get(36867) or exif.get(306) # DateTimeOriginal or DateTime
            if date_str:
                try:
                    date_taken = datetime.strptime(date_str, "%Y:%m:%d %H:%M:%S")
                except ValueError:
                    pass

            # Get GPS
            gps_info = exif.get_ifd(ExifTags.IFD.GPSInfo)
            if gps_info:
                # Convert keys to readable names for helper function
                gps_data = {}
                for k, v in gps_info.items():
                    tag = ExifTags.GPSTAGS.get(k, k)
                    gps_data[tag] = v
                lat, lon = get_decimal_coordinates(gps_data)
        
        return date_taken, lat, lon
    except Exception as e:
        logging.error(f"Error reading image metadata for {file_path}: {e}")
        return None, None, None

def get_video_date(file_path):
    """Extracts creation date from video files using hachoir."""
    try:
        parser = hachoir.parser.createParser(file_path)
        if not parser:
            return None
        with parser:
            metadata = hachoir.metadata.extractMetadata(parser)
            if metadata and metadata.has("creation_date"):
                return metadata.get("creation_date")
    except Exception as e:
        logging.warning(f"Could not read video metadata for {file_path}: {e}")
    return None

def process_single_item(item, source_dir, dest_dir, structure_type, rename_enabled, action_type, delete_aae=False, language='zh'):
    """
    Worker function to process a single item (file or pair).
    item: dict containing 'main_file', 'is_live_photo', 'pair_file'
    """
    t = translations[language]
    filename = item['main_file']
    src_path = os.path.join(source_dir, filename)
    
    if not os.path.isfile(src_path):
        return None

    base_name, ext = os.path.splitext(filename)
    ext = ext.lower()
    
    date_taken = None
    lat, lon = None, None
    
    # Metadata Extraction
    if ext in ['.heic', '.jpg', '.jpeg', '.png']:
        date_taken, lat, lon = get_image_metadata(src_path)
    elif ext == '.mov':
        date_taken = get_video_date(src_path)
    
    # Fallback date
    if not date_taken:
        timestamp = os.path.getmtime(src_path)
        date_taken = datetime.fromtimestamp(timestamp)
    
    # Geocoding (Thread-safe inside function)
    location_name = "Unknown"
    log_msg_loc = ""
    if lat and lon:
        location_name = get_location_name(lat, lon, language)
        log_msg_loc = t['log_geocoded'].format(filename, location_name)
    else:
        log_msg_loc = t['log_no_gps'].format(filename)
        
    # Determine Destination Structure
    year = date_taken.strftime("%Y")
    month = date_taken.strftime("%m")
    day_date = date_taken.strftime("%Y-%m-%d")
    
    final_dest_dir = dest_dir
    if structure_type == "date_location":
        final_dest_dir = os.path.join(dest_dir, year, month, f"{day_date}_{location_name}")
    elif structure_type == "month_location":
         # NEW LOGIC: Dest / YYYY / MM月 / Location_Name
         # e.g., 2025/10月/横沙乡_崇明区
         month_suffix = "月" if language == 'zh' else ""
         final_dest_dir = os.path.join(dest_dir, year, f"{month}{month_suffix}", location_name)
    elif structure_type == "date_only":
        final_dest_dir = os.path.join(dest_dir, year, month, day_date)
    elif structure_type == "location_first":
        final_dest_dir = os.path.join(dest_dir, location_name, f"{year}-{month}")
    elif structure_type == "flat":
        final_dest_dir = os.path.join(dest_dir, f"{day_date}_{location_name}")
    
    # Ensure dir exists (race condition possible here but makedirs(exist_ok=True) handles it)
    os.makedirs(final_dest_dir, exist_ok=True)

    # Determine Target Filenames
    target_name = filename
    pair_target_name = item.get('pair_file')
    aae_target_name = item.get('aae_file')
    
    if rename_enabled:
        time_str = date_taken.strftime("%Y%m%d_%H%M%S")
        name_base, name_ext = os.path.splitext(filename)
        target_name = f"{time_str}_{name_base}{name_ext}"
        
        if item.get('pair_file'):
            pair_base, pair_ext = os.path.splitext(item['pair_file'])
            pair_target_name = f"{time_str}_{pair_base}{pair_ext}"
            
        if item.get('aae_file'):
            aae_base, aae_ext = os.path.splitext(item['aae_file'])
            aae_target_name = f"{time_str}_{aae_base}{aae_ext}"

    target_path = os.path.join(final_dest_dir, target_name)
    
    # Move or Copy
    try:
        if action_type == "move":
            shutil.move(src_path, target_path)
        else:
            shutil.copy2(src_path, target_path)
        
        pair_msg = ""
        if item['is_live_photo'] and item.get('pair_file'):
            pair_src_path = os.path.join(source_dir, item['pair_file'])
            pair_dest_path = os.path.join(final_dest_dir, pair_target_name)
            
            if action_type == "move":
                shutil.move(pair_src_path, pair_dest_path)
            else:
                shutil.copy2(pair_src_path, pair_dest_path)
            pair_msg = f" + Pair: {item['pair_file']}"
            
        if item.get('aae_file'):
            aae_src_path = os.path.join(source_dir, item['aae_file'])
            
            if delete_aae:
                # DELETE AAE
                try:
                    os.remove(aae_src_path)
                    pair_msg += f" + AAE Deleted"
                except Exception as e:
                    pair_msg += f" + AAE Delete Failed: {e}"
            else:
                # MOVE/COPY AAE
                aae_dest_path = os.path.join(final_dest_dir, aae_target_name)
                if action_type == "move":
                    shutil.move(aae_src_path, aae_dest_path)
                else:
                    shutil.copy2(aae_src_path, aae_dest_path)
                pair_msg += f" + AAE: {item['aae_file']}"

        return f"{log_msg_loc}{t['log_action'].format(filename, pair_msg)}"
            
    except Exception as e:
        return t['log_error_process'].format(filename, e)

def organize_files(source_dir, dest_dir, progress_callback=None, log_callback=None, 
                   structure_type="date_location", rename_enabled=False, action_type="copy", delete_aae=False, language='zh'):
    """
    Main function to organize files concurrently.
    """
    t = translations[language]
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    files = [f for f in os.listdir(source_dir) if not f.startswith('.')]
    total_files_count = len(files) # Approximation for progress bar
    
    # 1. Pre-group files to handle Live Photo pairs
    # Logic: Identify pairs and treat them as a single unit of work
    work_items = []
    processed_names = set()
    
    # Helper to find if a file is already handled
    files_set = set(files)

    for filename in files:
        if filename in processed_names:
            continue
            
        base_name, ext = os.path.splitext(filename)
        ext = ext.lower()
        
        item = {
            'main_file': filename,
            'is_live_photo': False,
            'pair_file': None,
            'aae_file': None
        }
        
        if ext in ['.heic', '.jpg', '.jpeg', '.png']:
            possible_video = base_name + ".MOV"
            if possible_video in files_set:
                item['is_live_photo'] = True
                item['pair_file'] = possible_video
                processed_names.add(possible_video)
            
            # Check for AAE Sidecar
            possible_aae = base_name + ".AAE"
            if possible_aae in files_set:
                item['aae_file'] = possible_aae
                processed_names.add(possible_aae)
                
        elif ext == '.mov':
            # Check if this MOV belongs to a HEIC/JPG that we will process (or have processed)
            possible_heic = base_name + ".HEIC"
            possible_jpg = base_name + ".JPG"
            if possible_heic in files_set or possible_jpg in files_set:
                # This MOV is a pair to an image, let the image handle it
                continue
            # Else: Standalone video, process it
        
        work_items.append(item)
        processed_names.add(filename)

    total_tasks = len(work_items)
    msg = t['log_found_files'].format(total_files_count, total_tasks)
    if log_callback:
        log_callback(msg)
    else:
        print(msg)

    # 2. Process concurrently
    completed_count = 0
    # Use max_workers=None (defaults to CPU count * 5 for I/O bound) or set specific limit
    # We use a reasonable number to avoid opening too many file descriptors
    max_workers = min(32, os.cpu_count() + 4)
    
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {executor.submit(process_single_item, item, source_dir, dest_dir, structure_type, rename_enabled, action_type, delete_aae, language): item for item in work_items}
        
        for future in as_completed(futures):
            completed_count += 1
            result = future.result()
            
            # Update Progress
            if progress_callback:
                # We track tasks, but user expects file count progress? 
                # Let's map tasks to approximate file count or just use task count
                progress_callback(completed_count, total_tasks)
            
            if log_callback and result:
                # Log valid results
                log_callback(result)
            elif result:
                print(result)

    final_msg = t['log_org_complete']
    if log_callback:
        log_callback(final_msg)
    else:
        print(final_msg)

def restore_single_file(file_path, target_flat_dir, language='zh'):
    """Worker for restore."""
    t = translations[language]
    filename = os.path.basename(file_path)
    dest_path = os.path.join(target_flat_dir, filename)
    
    # Handle duplicate filenames (Atomic check/move is hard, so we use a lock or simple check)
    # For concurrent restore, strict renaming needs care. 
    # Simple strategy: Try move, if exist, rename.
    # Note: os.path.exists race condition is possible but unlikely to collide exact same nanosecond 
    # unless filenames are identical from different folders.
    
    if os.path.exists(dest_path):
        base, ext = os.path.splitext(filename)
        counter = 1
        while os.path.exists(dest_path):
            dest_path = os.path.join(target_flat_dir, f"{base}_{counter}{ext}")
            counter += 1
            
    try:
        shutil.move(file_path, dest_path)
        return t['log_restored'].format(filename)
    except Exception as e:
        return t['log_restore_fail'].format(filename, e)

def restore_files(organized_dir, target_flat_dir, progress_callback=None, log_callback=None, language='zh'):
    """
    Restores organized photos concurrently.
    """
    t = translations[language]
    if not os.path.exists(target_flat_dir):
        os.makedirs(target_flat_dir)
        
    all_files = []
    for root, dirs, files in os.walk(organized_dir):
        for f in files:
            if not f.startswith('.'):
                all_files.append(os.path.join(root, f))
    
    total_files = len(all_files)
    msg = t['log_found_restore'].format(total_files)
    if log_callback:
        log_callback(msg)
    else:
        print(msg)
        
    completed_count = 0
    max_workers = min(32, os.cpu_count() + 4)

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {executor.submit(restore_single_file, f, target_flat_dir, language): f for f in all_files}
        
        for future in as_completed(futures):
            completed_count += 1
            result = future.result()
            
            if progress_callback:
                progress_callback(completed_count, total_files)
            
            if log_callback and result:
                # Log less frequently
                if completed_count % 5 == 0: log_callback(result)
            elif result:
                print(result)

    # Clean up empty directories (Sequential is fine, fast)
    for root, dirs, files in os.walk(organized_dir, topdown=False):
        for name in dirs:
            dir_path = os.path.join(root, name)
            try:
                # Check if directory is effectively empty (ignoring .DS_Store)
                contents = os.listdir(dir_path)
                # Filter out .DS_Store
                valid_contents = [f for f in contents if f != '.DS_Store']
                
                if not valid_contents:
                    # It's empty or only has .DS_Store.
                    # Delete .DS_Store if present
                    if '.DS_Store' in contents:
                        try:
                            os.remove(os.path.join(dir_path, '.DS_Store'))
                        except OSError:
                            pass 
                    
                    # Try to remove dir
                    os.rmdir(dir_path)
            except OSError:
                pass  

    final_msg = t['log_restore_complete']
    if log_callback:
        log_callback(final_msg)
    else:
        print(final_msg)

if __name__ == "__main__":
    import sys
    if len(sys.argv) == 3:
        source = sys.argv[1]
        dest = sys.argv[2]
        organize_files(source, dest)
