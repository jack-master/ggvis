# create by ggvis
# update: 2024年10月23日
# function：输入文件夹，无损合并文件夹内所有视频

import os
import ffmpeg

# 文件夹路径
path = r"E:\demo\a" # 文件夹路径
os.chdir(path)
# 获取文件夹中的所有视频文件，可增加视频格式
videos_list = [f for f in os.listdir() if f.endswith(('.mp4', '.mkv', '.avi'))]

# 检查是否有视频文件
if not videos_list:
    print("文件夹中没有视频文件！")
else:
    # 创建一个文本文件列出所有视频件文
    with open('file_list.txt', 'w') as f:
        videos_list.sort()
        for video in videos_list:
            print(video)
            f.write(f"file '{video}'\n")

    # 合并文件
    out_name = os.path.basename(path) + os.path.splitext(videos_list[0])[1] # 与首个视频后缀相同
    ffmpeg.input('file_list.txt', format='concat', safe=0).output(out_name, c='copy').run(quiet=True)

    print("合并完成，输出文件:", out_name)

    # 删除 file_list.txt
    os.remove('file_list.txt')
    print("已删除 file_list.txt")
