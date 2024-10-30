# create by ggvis
# update: 2024年10月23日
# function：批量无损裁剪视频，输出目录、后缀与输入相同

import ffmpeg
import os

# 输入数据
clips = [
    #[start_time, end_time, "输出文件名（不带后缀）"],
    #["hh:mm:ss", "hh:mm:ss", "outname without suffix"],
    ["00:00:00", "00:02:15", '1'],
    ["00:00:15", "00:03:30", '2'],
]

# 原视频文件
path = r"E:\demo\a"  # 路径
file = r"1.1 in put.mp4" # 带后缀的文件名
os.chdir(path)

# 获取文件名（不带扩展名）和拓展名
file_name, file_suffix = os.path.splitext(file)

for start, end, out_name in clips:
    ffmpeg.input(file, ss=start, to=end).output(out_name + file_suffix, c='copy').run(quiet=True)
    print(f"已裁剪 {start} 到 {end} 保存为：{out_name}")
