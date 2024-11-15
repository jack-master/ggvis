# create by ggvis
# update: 2024年11月15日
# function：文件查重并移动到《duplicate_folder》，包含子目录，适合大文件，先比较大小，再比较哈希值，减少计算量

import os
import shutil
import hashlib

def calculate_sha1(file_path):
    """计算文件的SHA-1哈希值"""
    sha1 = hashlib.sha1()
    with open(file_path, 'rb') as f:
        while chunk := f.read(8192):
            sha1.update(chunk)
    return sha1.hexdigest()

def find_and_move_duplicates(folder):
    """查找并移动重复文件"""
    destination_folder = os.path.join(folder, "duplicates")
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    files_by_size = {}

    # 遍历文件，按大小分组
    for root, _, files in os.walk(folder):
        for file in files:
            file_path = os.path.join(root, file)
            # 忽略重复文件夹中的文件
            if destination_folder in root:
                continue
            file_size = os.path.getsize(file_path)

            if file_size not in files_by_size:
                files_by_size[file_size] = []
            files_by_size[file_size].append(file_path)

    # 初始化进度计数器
    total_files = sum(len(files) for files in files_by_size.values())
    processed_files = 0

    # 对于大小相同的文件，计算SHA-1哈希值
    for file_list in files_by_size.values():

        if len(file_list) < 2:
            processed_files += len(file_list)
            progress = (processed_files / total_files) * 100
            print(f"\r进度: {processed_files}/{total_files} 文件处理完成 ({progress:.2f}%)", end='', flush=True)
            continue

        hashes = {}
        for file_path in file_list:
            file_hash = calculate_sha1(file_path)
            if file_hash in hashes:
                # 打印提示信息
                print(f"重复: {hashes[file_hash]} 与 {file_path} --> 《{destination_folder}》")
                destination_path = os.path.join(destination_folder, os.path.basename(file_path))
                shutil.move(file_path, destination_path)

            else:
                hashes[file_hash] = file_path

            # 更新进度计数器
            processed_files += 1
            progress = (processed_files / total_files) * 100
            # 打印进度信息
            print(f"\r进度: {processed_files}/{total_files} 文件处理完成 ({progress:.2f}%)", end='', flush=True)

    print("\n处理完成!")

# 调用函数
folder_path = r'E:\demo'
find_and_move_duplicates(folder_path)
