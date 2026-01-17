import streamlit as st
import os
import subprocess
import platform
from organize_photos import organize_files, restore_files
from translations import translations

# --- Page Config ---
st.set_page_config(
    page_title="Mobile Photo Organizer",
    page_icon="📸",
    layout="wide"
)

# --- Language Setup ---
if 'language' not in st.session_state:
    st.session_state.language = 'zh'

def set_language():
    st.session_state.language = st.session_state.lang_select

t = translations[st.session_state.language]

# --- Styling ---
st.markdown("""
<style>
    /* Global Styles */
    .main {
        /* Let Streamlit handle background color to match theme */
        padding-top: 2rem;
    }
    
    /* Modern Card Style for Sections */
    .css-1r6slb0, .stExpander, .stTabs {
        /* Use theme-aware variables */
        background-color: var(--secondary-background-color);
        border-radius: 12px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        padding: 20px;
        margin-bottom: 20px;
        border: 1px solid rgba(128, 128, 128, 0.2);
    }

    /* Typography */
    h1, h2, h3 {
        font-family: 'SF Pro Display', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
        color: var(--text-color);
    }
    
    .main-header {
        font-size: 3rem;
        font-weight: 700;
        color: #1a73e8; /* Keep brand color or use var(--primary-color) */
        text-align: center;
        margin-bottom: 0.5rem;
        text-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }
    
    .sub-header {
        font-size: 1.1rem;
        color: var(--text-color);
        opacity: 0.8;
        text-align: center;
        margin-bottom: 3rem;
        font-weight: 400;
    }

    /* Inputs and Buttons */
    .stTextInput>div>div>input {
        border-radius: 8px;
        border: 1px solid rgba(128, 128, 128, 0.3);
        padding: 10px 12px;
        transition: border-color 0.3s ease;
        background-color: var(--background-color);
        color: var(--text-color);
    }
    .stTextInput>div>div>input:focus {
        border-color: #1a73e8;
        box-shadow: 0 0 0 2px rgba(26, 115, 232, 0.2);
    }

    .stButton>button {
        width: 100%;
        border-radius: 10px;
        height: 3.2em;
        background: linear-gradient(135deg, #1a73e8 0%, #0d47a1 100%);
        color: white;
        font-weight: 600;
        border: none;
        box-shadow: 0 4px 6px rgba(26, 115, 232, 0.3);
        transition: all 0.3s ease;
    }
    
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 12px rgba(26, 115, 232, 0.4);
    }
    
    .stButton>button:active {
        transform: translateY(0);
    }

    /* Info Boxes */
    .stAlert {
        border-radius: 10px;
        border: none;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    
    /* Footer */
    footer {visibility: hidden;}
    
</style>
""", unsafe_allow_html=True)

# --- Sidebar ---
with st.sidebar:
    st.selectbox(
        "🌐 语言 / Language",
        options=['zh', 'en'],
        format_func=lambda x: "中文" if x == 'zh' else "English",
        key='lang_select',
        on_change=set_language,
        index=0 if st.session_state.language == 'zh' else 1
    )
    
    st.markdown(f"### {t['system_menu']}")
    if st.button(t['exit_app']):
        st.warning(t['app_closed'])
        st.stop()
        os._exit(0)
    
    st.markdown("---")
    st.markdown(f"""
    {t['tips_title']}
    {t['tips_content']}
    """)

# --- Header ---
st.markdown(f'<div class="main-header">{t["main_header"]}</div>', unsafe_allow_html=True)
st.markdown(f'<div class="sub-header">{t["sub_header"]}</div>', unsafe_allow_html=True)

with st.expander(t['guide_expander'], expanded=True):
    st.markdown(t['guide_content'])

# --- Helper Functions ---
def pick_folder_gui():
    """Opens a native macOS folder picker dialog using AppleScript."""
    try:
        script = 'tell app "System Events" to activate\nset theFolder to choose folder\nPOSIX path of theFolder'
        result = subprocess.run(['osascript', '-e', script], capture_output=True, text=True)
        if result.returncode == 0:
            return result.stdout.strip()
    except Exception as e:
        st.error(t['cant_open_picker'].format(e))
    return None

