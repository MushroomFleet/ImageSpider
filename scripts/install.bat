@echo off
echo Setting up virtual environment and installing dependencies...
echo.

REM Store original directory
set "ORIGINAL_DIR=%CD%"

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python is not installed or not in PATH
    echo Please install Python and try again
    pause
    exit /b 1
)

REM Create and activate virtual environment
echo Creating virtual environment...
if exist "..\venv" (
    echo Found existing virtual environment, deleting...
    rmdir /s /q "..\venv"
)

python -m venv ..\venv
if errorlevel 1 (
    echo Error: Failed to create virtual environment
    cd "%ORIGINAL_DIR%"
    pause
    exit /b 1
)

REM Activate virtual environment
call ..\venv\Scripts\activate
if errorlevel 1 (
    echo Error: Failed to activate virtual environment
    cd "%ORIGINAL_DIR%"
    pause
    exit /b 1
)

REM Update pip in virtual environment
python -m pip install --upgrade pip
if errorlevel 1 (
    echo Warning: Failed to upgrade pip, continuing with installation...
)

REM Navigate to src directory
cd ..\src

REM Install core dependencies first
echo Installing core dependencies...
python -m pip install numpy==1.24.2
python -m pip install torch==2.0.0
if errorlevel 1 (
    echo Error installing core dependencies
    cd "%ORIGINAL_DIR%"
    pause
    exit /b 1
)

REM Install other dependencies
echo Installing additional dependencies...
pip install -r requirements.txt
if errorlevel 1 (
    echo Error installing dependencies
    cd "%ORIGINAL_DIR%"
    pause
    exit /b 1
)

echo.
echo Installation completed successfully!
cd "%ORIGINAL_DIR%"
pause