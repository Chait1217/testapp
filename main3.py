import json


def create_json_europe(filename, Questions, Countries):
    # left handed?
    Q_1 = ["no", "yes", "no", "no", "no", "no", "no", "yes", "no", "yes", "yes", "no", "no", "no", "yes", "yes",
           "no", "no", "no", "no", "no", "no", "no", "no", "no", "yes", "no", "no", "no", "no", "no", "no", "no",
           "no", "yes", "no", "yes", "yes", "no", "no", "no", "no", "no", "no", "no", "no", "yes", "no"]
    # older than 30
    Q_2 = ["no", "yes", "yes", "no", "no", "no", "yes", "yes", "yes", "no", "no", "no", "no", "no", "no", "yes", "yes",
           "yes",
           "yes", "yes", "yes", "no", "no", "yes", "yes", "yes", "yes", "no", "yes", "no", "no", "no", "yes", "yes",
           "no",
           "no", "yes", "no", "no", "yes", "no", "yes", "yes", "no", "no", "yes", "no", "no"]

    # participated in rio 2016 singles or team event?
    Q_3 = ["yes", "yes", "yes", "yes", "no", "yes", "yes", "yes", "yes", "yes", "yes", "no", "no", "yes", "no", "yes",
           "no", "no", "yes", "yes", "yes", "no", "no", "yes", "no", "yes", "yes", "no", "yes", "no", "no", "yes",
           "yes", "no", "no", "no", "yes", "no", "no", "yes", "no", "yes", "yes", "no", "no", "no", "no", "yes"]

    # participated in tokyo 2021 singles or team event?
    Q_4 = ["yes", "yes", "yes", "yes", "yes", "yes", "yes", "yes", "no", "yes", "yes", "yes", "yes", "yes",
           "no", "yes", "no", "no", "yes", "yes", "yes", "no", "no", "yes", "yes", "yes", "yes", "yes", "yes",
           "yes", "yes", "no", "yes", "no", "no", "no", "yes", "no", "no", "no", "no", "no", "no", "no",
           "yes", "yes", "no", "no"]

    dict_json = {}
    for k in range(0, len(Countries)):
        dict_question = {}
        for j in range(0, len(Questions)):
            dict_question[Questions[j]] = locals()[f"Q_{j + 1}"][k]
        dict_json[Countries[k]] = dict_question

    json_file = json.dumps(dict_json, indent=4)
    with open(filename, "w", encoding='utf-8') as f:
        return f.write(json_file)


