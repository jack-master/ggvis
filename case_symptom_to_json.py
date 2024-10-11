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
        case_name = case_name.replace(" ", "_")
        cases[case_name] = case_symptom

    return cases



surgery_symptom = "/Users/ggvis/Desktop/MISE_text/surgery_symptom.txt"
surgery_symptom_cases = txt_to_dic(surgery_symptom)
internal_medicine_symptom = "/Users/ggvis/Desktop/MISE_text/internal_medicine_symptom.txt"
internal_medicine_symptom_cases = txt_to_dic(internal_medicine_symptom)

all_cases ={
    "Surgery": surgery_symptom_cases,
    "Internal_Medicine": internal_medicine_symptom_cases
}

# 保存为 JSON 文件
new_file_name = "/Users/ggvis/Desktop/MISE_text/case_symptom.json"
with open(new_file_name, 'w') as json_file:
    json.dump(all_cases, json_file, ensure_ascii=False, indent=4)
