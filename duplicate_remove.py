import os
import hashlib
import shutil

# 文件夹路径
folder_path = r''
os.chdir(folder_path)

# 用于存储文件哈希值和文件大小
file_hashes = {}
file_sizes = {}

# 获取文件的哈希值
def get_file_hash(file_path):
    hash_sha1 = hashlib.sha1()  # 使用SHA-1算法
    with open(file_path, 'rb') as f:
        while chunk := f.read(8192):
            hash_sha1.update(chunk)
    return hash_sha1.hexdigest()

# 判断“duplicate_folder”文件夹是否存在，如果不存在，则创建
if not os.path.exists("duplicate_folder"):
    os.makedirs("duplicate_folder")

# 获取文件总数，用于进度计算
total_files = len([file_name for file_name in os.listdir() if os.path.isfile(file_name)])
processed_files = 0

# 遍历指定文件夹下的所有文件（不包括子目录）
for file_name in os.listdir():
    if os.path.isfile(file_name):  # 只处理文件，不处理目录
        file_size = os.path.getsize(file_name)

        # 先比较文件大小
        if file_size in file_sizes:
            # 如果文件大小相同，才计算 SHA-1 哈希值
            file_hash = get_file_hash(file_name)

            if file_hash in file_hashes:
                # 如果是重复文件，移动到“重复文件”文件夹
                new_file_name = os.path.join("duplicate_folder", file_name)
                shutil.move(file_name, new_file_name)
                print(f"重复：{file_hashes[file_hash]} 与 {file_name} -->《duplicate_folder》")
            else:
                file_hashes[file_hash] = file_name
        else:
            # 如果文件大小不同，直接记录文件大小和文件名
            file_sizes[file_size] = file_name
            file_hash = get_file_hash(file_name)
            file_hashes[file_hash] = file_name

        # 更新进度（不换行）
        processed_files += 1
        progress = (processed_files / total_files) * 100
        print(f"\r进度: {processed_files}/{total_files} 文件处理完成 ({progress:.2f}%)", end='', flush=True)

print("\n处理完成!")