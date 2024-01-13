import os
import subprocess


# Detect m4s and MP4 file paths
m4s_file = None
mp4_file = None

for file in os.listdir():
    if file.endswith('.m4s'):
        m4s_file = os.path.join(file)
    elif file.endswith('.mp4'):
        mp4_file = os.path.join(file)

# Make sure m4s and MP4 files are found
if m4s_file is None or mp4_file is None:
    print("M4S or MP4 file not found!")
    exit(1)

# Output file path
output_file = os.path.join('After merge - ' + mp4_file)

# Merge files using FFmpeg
command = f'ffmpeg -i "{m4s_file}" -i "{mp4_file}" -c copy "{output_file}"'

try:
    subprocess.run(command, check=True, shell=True)
    print("File merge successful!")
except subprocess.CalledProcessError as e:
    print("File merge failed:", e)

input("\nPress Enter key to close.")