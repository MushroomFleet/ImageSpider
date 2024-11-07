@echo off
echo Updating ImageSpider dependencies...
echo.

REM Store original directory
set "ORIGINAL_DIR=%CD%"

REM Check if virtual environment exists
if not exist "..\venv" (
    echo Error: Virtual environment not found
    echo Please run install.bat first to create the virtual environment
    pause
    exit /b 1
)

REM Activate virtual environment
call ..\venv\Scripts\activate
if errorlevel 1 (
    echo Error: Failed to activate virtual environment
    echo Try running install.bat to create a new environment
    pause
    exit /b 1
)

REM Update pip itself first
echo Updating pip to latest version...
python -m pip install --upgrade pip
if errorlevel 1 (
    echo Warning: Failed to upgrade pip, continuing with updates...
)

REM Navigate to src directory
cd ..\src

REM Backup existing packages
echo Creating backup of current package versions...
pip freeze > requirements.backup.txt

REM Update core dependencies first
echo.
echo Updating core dependencies...
python -m pip install --upgrade numpy==1.24.2
python -m pip install --upgrade torch==2.0.0
if errorlevel 1 (
    echo Error updating core dependencies
    echo Rolling back changes...
    pip install -r requirements.backup.txt
    cd "%ORIGINAL_DIR%"
    pause
    exit /b 1
)

REM Update remaining packages
echo.
echo Updating additional dependencies...
pip install --upgrade -r requirements.txt
if errorlevel 1 (
    echo Error updating dependencies
    echo Rolling back changes...
    pip install -r requirements.backup.txt
    cd "%ORIGINAL_DIR%"
    pause
    exit /b 1
)

REM Clean up backup
del requirements.backup.txt

echo.
echo Verification: Checking installed packages...
pip list

echo.
echo Update completed successfully!
echo If you experience any issues, run install.bat to perform a clean installation.

REM Return to original directory and deactivate virtual environment
cd "%ORIGINAL_DIR%"
deactivate
pause