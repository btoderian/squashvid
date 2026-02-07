@echo off
setlocal

:: 1. Define paths
set "CONDA_PATH=C:\Users\JehutyAdmin\anaconda3\condabin\conda.bat"
set "SCRIPT_PATH=D:\SquashVid\squash_tool.py"

:: 2. Check if a file was dropped
if "%~1"=="" (
    echo [ERROR] No file detected. Drag a video file onto this icon.
    pause
    exit /b
)

:: 3. Define output path for the final message
set "OUT_FILE=%~dpn1_h265.mp4"

:: 4. Execute
echo [START] Processing: %~nx1
:: Using 'call' with fully quoted arguments to handle spaces in file paths
call "%CONDA_PATH%" run -n squashvid --no-capture-output python "%SCRIPT_PATH%" %*

:: 5. Cleanup and Readout
echo.
echo Batch complete.
echo Last processed output location: %OUT_FILE%
echo.

endlocal
pause
