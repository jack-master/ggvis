# function：制作MISE内外科症状表，注意几个文件路径
# author：ggvis
# update：20240323


import json

def txt_to_dic(file):
    #读取文件
    with open(file, 'r') as f:
        lines = f.readlines()

    cases = {}

    lines = reversed(lines)
    for line in lines:
        line = line.strip()
        case_name, case_subject, case_symptom = line.split("\t")
        case_name = case_name.replace(" ", "")
        cases[case_name] = case_symptom

    return cases


# 外科
surgery_symptom = "/Users/ggvis/Desktop/MISE_text/surgery_symptom.txt"
surgery_symptom_cases = txt_to_dic(surgery_symptom)
# 内科
internal_medicine_symptom = "/Users/ggvis/Desktop/MISE_text/internal_medicine_symptom.txt"
internal_medicine_symptom_cases = txt_to_dic(internal_medicine_symptom)
#
symptoms = [
    '发热', '皮肤黏膜出血', '水肿', '咳嗽与咳痰', '咯血', '发绀', '呼吸困难', '胸痛', '心悸', '恶心与呕吐',
    '烧心与反流', '吞咽困难', '呕血', '便血', '腹痛', '腹泻', '便秘', '黄疸', '腰背痛', '关节痛', '血尿',
    '尿频/尿急/尿痛', '少尿、无尿与多尿', '尿失禁', '排尿困难', '阴道流血', '肥胖', '消瘦', '头痛', '眩晕',
    '晕厥', '抽搐与惊厥', '意识障碍', '睡眠障碍', '情感症状', '其他症状'
]

internal_medicine_department = {
    "心血管内科":   list(range(1, 15)),
    "呼吸内科":     list(range(15, 34)),
    "消化内科":     list(range(34, 53)),
    "血液内科":     list(range(53, 68)),
    "肾脏内科":     list(range(68, 83)),
    "内分泌科":     list(range(83, 94)),
    "风湿免疫科":   list(range(94, 107)),
    "神经内科":     list(range(107, 120)),
    "急诊内科":     list(range(120, 132)),
    "老年科":       list(range(132, 134))
}

all_cases ={
    "Surgery": surgery_symptom_cases,
    "Internal_Medicine": internal_medicine_symptom_cases,
    "symptoms": symptoms,
    "Internal_Medicine_department": internal_medicine_department
}

# 保存为 JSON 文件
new_file_name = "/Users/ggvis/Desktop/MISE_text/case_symptom.json"
with open(new_file_name, 'w') as json_file:
    json.dump(all_cases, json_file, ensure_ascii=False, indent=4)