# --- Tabs ---
tab_organize, tab_restore = st.tabs([t['tab_organize'], t['tab_restore']])

with tab_organize:
    # --- Main Interface ---
    col1, col2 = st.columns(2)

    with col1:
        st.markdown(t['select_source_title'])
        st.info(t['select_source_info'])
        
        # Use session state to persist paths across reruns
        if 'source_path' not in st.session_state:
            st.session_state.source_path = ""
        if 'src_input' not in st.session_state:
            st.session_state.src_input = ""
        
        # Callback to handle manual path updates
        def update_src_path():
            st.session_state.source_path = st.session_state.src_input

        # Callback to handle browse button
        def on_browse_source():
            path = pick_folder_gui()
            if path:
                st.session_state.source_path = path
                st.session_state.src_input = path

        # Don't use 'value' if key is present to avoid Streamlit warnings/issues
        # We initialize the key above
        st.text_input(t['source_path_label'], key="src_input", on_change=update_src_path)
        st.write("") 
        st.button(t['browse_source_btn'], on_click=on_browse_source)

    with col2:
        st.markdown(t['select_dest_title'])
        st.info(t['select_dest_info'])
        
        if 'dest_path' not in st.session_state:
            st.session_state.dest_path = ""
        if 'dest_input' not in st.session_state:
            st.session_state.dest_input = ""
        
        def update_dest_path():
            st.session_state.dest_path = st.session_state.dest_input

        def on_browse_dest():
            path = pick_folder_gui()
            if path:
                st.session_state.dest_path = path
                st.session_state.dest_input = path

        # Checkbox for In-Place Organization
        inplace_org = st.checkbox(
            t['inplace_org_label'],
            value=False,
            help=t['inplace_org_help']
        )

        if inplace_org:
            # Sync source to dest if inplace
            # Use src_input as the source of truth for the path string
            current_src = st.session_state.get("src_input", "")
            st.info(t['inplace_info'].format(current_src or t['source_path_label']))
            
            # Don't modify widget key 'dest_input' directly if it's already instantiated
            # Just ensure we use current_src for logic later
            dest_disabled = True
        else:
            dest_disabled = False

        # If disabled/inplace, we force the value to be source
        if inplace_org:
             st.text_input(
                t['dest_path_label'], 
                value=st.session_state.get("src_input", ""),
                key="dest_input_display", # Use a different key for display only
                disabled=True
            )
             # Ensure internal state matches for logic
             st.session_state.dest_input = st.session_state.get("src_input", "")
        else:
            st.text_input(
                t['dest_path_label'], 
                key="dest_input",
                disabled=False,
                on_change=update_dest_path
            )

        st.write("")
        st.button(t['browse_dest_btn'], disabled=dest_disabled, on_click=on_browse_dest)

    st.divider()

    # --- Advanced Options ---
    with st.expander(t['advanced_options'], expanded=False):
        st.markdown(t['custom_rules'])
        
        col_opt1, col_opt2 = st.columns(2)
        
        with col_opt1:
            st.markdown(t['folder_structure_title'])
            
            # Use keys as options, display values using format_func
            structure_keys = list(t['structure_options'].keys())
            
            structure_mode = st.radio(
                t['naming_mode_label'],
                options=structure_keys,
                format_func=lambda x: t['structure_options'][x],
                index=0,
                key="structure_mode_key", # Changed key
                help=t['naming_mode_help']
            )
            
            selected_structure = structure_mode

            # Dynamic Example Display
            example_text = t['structure_examples'].get(selected_structure, "")
            st.info(example_text)

        with col_opt2:
            st.markdown(t['file_processing_title'])
            rename_files = st.checkbox(
                t['rename_files_label'], 
                value=False,
                help=t['rename_files_help']
            )
            
            action_options = ["copy", "move"]
            action_mode = st.radio(
                t['action_mode_label'],
                options=action_options,
                format_func=lambda x: t['action_mode_options'][0] if x == 'copy' else t['action_mode_options'][1],
                index=0,
                help=t['action_mode_help']
            )
            selected_action = action_mode

            st.write("")
            delete_aae = st.checkbox(
                t['delete_aae_label'],
                value=False,
                help=t['delete_aae_help']
            )
            if delete_aae:
                st.warning(t['delete_aae_warning'])

    st.divider()

    # --- Execution Area ---
    st.markdown(t['start_organize_title'])

    if st.button(t['start_organize_btn']):
        # Read directly from widgets source of truth
        src = st.session_state.src_input
        dst = st.session_state.dest_input
        
        if not src or not os.path.exists(src):
            st.error(t['error_no_source'])
        elif not dst or not os.path.exists(dst):
            st.error(t['error_no_dest'])
        else:
            # Progress UI
            progress_bar = st.progress(0)
            status_text = st.empty()
            log_area = st.empty()
            logs = []

            def update_progress(current, total):
                progress = min(current / total, 1.0)
                progress_bar.progress(progress)
                status_text.text(t['progress_processing'].format(current, total))

            def update_log(message):
                logs.append(message)
                # Keep only last 5 logs to avoid clutter
                display_logs = logs[-5:]
                log_area.code("\n".join(display_logs))

            try:
                with st.spinner(t['spinner_analyzing']):
                    organize_files(
                        src, 
                        dst, 
                        progress_callback=update_progress, 
                        log_callback=update_log,
                        structure_type=selected_structure,
                        rename_enabled=rename_files,
                        action_type=selected_action,
                        delete_aae=delete_aae,
                        language=st.session_state.language
                    )
                
                st.success(t['success_complete'])
                st.balloons()
                
                # Show result summary
                action_label = t['action_mode_options'][0] if selected_action == 'copy' else t['action_mode_options'][1]
                structure_label = t['structure_options'][selected_structure]
                
                st.markdown(t['result_summary'].format(
                    dst,
                    structure_label,
                    action_label,
                    'Yes' if rename_files else 'No' # Simple boolean display or localize? leaving simple for now or localize if picky
                ))
                
            except Exception as e:
                st.error(t['error_generic'].format(str(e)))
                st.exception(e)

