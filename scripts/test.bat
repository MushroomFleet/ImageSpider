@echo off
setlocal

echo Starting test execution...
echo.

cd ..\src
python -u test_output.py 2>&1
set PYTHON_ERROR=%ERRORLEVEL%
cd ..\scripts

if %PYTHON_ERROR% NEQ 0 (
    echo.
    echo Error: Test failed with error code %PYTHON_ERROR%
    pause
    exit /b 1
)

echo.
echo Test completed successfully!
pause
endlocal