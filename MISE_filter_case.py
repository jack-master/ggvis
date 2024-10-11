import re
import json

file = "E:\\MISE_filter_case_input.txt"

with open(file, 'r', encoding='gb18030') as f:
    text = f.read()

# 案例1慢性心力衰竭
#
# 案例1
#
#
#
# 慢性心力衰竭
#
# 一、 病历资料
# 1 现病史
# 患者，男性，58岁，因“反复胸闷气急伴双下肢水肿7年，加重3个月”入院。
#
# case_pattern = re.compile(r"案例\d+\S+.*?患者，[男女]性，\d+岁，因“\S+”入院", re.DOTALL)
# out = case_pattern.findall(text)
# print(out)
#
#


# 定义一个函数来从文本中提取案例信息
def extract_case_info(text):
    cases = []
    case_pattern = re.compile(r"(案例\d+\S+).*?患者，([男女]性)，(\d+岁)，因“(\S+)”入院", re.DOTALL)
    for match in case_pattern.finditer(text):
        case_title = match.group(1)
        patient_sex = match.group(2)
        patient_age = match.group(3)
        chief_complaint = match.group(4)

        # 构建案例信息字典
        case_info = {
            "case_title": case_title,
            "patient_name": patient_sex,
            "patient_age": patient_age,
            "chief_complaint": chief_complaint
        }
        cases.append(case_info)

    return cases

file = "E:\\MISE_filter_case_input.txt"

with open(file, 'r', encoding='gb18030') as f:
    text = f.read()


department_table = {
    "心血管内科": tuple(range(1, 15)),
    "呼吸内科": tuple(range(15, 34)),
    "消化内科": tuple(range(34, 53)),
    "血液内科": tuple(range(53, 68)),
    "肾脏内科": tuple(range(68, 83)),
    "内分泌科": tuple(range(83, 94)),
    "风湿免疫科": tuple(range(94, 107)),
    "神经内科": tuple(range(107, 120)),
    "急诊内科": tuple(range(120, 132)),
    "老年科": tuple(range(132, 133))
}

case_numbers = (
    1, 3, 6, 7, 10, 11, 12, 13, 17, 19, 20, 21, 24, 25, 28, 34, 35, 36,
    44, 45, 46, 48, 49, 53, 54, 55, 57, 59, 66, 67, 68, 70, 81, 82, 87,
    88, 90, 93, 94, 95, 96, 97, 108, 109, 111, 114, 116, 117, 121, 122,
    123, 127, 132, 133
)
print(len(case_numbers))

# 提取并打印JSON格式的案例信息
case_infos = extract_case_info(text)
# for case_info in case_infos:
#     print(case_info)

for case_number in case_numbers:
    for department, case_range in department_table.items():
        if case_number in case_range:
            case_infos[case_number-1]["case_number"] = case_number
            case_infos[case_number-1]["department"] = department
            print(case_infos[case_number-1])



