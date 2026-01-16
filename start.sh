#!/bin/bash

# Define the virtual environment directory
VENV_DIR="venv"

# Check if venv exists
if [ ! -d "$VENV_DIR" ]; then
    echo "Creating virtual environment in $VENV_DIR..."
    python3 -m venv "$VENV_DIR"
else
    echo "Virtual environment already exists."
fi

# Activate the virtual environment
source "$VENV_DIR/bin/activate"

# Upgrade pip to ensure latest version (optional but good practice)
pip install --upgrade pip

# Install requirements
if [ -f "requirements.txt" ]; then
    echo "Installing requirements..."
    pip install -r requirements.txt
else
    echo "requirements.txt not found!"
    exit 1
fi

# Run the Streamlit app
echo "Starting Photo Organizer Web App..."
# Suppress the "Email" prompt and usage stats
export STREAMLIT_CREDENTIALS_NO_EMAIL=true
export STREAMLIT_BROWSER_GATHER_USAGE_STATS=false

streamlit run app.py
