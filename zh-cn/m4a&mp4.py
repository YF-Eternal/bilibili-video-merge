import os
import subprocess


# 检测m4a和MP4文件路径
m4a_file = None
mp4_file = None

for file in os.listdir():
    if file.endswith('.m4a'):
        m4a_file = os.path.join(file)
    elif file.endswith('.mp4'):
        mp4_file = os.path.join(file)

# 确保找到了m4a和MP4文件
if m4a_file is None or mp4_file is None:
    print("未找到M4A或MP4文件")
    exit(1)

# 输出文件路径
output_file = os.path.join('合并后 - ' + mp4_file)

# 使用FFmpeg合并文件
command = f'ffmpeg -i "{m4a_file}" -i "{mp4_file}" -c copy "{output_file}"'

try:
    subprocess.run(command, check=True, shell=True)
    print("文件合并成功")
except subprocess.CalledProcessError as e:
    print("文件合并失败:", e)

input("\n按回车键关闭")