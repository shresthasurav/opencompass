from opencompass.openicl.icl_prompt_template import PromptTemplate
from opencompass.openicl.icl_retriever import FixKRetriever
from opencompass.openicl.icl_inferencer import PPLInferencer
from opencompass.openicl.icl_evaluator import AccEvaluator
from opencompass.datasets import CEvalDataset

ceval_subject_mapping = {
    "computer_network":
    ["Computer Network", "\u8ba1\u7b97\u673a\u7f51\u7edc", "STEM"],
    "operating_system":
    ["Operating System", "\u64cd\u4f5c\u7cfb\u7edf", "STEM"],
    "computer_architecture":
    ["Computer Architecture", "\u8ba1\u7b97\u673a\u7ec4\u6210", "STEM"],
    "college_programming":
    ["College Programming", "\u5927\u5b66\u7f16\u7a0b", "STEM"],
    "college_physics": ["College Physics", "\u5927\u5b66\u7269\u7406", "STEM"],
    "college_chemistry":
    ["College Chemistry", "\u5927\u5b66\u5316\u5b66", "STEM"],
    "advanced_mathematics":
    ["Advanced Mathematics", "\u9ad8\u7b49\u6570\u5b66", "STEM"],
    "probability_and_statistics":
    ["Probability and Statistics", "\u6982\u7387\u7edf\u8ba1", "STEM"],
    "discrete_mathematics":
    ["Discrete Mathematics", "\u79bb\u6563\u6570\u5b66", "STEM"],
    "electrical_engineer": [
        "Electrical Engineer", "\u6ce8\u518c\u7535\u6c14\u5de5\u7a0b\u5e08",
        "STEM"
    ],
    "metrology_engineer":
    ["Metrology Engineer", "\u6ce8\u518c\u8ba1\u91cf\u5e08", "STEM"],
    "high_school_mathematics":
    ["High School Mathematics", "\u9ad8\u4e2d\u6570\u5b66", "STEM"],
    "high_school_physics":
    ["High School Physics", "\u9ad8\u4e2d\u7269\u7406", "STEM"],
    "high_school_chemistry":
    ["High School Chemistry", "\u9ad8\u4e2d\u5316\u5b66", "STEM"],
    "high_school_biology": [
        "High School Biology", "\u9ad8\u4e2d\u751f\u7269", "STEM"
    ],
    "middle_school_mathematics": [
        "Middle School Mathematics", "\u521d\u4e2d\u6570\u5b66", "STEM"
    ],
    "middle_school_biology": [
        "Middle School Biology", "\u521d\u4e2d\u751f\u7269", "STEM"
    ],
    "middle_school_physics": [
        "Middle School Physics", "\u521d\u4e2d\u7269\u7406", "STEM"
    ],
    "middle_school_chemistry": [
        "Middle School Chemistry", "\u521d\u4e2d\u5316\u5b66", "STEM"
    ],
    "veterinary_medicine": [
        "Veterinary Medicine", "\u517d\u533b\u5b66", "STEM"
    ],
    "college_economics": [
        "College Economics", "\u5927\u5b66\u7ecf\u6d4e\u5b66", "Social Science"
    ],
    "business_administration": [
        "Business Administration", "\u5de5\u5546\u7ba1\u7406", "Social Science"
    ],
    "marxism": [
        "Marxism", "\u9a6c\u514b\u601d\u4e3b\u4e49\u57fa\u672c\u539f\u7406",
        "Social Science"
    ],
    "mao_zedong_thought": [
        "Mao Zedong Thought",
        "\u6bdb\u6cfd\u4e1c\u601d\u60f3\u548c\u4e2d\u56fd\u7279\u8272\u793e\u4f1a\u4e3b\u4e49\u7406\u8bba\u4f53\u7cfb\u6982\u8bba",
        "Social Science"
    ],
    "education_science": [
        "Education Science", "\u6559\u80b2\u5b66", "Social Science"
    ],
    "teacher_qualification": [
        "Teacher Qualification", "\u6559\u5e08\u8d44\u683c", "Social Science"
    ],
    "high_school_politics": [
        "High School Politics", "\u9ad8\u4e2d\u653f\u6cbb", "Social Science"
    ],
    "high_school_geography": [
        "High School Geography", "\u9ad8\u4e2d\u5730\u7406", "Social Science"
    ],
    "middle_school_politics": [
        "Middle School Politics", "\u521d\u4e2d\u653f\u6cbb", "Social Science"
    ],
    "middle_school_geography": [
        "Middle School Geography", "\u521d\u4e2d\u5730\u7406", "Social Science"
    ],
    "modern_chinese_history":
    ["Modern Chinese History", "\u8fd1\u4ee3\u53f2\u7eb2\u8981", "Humanities"],
    "ideological_and_moral_cultivation": [
        "Ideological and Moral Cultivation",
        "\u601d\u60f3\u9053\u5fb7\u4fee\u517b\u4e0e\u6cd5\u5f8b\u57fa\u7840",
        "Humanities"
    ],
    "logic": ["Logic", "\u903b\u8f91\u5b66", "Humanities"],
    "law": ["Law", "\u6cd5\u5b66", "Humanities"],
    "chinese_language_and_literature": [
        "Chinese Language and Literature",
        "\u4e2d\u56fd\u8bed\u8a00\u6587\u5b66", "Humanities"
    ],
    "art_studies": ["Art Studies", "\u827a\u672f\u5b66", "Humanities"],
    "professional_tour_guide": [
        "Professional Tour Guide", "\u5bfc\u6e38\u8d44\u683c", "Humanities"
    ],
    "legal_professional": [
        "Legal Professional", "\u6cd5\u5f8b\u804c\u4e1a\u8d44\u683c",
        "Humanities"
    ],
    "high_school_chinese": [
        "High School Chinese", "\u9ad8\u4e2d\u8bed\u6587", "Humanities"
    ],
    "high_school_history": [
        "High School History", "\u9ad8\u4e2d\u5386\u53f2", "Humanities"
    ],
    "middle_school_history": [
        "Middle School History", "\u521d\u4e2d\u5386\u53f2", "Humanities"
    ],
    "civil_servant": ["Civil Servant", "\u516c\u52a1\u5458", "Other"],
    "sports_science": ["Sports Science", "\u4f53\u80b2\u5b66", "Other"],
    "plant_protection": [
        "Plant Protection", "\u690d\u7269\u4fdd\u62a4", "Other"
    ],
    "basic_medicine": ["Basic Medicine", "\u57fa\u7840\u533b\u5b66", "Other"],
    "clinical_medicine": [
        "Clinical Medicine", "\u4e34\u5e8a\u533b\u5b66", "Other"
    ],
    "urban_and_rural_planner": [
        "Urban and Rural Planner",
        "\u6ce8\u518c\u57ce\u4e61\u89c4\u5212\u5e08", "Other"
    ],
    "accountant": ["Accountant", "\u6ce8\u518c\u4f1a\u8ba1\u5e08", "Other"],
    "fire_engineer": [
        "Fire Engineer", "\u6ce8\u518c\u6d88\u9632\u5de5\u7a0b\u5e08", "Other"
    ],
    "environmental_impact_assessment_engineer": [
        "Environmental Impact Assessment Engineer",
        "\u73af\u5883\u5f71\u54cd\u8bc4\u4ef7\u5de5\u7a0b\u5e08", "Other"
    ],
    "tax_accountant": ["Tax Accountant", "\u7a0e\u52a1\u5e08", "Other"],
    "physician": ["Physician", "\u533b\u5e08\u8d44\u683c", "Other"]
}
ceval_all_sets = list(ceval_subject_mapping.keys())