with tab_restore:
    st.markdown(t['restore_title'])
    st.warning(t['restore_warning'])
    st.info(t['restore_info'])

    if 'restore_input' not in st.session_state:
        # Default to dest_input if available, else empty
        st.session_state.restore_input = st.session_state.get("dest_input", "")

    def update_restore_path():
        pass # Just to trigger rerun if needed

    def on_browse_restore():
        path = pick_folder_gui()
        if path:
            st.session_state.restore_input = path

    c_res1, c_res2 = st.columns([3, 1])
    with c_res1:
        restore_folder = st.text_input(
            t['restore_path_label'], 
            key="restore_input",
            on_change=update_restore_path
        )
    with c_res2:
        st.write("") # spacer
        st.write("")
        st.button(t['browse_btn'], key="btn_browse_restore", on_click=on_browse_restore)
    
    st.write("")
    if st.button(t['start_restore_btn']):
        if not restore_folder or not os.path.exists(restore_folder):
            st.error(t['error_invalid_path'])
        else:
            # Progress UI
            progress_bar_res = st.progress(0)
            status_text_res = st.empty()
            log_area_res = st.empty()
            logs_res = []

            def update_progress_res(current, total):
                progress = min(current / total, 1.0)
                progress_bar_res.progress(progress)
                status_text_res.text(t['progress_restoring'].format(current, total))

            def update_log_res(message):
                logs_res.append(message)
                display_logs = logs_res[-5:]
                log_area_res.code("\n".join(display_logs))

            try:
                with st.spinner(t['spinner_restoring']):
                    restore_files(
                        restore_folder, 
                        restore_folder, # Restore to same dir (flatten in place)
                        progress_callback=update_progress_res,
                        log_callback=update_log_res,
                        language=st.session_state.language
                    )
                st.success(t['success_restore'])
            except Exception as e:
                st.error(t['error_restore'].format(str(e)))
st.markdown("---")
st.caption(t['footer_caption'])
