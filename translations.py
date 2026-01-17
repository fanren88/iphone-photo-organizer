
translations = {
    "zh": {
        "page_title": "手机照片整理工具 (iPhone/Android)",
        "system_menu": "⚙️ 系统菜单",
        "exit_app": "❌ 关闭程序 (Exit App)",
        "app_closed": "程序已关闭，请关闭浏览器窗口。",
        "tips_title": "**💡 提示：**",
        "tips_content": """
    - 如需 **中途停止整理**，请直接点击浏览器地址栏旁边的 **“X” (停止)** 按钮，或直接 **刷新页面**。
    - 整理完成后，点击上方“关闭程序”可完全退出后台服务。
    """,
        "main_header": "📸 手机照片整理工具",
        "sub_header": "自动备份整理您的手机照片 (iPhone & Android)，支持地理位置分类和实况照片。",
        "guide_expander": "ℹ️ 使用指南（必读：如何导出照片？）",
        "guide_content": """
    **📱 iPhone 用户：**
    1.  **连接手机**：用数据线连接 iPhone 到电脑。
    2.  **导出照片**：
        *   **macOS**: 打开“图像捕捉” (Image Capture)，选择手机，下载照片到本地文件夹。
        *   **Windows**: 打开“照片”应用或直接在资源管理器中访问 iPhone 设备，复制照片到本地文件夹。
    
    **🤖 Android 用户：**
    1.  **连接手机**：用数据线连接手机，在手机上选择“文件传输 / MTP”模式。
    2.  **导出照片**：打开文件资源管理器，进入手机存储的 `DCIM/Camera` 文件夹，将照片复制到电脑上的文件夹。
    
    **🚀 开始整理：**
    在下方选择刚才导出的文件夹作为 **“源文件夹”**，点击开始整理即可。
    """,
        "cant_open_picker": "无法打开文件夹选择器：{}",
        "tab_organize": "🚀 整理照片",
        "tab_restore": "↩️ 还原撤销",
        "select_source_title": "### 1. 选择源文件夹",
        "select_source_info": "请选择包含原始照片的文件夹 (支持 iPhone HEIC/MOV 及 Android JPG/MP4)。",
        "source_path_label": "源文件夹路径",
        "browse_source_btn": "浏览源文件夹",
        "select_dest_title": "### 2. 选择目标文件夹",
        "select_dest_info": "请选择整理后的照片存放位置（如移动硬盘）。",
        "inplace_org_label": "📂 原地整理 (直接在源文件夹内创建分类文件夹)",
        "inplace_org_help": "如果选中，整理后的文件夹将直接创建在源文件夹内。适合清理桌面杂乱文件夹。",
        "inplace_info": "将在 `{}` 内部直接整理。",
        "dest_path_label": "目标文件夹路径",
        "browse_dest_btn": "浏览目标文件夹",
        "advanced_options": "🛠️ 高级选项 (点击展开)",
        "custom_rules": "自定义您的整理规则：",
        "folder_structure_title": "**📂 文件夹结构**",
        "naming_mode_label": "选择文件夹命名方式",
        "naming_mode_help": "决定照片文件夹的层级和命名规则",
        "structure_options": {
            "date_location": "按日期 + 地点 (YYYY/MM/DD_地点)",
            "month_location": "按月份 + 地点 (YYYY/MM_地点)",
            "date_only": "仅按日期",
            "location_first": "按地点归档",
            "flat": "扁平化"
        },
        "structure_examples": {
            "date_location": "📄 **示例**：`2023/10/2023-10-01_上海市_黄浦区/IMG_001.JPG`\n\n📝 **说明**：最详细的分类，精确到每一天和具体地点。",
            "month_location": "📄 **示例**：`2023/10月/上海市_黄浦区/IMG_001.JPG`\n\n📝 **说明**：按月归档，并将同一个月内同一地点的照片聚合在一起。适合旅行整理。",
            "date_only": "📄 **示例**：`2023/10/2023-10-01/IMG_001.JPG`\n\n📝 **说明**：只按日期分类，不包含地理位置信息。",
            "location_first": "📄 **示例**：`上海市_黄浦区/2023-10/IMG_001.JPG`\n\n📝 **说明**：优先按地点分类，适合以“足迹”为维度的整理。",
            "flat": "📄 **示例**：`2023-10-01_上海市_黄浦区/IMG_001.JPG`\n\n📝 **说明**：所有文件夹都在第一层，没有年份/月份的嵌套。"
        },
        "file_processing_title": "**⚙️ 文件处理**",
        "rename_files_label": "重命名文件",
        "rename_files_help": "如果选中，文件将被重命名为 'YYYYMMDD_HHMMSS_原名' 格式，避免文件名冲突并按时间排序。",
        "action_mode_label": "处理动作",
        "action_mode_options": ["复制文件 (保留源文件)", "移动文件 (删除源文件)"],
        "action_mode_help": "复制更加安全；移动可以节省磁盘空间。",
        "delete_aae_label": "🗑️ 删除 .AAE 临时文件",
        "delete_aae_help": ".AAE 文件是苹果相册生成的编辑记录文件（如滤镜、裁剪信息）。如果您只需要保留原始照片，可以勾选此项以删除它们，保持文件夹整洁。",
        "delete_aae_warning": "注意：删除 .AAE 文件意味着在非苹果设备上查看照片时，您之前在手机上做的编辑（如滤镜）可能会丢失，只显示原图。",
        "start_organize_title": "### 3. 开始整理",
        "start_organize_btn": "🚀 开始整理照片",
        "error_no_source": "请选择有效的源文件夹。",
        "error_no_dest": "请选择有效的目标文件夹。",
        "spinner_analyzing": "正在分析并整理照片，请耐心等待...",
        "progress_processing": "正在处理: {} / {}",
        "success_complete": "✅ 整理完成！",
        "result_summary": """
                **照片整理成功！**
                
                您的照片已保存到：`{}`
                
                **本次整理配置：**
                - 结构模式：{}
                - 动作：{}
                - 重命名：{}
                """,
        "error_generic": "发生错误：{}",
        "restore_title": "### ↩️ 还原撤销",
        "restore_warning": "⚠️ 此功能会将指定文件夹内的所有照片（包括子文件夹）全部移动到根目录，并删除空文件夹。",
        "restore_info": "如果你对刚才的整理结果不满意，或者想换一种方式整理，请使用此功能将照片“打散”回原状。",
        "restore_path_label": "需要还原的文件夹路径",
        "browse_btn": "浏览文件夹",
        "start_restore_btn": "开始还原 (打散文件)",
        "error_invalid_path": "请输入有效的文件夹路径。",
        "spinner_restoring": "正在还原文件...",
        "progress_restoring": "正在还原: {} / {}",
        "success_restore": "✅ 还原完成！所有照片已回到根目录。",
        "error_restore": "还原失败：{}",
        "footer_caption": "基于 Python, Pillow 和 Streamlit 构建。完全本地处理 - 您的照片非常安全。",
        "language_select": "🌐 语言 / Language",
        
        # Backend / Logs
        "log_geocoded": "已定位 {} -> {}",
        "log_no_gps": "处理 {} (无 GPS)",
        "log_action": " | 动作: {}{}",
        "log_error_process": "错误: 处理失败 {}: {}",
        "log_found_files": "发现 {} 个文件 ({} 个任务)。开始并发整理...",
        "log_org_complete": "整理完成！详情请查看 'photo_organizer.log'。",
        "log_restored": "已还原: {}",
        "log_restore_fail": "还原失败 {}: {}",
        "log_found_restore": "发现 {} 个文件待还原...",
        "log_restore_complete": "还原完成！",
        "unknown_location": "未知地点"
    },
    "en": {
        "page_title": "Mobile Photo Organizer (iPhone/Android)",
        "system_menu": "⚙️ System Menu",
        "exit_app": "❌ Exit App",
        "app_closed": "App closed. Please close the browser tab.",
        "tips_title": "**💡 Tips:**",
        "tips_content": """
    - To **stop organizing**, click the **"X" (Stop)** button next to the browser address bar, or **refresh the page**.
    - After organizing, click "Exit App" above to completely stop the background service.
    """,
        "main_header": "📸 Mobile Photo Organizer",
        "sub_header": "Automatically backup and organize your mobile photos (iPhone & Android), supporting location categorization and Live Photos.",
        "guide_expander": "ℹ️ User Guide (Must Read: How to Export Photos?)",
        "guide_content": """
    **📱 iPhone Users:**
    1.  **Connect**: Connect iPhone via USB.
    2.  **Export**:
        *   **macOS**: Use "Image Capture" app to download photos.
        *   **Windows**: Use "Photos" app or File Explorer to copy photos.
        
    **🤖 Android Users:**
    1.  **Connect**: Connect phone via USB, select "File Transfer / MTP" mode on phone.
    2.  **Export**: Open File Explorer, go to `DCIM/Camera`, and copy photos to a local folder.
    
    **🚀 Start:**
    Select that folder below as **"Source Folder"**.
    """,
        "cant_open_picker": "Cannot open folder picker: {}",
        "tab_organize": "🚀 Organize",
        "tab_restore": "↩️ Restore/Undo",
        "select_source_title": "### 1. Select Source Folder",
        "select_source_info": "Please select the folder containing original photos (Supports iPhone HEIC/MOV & Android JPG/MP4).",
        "source_path_label": "Source Folder Path",
        "browse_source_btn": "Browse Source Folder",
        "select_dest_title": "### 2. Select Destination Folder",
        "select_dest_info": "Please select where to store organized photos (e.g., external hard drive).",
        "inplace_org_label": "📂 In-place Organize (Create folders inside source folder)",
        "inplace_org_help": "If checked, organized folders will be created directly inside the source folder. Good for cleaning up messy desktop folders.",
        "inplace_info": "Will organize directly inside `{}`.",
        "dest_path_label": "Destination Folder Path",
        "browse_dest_btn": "Browse Destination Folder",
        "advanced_options": "🛠️ Advanced Options (Click to expand)",
        "custom_rules": "Customize your organization rules:",
        "folder_structure_title": "**📂 Folder Structure**",
        "naming_mode_label": "Select Folder Naming Mode",
        "naming_mode_help": "Determines the hierarchy and naming rules for photo folders.",
        "structure_options": {
            "date_location": "Date + Location (YYYY/MM/DD_Location)",
            "month_location": "Month + Location (YYYY/MM_Location)",
            "date_only": "Date Only",
            "location_first": "Location First",
            "flat": "Flat (No hierarchy)"
        },
        "structure_examples": {
            "date_location": "📄 **Example**: `2023/10/2023-10-01_Shanghai_Huangpu/IMG_001.JPG`\n\n📝 **Note**: Most detailed categorization, precise to day and location.",
            "month_location": "📄 **Example**: `2023/10/Shanghai_Huangpu/IMG_001.JPG`\n\n📝 **Note**: Archived by month, aggregating photos from the same location within the same month. Good for travel.",
            "date_only": "📄 **Example**: `2023/10/2023-10-01/IMG_001.JPG`\n\n📝 **Note**: Classified by date only, no location info.",
            "location_first": "📄 **Example**: `Shanghai_Huangpu/2023-10/IMG_001.JPG`\n\n📝 **Note**: Prioritizes location, suitable for \"Footprints\" dimension.",
            "flat": "📄 **Example**: `2023-10-01_Shanghai_Huangpu/IMG_001.JPG`\n\n📝 **Note**: All folders in the first level, no Year/Month nesting."
        },
        "file_processing_title": "**⚙️ File Processing**",
        "rename_files_label": "Rename Files",
        "rename_files_help": "If checked, files will be renamed to 'YYYYMMDD_HHMMSS_OriginalName' format to avoid conflicts and sort by time.",
        "action_mode_label": "Action Mode",
        "action_mode_options": ["Copy Files (Keep Source)", "Move Files (Delete Source)"],
        "action_mode_help": "Copy is safer; Move saves disk space.",
        "delete_aae_label": "🗑️ Delete .AAE Temp Files",
        "delete_aae_help": ".AAE files are edit records (filters, crops) generated by Apple Photos. Check this to delete them if you only want original photos.",
        "delete_aae_warning": "Note: Deleting .AAE files means edits made on phone (like filters) might be lost when viewing on non-Apple devices, showing only the original image.",
        "start_organize_title": "### 3. Start Organizing",
        "start_organize_btn": "🚀 Start Organizing Photos",
        "error_no_source": "Please select a valid source folder.",
        "error_no_dest": "Please select a valid destination folder.",
        "spinner_analyzing": "Analyzing and organizing photos, please wait...",
        "progress_processing": "Processing: {} / {}",
        "success_complete": "✅ Organization Complete!",
        "result_summary": """
                **Photo Organization Successful!**
                
                Your photos have been saved to: `{}`
                
                **Configuration:**
                - Structure Mode: {}
                - Action: {}
                - Rename: {}
                """,
        "error_generic": "Error occurred: {}",
        "restore_title": "### ↩️ Restore/Undo",
        "restore_warning": "⚠️ This feature will move ALL photos in the specified folder (including subfolders) to the root directory and delete empty folders.",
        "restore_info": "If you are unsatisfied with the result or want to reorganize, use this to \"flatten\" files back to original state.",
        "restore_path_label": "Folder to Restore",
        "browse_btn": "Browse Folder",
        "start_restore_btn": "Start Restore (Flatten Files)",
        "error_invalid_path": "Please enter a valid folder path.",
        "spinner_restoring": "Restoring files...",
        "progress_restoring": "Restoring: {} / {}",
        "success_restore": "✅ Restore Complete! All photos moved to root.",
        "error_restore": "Restore failed: {}",
        "footer_caption": "Built with Python, Pillow, and Streamlit. Fully local processing - your photos are safe.",
        "language_select": "🌐 语言 / Language",
        
        # Backend / Logs
        "log_geocoded": "Geocoded {} -> {}",
        "log_no_gps": "Processing {} (No GPS)",
        "log_action": " | Action: {}{}",
        "log_error_process": "Error: Failed to process {}: {}",
        "log_found_files": "Found {} files ({} tasks). Starting concurrent organization...",
        "log_org_complete": "Organization complete! Check 'photo_organizer.log' for details.",
        "log_restored": "Restored: {}",
        "log_restore_fail": "Failed to restore {}: {}",
        "log_found_restore": "Found {} files to restore...",
        "log_restore_complete": "Restoration complete!",
        "unknown_location": "Unknown_Location"
    }
}
