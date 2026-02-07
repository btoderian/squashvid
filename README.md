# Video Recompression Tool
A utility for compressing large video files (like stream captures) using Python and FFmpeg via a drag-and-drop batch interface.

---


# 1. Prerequisites
Miniconda or Anaconda
https://docs.anaconda.com/miniconda/


---


# 2. Environment Setup
Create a dedicated Conda environment to manage dependencies and avoid global system conflicts

Powershell:
```
# Create the environment
conda create -n squashvid -c conda-forge python=3.10 ffmpeg send2trash pywin32 -y
```


---


# 3. Local Configuration
You must update the paths in SquashVid.bat to match your local installation.

### To find CONDA_PATH: Open PowerShell and run:

PowerShell:
```
(Get-Command conda).Source.Replace("Scripts\conda.exe", "condabin\conda.bat")
```

### To find SCRIPT_PATH: 

Folder with this cloned this repository + \squash_tool.py

## Update these variables in SquashVid.bat:
```
set "CONDA_PATH=C:\YOUR_PATH_HERE\condabin\conda.bat"
set "SCRIPT_PATH=C:\YOUR_PATH_HERE\squash_tool.py"
```


---



# 4. Usage Instructions
Drag and Drop: Drag the target video file(s) onto the SquashVid.bat icon.
Create links/shortcuts to the .bat file to use this function in other directories or from the desktop.

Output: The script will process the video. The result is saved in the source directory with the suffix _h265.mp4.

File Management: Original files are moved to the System Recycle Bin only after successful verification of the output.

---




# 5. Troubleshooting
'ffmpeg' is not recognized: Ensure FFmpeg is installed. If it is installed but not in your System PATH, you can specify the absolute path to ffmpeg.exe inside the squash_tool.py script in the cmd list.

Window closes immediately: This usually indicates an incorrect path in the CONDA_PATH or SCRIPT_PATH variables. Double-check that both files exist at the specified locations.

File in use error: Ensure the video file you are trying to compress is not open in another application (e.g., VLC, Windows Media Player, or Premiere Pro) during processing.

Missing _h265.mp4 file: If the original file is gone but no new file appeared, check your disk space. FFmpeg will fail if there isn't enough room to write the new file, but the script is designed not to trash your original unless the squash is verified.

---




# 6. FFMPEG Technical Specifications

Video Encoding: Uses HEVC via libx265 encoder with Constant Rate Factor (CRF) of 26.  Target = 10:1 compression

Speed Preset: Set to slow for optimized compression efficiency and redundant data reduction.

Audio Handling: Audio is passed through using -c:a copy to ensure no loss in quality or synchronization.
