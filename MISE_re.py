import os
import re
import json

os.chdir(r"E:\demo") # 需要修改文件路径
with open("neike.txt", encoding="gb18030") as f:
    text = f.read()

cases = []

pattern = re.compile(r"\n案例\d{1,3}+.*?(?=\n案例\d{1,3}+[^\n]|$)", re.DOTALL)
matches = pattern.finditer(text)

for match in matches:
    cases_info = []

    match = match.group() # 完整案例

    pattern_medical_record_datas = re.search(r"病[历史例]资料(.*?)二、 诊治经过", match, re.DOTALL) # 一、病历资料
    if pattern_medical_record_datas:
        for pattern_medical_record_data in pattern_medical_record_datas.groups(1):

            present_history_pattern = re.search(r"现病史(.*?)2 既往史", pattern_medical_record_data, re.DOTALL) # 现病史
            present_history = present_history_pattern.group(1).strip() if present_history_pattern else "未提及"

            past_history_pattern = re.search(r"既往史(.*?)3 体格检查", pattern_medical_record_data, re.DOTALL)  # 既往史
            past_history = past_history_pattern.group(1).strip() if past_history_pattern else "未提及"

            physical_examination_pattern = re.search(r"体格检查(.*?)[34] 实验室.*?检查", pattern_medical_record_data, re.DOTALL)  # 体格检查
            if not physical_examination_pattern:
                physical_examination_pattern = re.search(r"体格检查(.*+)", pattern_medical_record_data, re.DOTALL)
            physical_examination = physical_examination_pattern.group(1).strip() if physical_examination_pattern else "未提及"

            auxiliary_examination_pattern = re.search(r"[34] 实验室.*?检查(.*+)", pattern_medical_record_data, re.DOTALL) # 辅助检查
            auxiliary_examination = auxiliary_examination_pattern.group(1).strip() if auxiliary_examination_pattern else "未提及"

    else:
        present_history = past_history = physical_examination = auxiliary_examination = "未提及0"

    diagnosis_and_treatment_process_patterns = re.search(r"、 诊治经过(.*?)三、 病[例历]分析", match, re.DOTALL) # 二、诊治经过
    if diagnosis_and_treatment_process_patterns:
        for diagnosis_and_treatment_process in diagnosis_and_treatment_process_patterns.groups(1):

            preliminary_diagnosis_pattern = re.search(r"初步诊断：(.*?)。", diagnosis_and_treatment_process, re.DOTALL) # 初步诊断
            preliminary_diagnosis = preliminary_diagnosis_pattern.group(1).strip() if preliminary_diagnosis_pattern else "未提及"

            treatment_process_pattern = re.search(r"诊[治疗断]经过[：:](.*+)", diagnosis_and_treatment_process, re.DOTALL) # 诊疗过程
            if not treatment_process_pattern:
                treatment_process_pattern = re.search(r"。(.*+)", diagnosis_and_treatment_process, re.DOTALL)  # 诊疗过程
            treatment_process = treatment_process_pattern.group(1).strip() if treatment_process_pattern else "未提及"

    else:
        preliminary_diagnosis = treatment_process = "未提及0"

    pattern_case_analysises = re.search(r"、 病[例历]分析\n(.*?)\n四、 要点[与及和]讨论", match, re.DOTALL) # 三、病历分析
    if pattern_case_analysises:
        for case_analysis in pattern_case_analysises.groups(1):

            pattern_history_features = re.search(r" 病史特点\n(.*?)\n\d 诊断[与及和]诊断依据", case_analysis, re.DOTALL) # 病史特点
            history_features = pattern_history_features.group(1).strip() if pattern_history_features else "未提及"

            pattern_diagnosis_and_diagnosis_basis = re.search(r" 诊断[与及和]诊断依据\n(.*?)\n\d 处理方案及理由", case_analysis, re.DOTALL)  # 诊断及依据
            diagnosis_and_diagnosis_basis = pattern_diagnosis_and_diagnosis_basis.group(1).strip() if pattern_diagnosis_and_diagnosis_basis else "未提及"

            pattern_treatment_plan_and_reason = re.search(r" (处理方案及理由|处理原则及具体措施)\n(.*+)", case_analysis, re.DOTALL)  # 治疗方案
            treatment_plan_and_reason = pattern_treatment_plan_and_reason.group(2).strip() if pattern_treatment_plan_and_reason else "未提及"

    else:
        history_features = diagnosis_and_diagnosis_basis = treatment_plan_and_reason = "未提及0"



    pattern_key_points_and_discussion = re.search(r"要点[与及和]讨论\n(.*?)\n五、", match, re.DOTALL)  # 四、要点与讨论
    key_points_and_discussion = pattern_key_points_and_discussion.group(1).strip() if pattern_key_points_and_discussion else "未提及"

    pattern_thinking_questions = re.search(r"(思考题|思考问题)\n(.*?)六、 推荐阅读", match, re.DOTALL)  # 五、思考题
    thinking_questions = pattern_thinking_questions.group(2).strip() if pattern_thinking_questions else "未提及"

    pattern_literature = re.search(r"(推荐阅读文献|推荐阅读的参考书)(.*?)\n[(（]", match, re.DOTALL)  # 六、文献
    literature = pattern_literature.group(2).strip() if pattern_literature else "未提及"


    cases_info = {
        "medical_record_data":{
            "present_history":present_history,
            "past_history":past_history,
            "physical_examination":physical_examination,
            "auxiliary_examination":auxiliary_examination
        },
        "diagnosis_and_treatment_process":{
            "preliminary_diagnosis":preliminary_diagnosis,
            "treatment_process":treatment_process
        },
        "case_analysis": {
            "history_features":history_features,
            "diagnosis_and_diagnosis_basis":history_features,
            "treatment_plan_and_reason":treatment_plan_and_reason,
        },
        "key_points_and_discussion":key_points_and_discussion,
        "thinking_questions":thinking_questions,
        "literature":literature
    }

    cases.append(cases_info)

print(len(cases))


with open("neike.json", "w", encoding='utf-8') as f:
    json.dump(cases, f, indent=4, ensure_ascii=False)
