# create by ggvis
# update: 2024年11月8日
# function：字符串批量查找替换，支持普通查找替换、正则查找替换。

import re

# 字典，包含要替换的字符串
replacements = {
    "old1": "new1",
    "old2": "new2"
}

# 字典，包含正则表达式和对应的处理函数
patterns = {
    # key 为要匹配的表达式，value为lambda表达式
    r"见图\d+": lambda x: x.group(0) + "^"
}

# 待替换的原始字符串
text = ("This is old1, this is old2, and this is old3.\n"
        "这是见图123的描述，另一个见图456的例子，见图789最后一个图。")

# 普通查找替换
for old, new in replacements.items():
    text = text.replace(old, new)

# 正则查找替换
for pattern, func in patterns.items():
    text = re.sub(pattern, func, text)

print(text)
