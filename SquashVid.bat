@echo off
setlocal

:: 1. Define the absolute path to your conda batch file and python script
set "CONDA_PATH=C:\Users\JehutyAdmin\anaconda3\condabin\conda.bat"
set "SCRIPT_PATH=D:\SquashVid\squash_tool.py"

:: 2. Check if a file was dropped
if "%~1"=="" (
    echo [ERROR] No file detected. Drag a video file onto this icon.
    pause
    exit /b
)

:: 3. Identify the Output Path for the Readout
set "OUT_FILE=%~dpn1_h265.mp4"

:: 4. Execute in the 'squashvid' environment
echo [START] Processing: %~nx1
:: Using 'call' with fully quoted arguments to handle spaces in file paths
call "%CONDA_PATH%" run -n squashvid --no-capture-output python "%SCRIPT_PATH%" "%~1"

:: 5. Readout
echo.
echo %OUT_FILE%
echo.

endlocal
pause
