@echo off
setlocal

:: Define the virtual environment directory
set "VENV_DIR=venv"

:: Check if venv exists
if not exist "%VENV_DIR%" (
    echo Creating virtual environment in %VENV_DIR%...
    python -m venv "%VENV_DIR%"
) else (
    echo Virtual environment already exists.
)

:: Activate the virtual environment
call "%VENV_DIR%\Scripts\activate.bat"

:: Upgrade pip
python -m pip install --upgrade pip

:: Install requirements
if exist "requirements.txt" (
    echo Installing requirements...
    pip install -r requirements.txt
) else (
    echo requirements.txt not found!
    pause
    exit /b 1
)

:: Run the Streamlit app
echo Starting Photo Organizer Web App...
set STREAMLIT_CREDENTIALS_NO_EMAIL=true
set STREAMLIT_BROWSER_GATHER_USAGE_STATS=false

streamlit run app.py
pause
