import os
import sys
import subprocess
from send2trash import send2trash

# CONFIGURATION
# CRF 26 targets that ~10:1 ratio for high-bitrate clips
TARGET_CRF = "26" 

def squash_video(input_path):
    # Create output filename
    output_path = os.path.splitext(input_path)[0] + "_h265.mp4"
    file_size_mb = os.path.getsize(input_path) / (1024 * 1024)
    
    print(f"\n>>> Squashing: {os.path.basename(input_path)} ({file_size_mb:.1f}MB)")

    # FFmpeg Command
    # libx265 + slow preset targets the 100MB/1GB goal
    cmd = [
        "ffmpeg", "-i", input_path,
        "-c:v", "libx265",
        "-crf", TARGET_CRF,
        "-preset", "slow",
        "-c:a", "copy",
        "-y", output_path
    ]

    try:
        subprocess.run(cmd, check=True)
        
        # Verify success before trashing original
        if os.path.exists(output_path) and os.path.getsize(output_path) > 0:
            new_size_mb = os.path.getsize(output_path) / (1024 * 1024)
            print(f"--- Success! New size: {new_size_mb:.1f}MB")
            
            print(f"--- Moving original to Recycle Bin...")
            send2trash(input_path)
        else:
            print("--- Error: Output file was not created correctly.")
            
    except subprocess.CalledProcessError:
        print(f"--- FFMPEG ERROR: Failed to process {input_path}")
    except Exception as e:
        print(f"--- SYSTEM ERROR: {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("No files detected. Drag and drop videos onto the .bat file.")
    else:
        for file_path in sys.argv[1:]:
            if os.path.isfile(file_path):
                squash_video(file_path)
    
    print("\nBatch complete.")
    input("Press Enter to close...")