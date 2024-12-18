# create by ggvis
# update: 2024年10月10日
# function：整理上交的TXT文档

import re

# 普通查找替换的映射
mapping_table = {
    # 普通查找替换
    # "old_text": "new_text"
    "HCO-3"     :"HCO3-",
    "kg/m2"     :"kg/m^2",
    "TSpot"    :"T-SPOT",
    "Tspot"    :"T-SPOT",
    "TSPOT"     :"T-SPOT",
    "PETCT"    :"PET-CT",
    "PET/CT"    :"PET-CT",
    "PETCT"    :"PET-CT",
}

# 打开原文件读取内容
with open("E:\\oringe_text.txt", 'r', encoding='gb18030') as file:
    text = file.read()

# 普通查找替换
for old_text, new_text in mapping_table.items():
    text = text.replace(old_text, new_text)

# 正则查找替换，采用伟大的lambda函数表达式
text = re.sub(r'×10(?=([3-9]|1[0-5])[^cm ])', lambda x: x.group(0) + "^", text) # 科学计数法
text = re.sub(r'(?<=\d)[kdcmμnp]m', lambda x: " "+ x.group(0), text) # 长度
text = re.sub(r'(?<=\d)[kdcmμnp]g', lambda x: " "+ x.group(0), text) # 质量
text = re.sub(r'(?<=\d)[mμnp]?mol', lambda x: " "+ x.group(0), text) # 物质的量
text = re.sub(r'（见图\d+）', "", text) # 删除“（见图）”

#print(text)

with open("E:\\cleard_text.txt", 'w', encoding='gb18030') as file:
    file.write(text)
