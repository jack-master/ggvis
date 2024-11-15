# create by ggvis
# update: 2024年11月15日
# function：文件查重并移动到《duplicate_folder》，不包含子目录，适用于小文件

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
    
    files_by_hash = {}
    total_files = sum([len(files) for root, _, files in os.walk(folder) if destination_folder not in root])

    processed_files = 0

    for root, _, files in os.walk(folder):
        # 忽略重复文件夹中的文件
        if destination_folder in root:
            continue
        for file in files:
            processed_files += 1
            file_path = os.path.join(root, file)

            file_hash = calculate_sha1(file_path)
            if file_hash in files_by_hash:
                # 找到重复文件，移动到duplicates文件夹
                destination_path = os.path.join(destination_folder, os.path.basename(file_path))
                shutil.move(file_path, destination_path)
                print(f"重复: {files_by_hash[file_hash]} 与 {file_path} --> 《{destination_folder}》")
            else:
                files_by_hash[file_hash] = file_path
            
            print(f"\r{processed_files}/{total_files} 文件处理完成 ({processed_files / total_files * 100:.2f}%)", end='', flush=True)

    print("文件处理完成！")


# 调用函数
folder_path = r'E:\demo'
find_and_move_duplicates(folder_path)
