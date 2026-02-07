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
You must update the paths in SquashDrop.bat to match your local installation.

### To find CONDA_PATH: Open PowerShell and run:

PowerShell:
```
(Get-Command conda).Source.Replace("Scripts\conda.exe", "condabin\conda.bat")
```

### To find SCRIPT_PATH: 

Folder with this cloned this repository + \crop_tool.py

## Update these variables in SquashVid.bat:
```
set "CONDA_PATH=C:\YOUR_PATH_HERE\condabin\conda.bat"
set "SCRIPT_PATH=C:\YOUR_PATH_HERE\squash_tool.py"
```


---



# 4. Usage Instructions
Drag and Drop: Drag the target video file onto the CropDrop.bat icon.
Create links/shortcuts to the .bat file to use this function in other directories or from the desktop.

An interactive window will open displaying the first frame of the video.
Left-click and drag the mouse to draw a rectangle over the desired area.
Confirm: Press ENTER or SPACE to confirm.

Output: The script will process the video. The result is saved in the source directory with the suffix _cropped.mp4.



---




# 5. Troubleshooting
'ffmpeg' is not recognized: Ensure FFmpeg is installed. If it is installed but not in your System PATH, you can specify the absolute path to ffmpeg.exe inside the crop_tool.py script in the cmd list.

Window closes immediately: This usually indicates an incorrect path in the CONDA_PATH or SCRIPT_PATH variables. Double-check that both files exist at the specified locations.

File in use error: Ensure the video file you are trying to crop is not open in another application (e.g., VLC, Windows Media Player, or Premiere Pro) during processing.

OpenCV Window doesn't appear: Verify that the cropvid environment was created successfully and that opencv-python is installed within it.



---




# 6. FFMPEG Technical Specifications
Video Encoding: Uses libx264 with a Constant Rate Factor (CRF) of 23.
Speed Preset: Set to slow for optimized compression efficiency.
Audio Handling: Audio is passed through using -c:a copy to ensure no loss in quality or synchronization.
ROI Interface: Handled via cv2.selectROI.