def create_json_asia(filename, Questions, Countries):
    # left handed
    Q_1 = ["no", "yes", "no", "yes", "no", "yes", "no", "no", "no", "yes", "yes", "no", "no", "no", "no", "no", "no",
           "yes", "no", "no", "no", "no", "yes", "no", "no", "no", "yes", "yes", "yes", "no", "yes", "no", "no", "no",
           "no"]
    # pen holder
    Q_2 = ["no", "yes", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "yes", "no", "yes", "no", "no",
           "no",
           "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no"]
    # older than 30 years old
    Q_3 = ["no", "yes", "yes", "no", "no", "no", "no", "no", "no", "no", "no", "yes", "no", "yes", "no", "yes", "yes",
           "no", "no", "no", "no", "no", "no", "no", "no", "no", "yes", "no", "no", "no", "no", "no", "no", "yes", "no"]
    # participated in rio 2016 singles or team event?
    Q_4 = ["no", "yes", "yes", "no", "no", "no", "no", "no", "yes", "no", "yes", "yes", "yes", "yes", "no", "yes",
           "yes", "no", "no", "no", "no", "yes", "no", "no", "no", "yes", "yes", "no", "yes", "no", "no", "no", "no",
           "no", "no"]
    # ever won an olympic medal in singles or in team event?
    Q_5 = ["yes", "yes", "yes", "no", "yes", "no", "no", "no", "no", "no", "yes", "yes", "no", "no", "no", "no",
           "no", "no", "no",
           "no", "no", "no", "no", "no", "no", "yes", "no", "no", "no", "no", "no", "no", "no", "no", "no"]
    # is he chinese?
    Q_6 = ["yes", "yes", "yes", "yes", "no", "no", "yes", "no", "no", "yes", "no", "no", "no", "no", "yes", "no", "no",
           "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "yes"]
    # particpated in olympics 2021 tokyo singles or team event?
    Q_7 = ["yes", "yes", "yes", "no", "yes", "yes", "no", "yes", "yes", "no", "yes", "yes", "yes", "yes", "no", "yes",
           "yes",
           "no", "yes", "no", "no", "yes", "no", "no", "no", "no", "yes", "no", "no", "no", "no", "yes", "no", "no",
           "no"]
    # is he korean?
    Q_8 = ["no", "no", "no", "no", "no", "no", "no", "yes", "yes", "no", "no", "no", "no", "yes", "no", "no", "no",
           "no", "no",
           "yes", "no", "no", "no", "no", "no", "no", "no", "yes", "no", "no", "yes", "no", "no", "no", "no"]

    # sponsored butterfly?
    Q_9 = ["no", "no", "no", "yes", "yes", "yes", "no", "no", "no", "no", "no", "yes", "yes", "yes", "no", "yes", "no",
           "yes", "yes", "no", "no", "yes", "no", "no", "no", "yes", "no", "no", "yes", "no", "no", "no", "no", "no",
           "no"]
    dict_json = {}
    for k in range(0, len(Countries)):
        dict_question = {}
        for j in range(0, len(Questions)):
            dict_question[Questions[j]] = locals()[f"Q_{j + 1}"][k]
        dict_json[Countries[k]] = dict_question

    json_file = json.dumps(dict_json, indent=4)
    with open(filename, "w", encoding='utf-8') as f:
        return f.write(json_file)


def create_json_africa(filename, Questions, Countries):
    # older than 30 years
    Q_1 = ["yes", "no", "yes", "no", "no"]
    # participated in rio 2016 singles or team event?
    Q_2 = ["yes", "yes", "no", "no", "no"]
    # particpated in olympics 2021 tokyo singles or team event?
    Q_3 = ["yes", "yes", "no", "yes", "no"]
    # know for his extremely powerful forehand?
    Q_4 = ["yes", "no", "no", "no", "no", ]
    # reached quarter final in 2021 olympics?
    Q_5 = ["no", "yes", "no", "no", "no"]
    # older than 40 years old?
    Q_6 = ["no", "no", "yes", "no", "no", ]
    # used to represent france when he was under 18?
    Q_7 = ["no", "no", "no", "yes", "no"]
    # 2nd best player of nigeria?
    Q_8 = ["no", "no", "no", "no", "yes"]
    # sponsored butterfly?
    Q_9 = ["no", "yes", "no", "no", "no"]
    # sponsor gewo
    Q_10 = ["yes", "no", "no", "no", "yes"]
    dict_json = {}
    for k in range(0, len(Countries)):
        dict_question = {}
        for j in range(0, len(Questions)):
            dict_question[Questions[j]] = locals()[f"Q_{j + 1}"][k]
        dict_json[Countries[k]] = dict_question

    json_file = json.dumps(dict_json, indent=4)
    with open(filename, "w", encoding='utf-8') as f:
        return f.write(json_file)


def create_json_north(filename, Questions, Countries):
    # left handed
    Q_1 = ["no", "no", "yes", "no", "yes", "no", "no", "no", "no", "no", "no", "no"]

    # older than 30 years old
    Q_2 = ["no", "no", "yes", "no", "no", "no", "yes", "yes", "yes", "no", "no", "yes"]

    # participated in rio 2016 singles or team event?
    Q_3 = ["yes", "yes", "yes", "no", "yes", "no", "yes", "no", "no", "no", "yes", "no"]

    # particpated in olympics 2021 tokyo singles or team event?
    Q_4 = ["yes", "yes", "yes", "yes", "no", "yes", "no", "yes", "no", "no", "yes", "yes"]

    # is he argentinian?
    Q_5 = ["no", "no", "no", "no", "no", "yes", "no", "no", "no", "no", "no", "yes"]

    # ranked in the top 30 of the world?
    Q_6 = ["yes", "yes", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", ]

    # known for his shots with two hands on the racket?
    Q_7 = ["yes", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", ]
    dict_json = {}
    for k in range(0, len(Countries)):
        dict_question = {}
        for j in range(0, len(Questions)):
            dict_question[Questions[j]] = locals()[f"Q_{j + 1}"][k]
        dict_json[Countries[k]] = dict_question

    json_file = json.dumps(dict_json, indent=4)
    with open(filename, "w", encoding='utf-8') as f:
        return f.write(json_file)