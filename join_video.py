# create by ggvis
# update: 2024年10月23日
# function：输入文件夹，无损合并文件夹内所有视频
import os
import ffmpeg

# 文件夹路径
folder_path = ""
# 获取文件夹中的所有视频文件
video_files = [f for f in os.listdir(folder_path) if f.endswith(('.mp4', '.mkv', '.avi'))] # 可增加视频格式

# 检查是否有视频文件
if not video_files:
    print("文件夹中没有视频文件！")
else:
    # 创建一个合并文件列表
    input_files = [os.path.join(folder_path, f) for f in video_files]
    input_files.sort()

    # 创建一个文本文件列出所有视频文件
    file_list_path = os.path.join(folder_path, 'file_list.txt')
    with open(file_list_path, 'w') as f:
        for file in input_files:
            print(os.path.basename(file))
            f.write(f"file '{file}'\n")

    # 合并文件
    output_file = os.path.join(folder_path,
                               os.path.basename(os.path.normpath(folder_path)) + os.path.splitext(video_files[0])[1]) # 与首个视频后缀相同
    ffmpeg.input(os.path.join(folder_path, 'file_list.txt'), format='concat', safe=0).output(output_file, c='copy').run(quiet=True)

    print("合并完成，输出文件:", output_file)

    # 删除 file_list.txt
    os.remove(file_list_path)
    print("已删除 file_list.txt")
