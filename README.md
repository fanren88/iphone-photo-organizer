<div align="center">
  <a href="./README.md">
    <h1>📸 Mobile Photo Organizer</h1>
  </a>

  <p align="center">
    <strong>A powerful toolkit to backup and organize mobile photos (iPhone & Android) on macOS and Windows.</strong>
  </p>

  <p align="center">
    <a href="README.md">English</a> •
    <a href="README_zh.md">简体中文</a>
  </p>

  <p align="center">
    <img src="https://img.shields.io/badge/Python-3.9%2B-blue" alt="Python Version">
    <img src="https://img.shields.io/badge/License-MIT-green" alt="License">
    <img src="https://img.shields.io/badge/Platform-macOS-lightgrey" alt="Platform">
  </p>
</div>

---

## 📖 Introduction

**iPhone Photo Organizer** helps you backup iPhone photos and videos to your Mac / Windows PC (and external drives) while preserving:
- **Live Photos**: Keeps `.HEIC` images and `.MOV` videos paired together.
- **Metadata**: Preserves original creation dates and times.
- **Location**: Automatically organizes folders by location (e.g., `2023/10/2023-10-01_Shanghai`).

## ✨ Features

- **Live Photo Support**: Automatically detects and groups `IMG_X.HEIC` and `IMG_X.MOV`.
- **Smart Geocoding**: Converts GPS coordinates to readable city names (requires internet).
- **Date Sorting**: Organizes files into `Year -> Month -> Date_Location` structure.
- **Duplicate Handling**: Smartly handles duplicates during import.
- **User-Friendly Interface**: Built with Streamlit for an easy-to-use web UI.

## 🚀 Quick Start

### Prerequisites
- macOS or Windows
- Python 3 installed

### Installation & Usage

#### macOS / Linux

1.  **Clone or Download** this repository.
2.  **Run the Starter Script**:
    Open Terminal in the project folder and run:
    ```bash
    chmod +x start.sh
    ./start.sh
    ```
    *This script sets up the environment and launches the application.*

#### Windows

1.  **Clone or Download** this repository.
2.  **Run the Starter Script**:
    Double-click `start.bat` in the project folder.
    *This script sets up the environment and launches the application.*

3.  **Use the Web App**:
    - The app will open in your browser (usually `http://localhost:8501`).
    - **Source Folder**: Select the folder where you downloaded photos (iPhone or Android).
    - Select your **Destination Folder** (where you want organized photos).
    - Click **Start Organizing**.

## 🛠 Manual Setup (Optional)

If you prefer not to use `start.sh`, you can run it manually:

```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

## 📄 License

This project is licensed under the MIT License.
