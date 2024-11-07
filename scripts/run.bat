@echo off
setlocal enabledelayedexpansion
cls

echo ImageSpider Processing Tool
echo =========================
echo.

REM Store original directory
set "ORIGINAL_DIR=%CD%"

echo [1/6] Checking environment...
echo -----------------------------
call ..\venv\Scripts\activate
if errorlevel 1 (
    echo [ERROR] Virtual environment not found. Please run install.bat first.
    pause
    exit /b 1
)
echo [OK] Environment activated
echo.

echo [2/6] Input configuration...
echo ---------------------------
:INPUT_PATH
echo Enter the path to your images folder (relative or absolute):
echo Example: ..\images or C:\Users\YourName\Pictures
echo.
set /p "IMAGE_FOLDER="

REM Remove quotes if present
set IMAGE_FOLDER=!IMAGE_FOLDER:"=!

echo.
echo [3/6] Validating path...
echo -----------------------
echo Checking: !IMAGE_FOLDER!

REM Convert to absolute path
pushd "!IMAGE_FOLDER!" 2>nul
if errorlevel 1 (
    echo.
    echo [ERROR] Cannot access the specified path
    pause
    exit /b 1
)
set "IMAGE_FOLDER=!CD!"
popd

echo [OK] Path validated: !IMAGE_FOLDER!
echo.

echo [4/6] Setting up environment...
echo -----------------------------
set "IMAGE_FOLDER=!IMAGE_FOLDER!"
echo [OK] Environment configured
echo.

echo [5/6] Starting Python processor...
echo -------------------------------
cd ..\src
echo [OK] Directory changed
echo.

echo [6/6] Running image processing...
echo ------------------------------
echo Start Time: %TIME%
echo.
echo Processing will begin in 3 seconds...
timeout /t 3 /nobreak >nul

cls
echo ImageSpider Processing Tool - Running
echo ===================================
echo Processing started at: %TIME%
echo Using folder: !IMAGE_FOLDER!
echo.
echo Processing... Please wait...
echo.

python -u ImageSpiderV1.py 2>&1
set PYTHON_ERROR=%ERRORLEVEL%

echo.
echo End Time: %TIME%
echo.

cd ..\scripts

if %PYTHON_ERROR% NEQ 0 (
    echo [ERROR] Processing failed with error code %PYTHON_ERROR%
    cd "%ORIGINAL_DIR%"
    deactivate
    pause
    exit /b 1
)

REM Return to original directory and deactivate virtual environment
cd "%ORIGINAL_DIR%"
deactivate

echo ================================
echo Processing completed successfully
echo ================================
pause
endlocal