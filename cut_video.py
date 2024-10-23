# create by ggvis
# update: 2024年10月23日
# function：批量无损裁剪视频，输出目录、后缀与输入相同

import ffmpeg
import os

# 输入数据
clips = [
    #[start_time, end_time, "输出文件名"],
    #["hh:mm:ss", "hh:mm:ss", "outname"],
    ["00:00:00", "01:03:29", '1'],
    ["01:03:29", "02:00:00", '2'],
]

# 原视频文件
input_file = ""  # 带路径和后缀的完整文件名
# 获取目录路径
directory_path = os.path.dirname(input_file)
# 获取文件名（不带扩展名）和拓展名
file_name, file_extension = os.path.splitext(os.path.basename(input_file))


for start, end, out_name in clips:
    full_out_name = os.path.join(directory_path, out_name + file_extension)
    ffmpeg.input(input_file, ss=start, to=end).output(full_out_name, c='copy').run(quiet=True)
    print(f"已裁剪 {start} 到 {end} 保存为：{out_name}")
