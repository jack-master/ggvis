# function：给出挑选好的案例，并给出症状及频次，注意几个文件路径
# author：ggvis
# update：20241012

import re
import json
from collections import Counter


# 定义一个函数来从文本中提取案例信息
def extract_case_info(text):
    cases = []

    case_pattern = re.compile(r"\n(案例.*?既往史)", re.DOTALL)
    for match in case_pattern.finditer(text):
        match = match.group(1)

        # 提取案例名
        case_title_pattern = re.search(r"案例[ \d].*", match)
        case_title = case_title_pattern.group() if case_title_pattern else " "

        # 提取案例名
        patient_sex_age_chief_complaint_pattern = re.search(r"患者，([男女]性)，(\d+岁)，因“(.*?)”", match)
        if patient_sex_age_chief_complaint_pattern:
            # 多次赋值合并啦
            patient_sex, patient_age, chief_complaint = (patient_sex_age_chief_complaint_pattern.group(i)  for i in (1, 2, 3))
        else:# 如果上面性别、年龄、主诉没有一起匹配到，就单独匹配
            patient_sex_pattern = re.search(r"，([男女]性)，", match)
            patient_sex = patient_sex_pattern.group(1) if patient_sex_pattern else " " # 性别实在找不到就空着
            patient_age_pattern = re.search(r"，(\d+岁)，", match)
            patient_age = patient_age_pattern.group(1) if patient_age_pattern else " " # 年龄实在找不到也空着
            chief_complaint_pattern = re.search(r"因“(.*?)”", match)
            chief_complaint = chief_complaint_pattern.group(1) if chief_complaint_pattern else " " # 主诉实在找不到也空着


        # 构建案例信息字典
        case_info = {
            "case_title": case_title,
            "patient_sex": patient_sex,
            "patient_age": patient_age,
            "chief_complaint": chief_complaint,
        }
        cases.append(case_info)

    return cases


# 加载症状字典表
case_symptom = "/Users/ggvis/Desktop/MISE_text/case_symptom.json"
with open(case_symptom, 'r', encoding='utf-8') as json_file:
    case_symptom = json.load(json_file)
    Surgery = case_symptom["Surgery"] # 外科案例与症状字典
    Internal_Medicine = case_symptom["Internal_Medicine"] # 内科案例与症状字典
    Internal_Medicine_department = case_symptom["Internal_Medicine_department"] # 内科案例与科室字典


# 这是挑出来的案例
case_numbers = (
    1, 3, 6, 7, 10, 11, 12, 13, 17, 19, 20, 21, 24, 25, 28, 34, 35, 36,
    44, 45, 46, 48, 49, 53, 54, 55, 57, 59, 66, 67, 68, 70, 81, 82, 87,
    88, 90, 93, 94, 95, 96, 97, 108, 109, 111, 114, 116, 117, 121, 122,
    123, 127, 132, 133
)


# 导入整本病历
MISE_filter_case_input = "/Users/ggvis/Desktop/MISE_text/MISE_filter_case_input.txt"
with open(MISE_filter_case_input, 'r', encoding='gb18030') as f:
    content = f.read()

case_infos = extract_case_info(content)

# 新的案例
for i in range(len(case_infos)):
    case_infos[i]["show"] = True if (i+1) in case_numbers else False # 要不要作为展示病历
    case_infos[i]["symptom"] = list(Internal_Medicine.items())[i][1]
    for department, case_range in Internal_Medicine_department.items(): # 科室
        if (i+1) in case_range:
            case_infos[i]["department"] = department



# 保存为 JSON 文件
new_file_name = "/Users/ggvis/Desktop/MISE_text/filter_cases.json"
with open(new_file_name, 'w') as json_file:
    json.dump(case_infos, json_file, ensure_ascii=False, indent=4)

# 计算摘要信息：
cases_sum =  len(case_infos) # 总的病历数
show_sum = 0 # 挑选出来的病历数
symptom_counter = Counter()# 提取所有症状并计数

for case_info in case_infos:
    show_sum += 1 if case_info["show"] else 0 # 挑选show
    symptom = case_info.get("symptom", "").split(",")  # 分割症状
    symptom_counter.update(symptom)  # 更新症状计数
    common_symptoms = symptom_counter.most_common() # 症状从高到低排序

print(f"show案例数：{show_sum} / {cases_sum} 个")
# 打印每个症状及其出现次数
print("症状：出现次数")
for symptom, count in common_symptoms:
    print(f"{symptom}: {count}")