ceval_datasets = []
for _split in ["val"]:
    for _name in ceval_all_sets:
        _ch_name = ceval_subject_mapping[_name][1]
        ceval_infer_cfg = dict(
            ice_template=dict(
                type=PromptTemplate,
                template={
                    answer: dict(
                        begin="</E>",
                        round=[
                            dict(
                                role="HUMAN",
                                prompt=
                                f"以下是中国关于{_ch_name}考试的单项选择题，请选出其中的正确答案。\n{{question}}\nA. {{A}}\nB. {{B}}\nC. {{C}}\nD. {{D}}\n答案: "
                            ),
                            dict(role="BOT", prompt=answer),
                        ])
                    for answer in ["A", "B", "C", "D"]
                },
                ice_token="</E>",
            ),
            retriever=dict(type=FixKRetriever, fix_id_list=[0, 1, 2, 3, 4]),
            inferencer=dict(type=PPLInferencer),
        )

        ceval_eval_cfg = dict(evaluator=dict(type=AccEvaluator))

        ceval_datasets.append(
            dict(
                type=CEvalDataset,
                path="./data/ceval/formal_ceval",
                name=_name,
                abbr="ceval-" + _name if _split == "val" else "ceval-test-" +
                _name,
                reader_cfg=dict(
                    input_columns=["question", "A", "B", "C", "D"],
                    output_column="answer",
                    train_split="dev",
                    test_split=_split),
                infer_cfg=ceval_infer_cfg,
                eval_cfg=ceval_eval_cfg,
            ))

del _split, _name, _ch_name
