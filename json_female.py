import json


def create_json_europe(filename, Questions, Countries):

    EUROPE = ("POLCANOVA Sofia", "SOLJA Petrissa", "HAN Ying", "SZOCS Bernadette", "EERLAND Britt", "PESOTSKA Margaryta",
    "LI Qian", "SAMARA Elizabeta", "MITTELHAM Nina", "NI Xia Lian", "SHAN Xiaona", "YANG Xiaoxin",
    "MIKHAILOVA Polina", "EKHOLM Matilda", "MATELOVA Hana", "POTA Georgina", "BALAZOVA Barbora", "YU Fu", "LI Jie",
    "NOSKOVA Yana", "SHAO Jieni", "MADARASZ Dora", "GAPONOVA Ganna", "VIVARELLI Debora",
    "XIAO Maria", "PERGEL Szandra", "DE NUTTE Sarah", "DVORAK Galia", "SOLJA Amelie", "PARTYKA Natalia",
    "BERGSTROM Linda", "GASNIER Laura", "MORET Rachel", "LOEUILLETTE Stephanie", "BAJOR Natalia",
    "HO Tin-Tin", "LUPULESKU Izabela", "CIOBANU Irina")

    # left handed?
    Q_1 = ["yes","yes","no","no","no","no","no","yes","no","yes","no","no","no","yes","no","no","yes","no",
           "no","no","yes","no","no","no","yes","yes","no","no","no","yes","no","yes","yes","yes","no","no",
           "no","no"]
    # older than 30
    Q_2 = ["no","no","yes","no","no","yes","yes","yes","no","yes","yes","yes","yes","yes","yes","yes","no","yes",
           "yes","no","no","no","yes","no","no","yes","no","yes","yes","yes","no","no","yes","no","no","no",
           "no","no"]
    # older than 25
    Q_3 = ["yes","yes","yes","yes","yes","yes","yes","yes","no","yes","yes","yes","yes","yes","yes","yes","yes","yes",
           "yes","yes","yes","yes","yes","yes","yes","yes","yes","yes","yes","yes","yes","yes","yes","yes","no","no",
           "no","yes"]
    # Playing style Defense
    Q_4 = ["no","no","yes","no","no","no","yes","no","no","yes","no","no","yes","no","no","no","no","no",
           "yes","no","no","no","yes","no","no","no","no","no","no","no","yes","no","no","no","no","no",
           "no","no"]
    # participated in rio 2016 singles or team event?
    Q_6 = ["yes","yes","yes","yes","yes","no","yes","yes","no","yes","yes","no","yes","yes","yes","yes","yes","yes",
           "yes","no","yes","no","no","no","no","no","no","yes","no","yes","no","no","no","no","no","no",
           "no","no"]
    # participated in tokyo 2021 singles or team event?
    Q_7 = ["yes","yes","yes","yes","yes","yes","yes","yes","no","yes","yes","yes","yes","no","yes","yes","yes","yes",
           "no","yes","yes","yes","yes","yes","yes","yes","yes","yes","no","yes","yes","no","yes","yes","yes","yes",
           "no","no"]
    # ever won an olympic medal in singles or in team event?
    Q_8 = ["no","yes","yes","no","no","no","no","no","no","no","yes","no","no","no","no","no","no","no","no","no",
           "no","no","no","no","no","no","no","no","no","no","no","no","no","no","no","no","no","no"]

    # pimples?
    # sponsered butterfly
    # backhand serve
    # forehand hook serve?

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
    ASIA = ("CHEN Meng", "SUN Yingsha", "ITO Mima", "WANG Manyu", "DING Ning", "ZHU Yuling",
            "LIU Shiwen", "CHENG I-Ching", "ISHIKAWA Kasumi", "WANG Yidi", "HIRANO Miu", "FENG Tianwei","CHEN Xingtong",
            "DOO Hoi Kem", "JEON Jihee", "SATO Hitomi", "HE Zhuojia", "SUH Hyowon", "KATO Miyu", "QIAN Tianyi",
            "CHEN Szu-Yu","SOO Wai Yam Minnie", "HAYATA Hina", "HASHIMOTO Honoka", "SHIBATA Saki", "GU Yuting",
            "SAWETTABUT Suthasini","LEE Ho Ching", "KIHARA Miyuu", "YU Mengyu", "KIM Song I", "NAGASAKI Miyu",
            "CHENG Hsien-Tzu","LIN Ye", "ZHANG Rui", "BATRA Manika", "CHOI Hyojoo", "MORI Sakura", "LIU Fei",
            "CHA Hyo Sim","ZENG Jian", "YANG Haeun", "ANDO Minami", "SUN Mingyang", "LIU Hsing-Yin",
            "PARANANG Orawan","OJIO Haruna", "ZHU Chengzhu", "SHIOMI Maki", "SHIN Yubin", "MUKHERJEE Sutirtha",
            "KIM Nam Hae","LIU Weishan")

    # left handed?
    Q_1 = ["no","no","no","no","yes","no","no","no","yes","no","no","no","no","no","yes","no","no","no","no","yes",
           "no","no","yes","no","no","yes","no","no","no","no","no","yes","no","no","no","no","yes","no","no","yes",
           "no","no","no","no","no","yes","no","no","no","no","no","no","no"]

    # older than 30
    Q_2 = ["no","no","no","no","yes","no","yes","no","no","no","no","yes","no","no","no","no","no","yes","no",
           "no","no","no","no","no","no","no","no","no","no","yes","no","no","no","no","no","no","no","no",
           "no","no","no","no","no","no","yes","no","no","no","no","no","no","yes","no"]
    # older than 25
    Q_3 = ["yes","no","no","no","yes","yes","yes","yes","yes","no","no","yes","no","no","yes","no","no","yes","no",
           "no","yes","no","no","no","no","yes","yes","no","no","yes","yes","no","yes","yes","no","yes","no","yes",
           "yes","yes","no","yes","no","no","yes","no","no","no","no","no","yes","yes","no"]
    # Playing style Defense
    Q_4 = ["no","no","no","no","no","no","no","no","no","no","no","no","no","no","no","yes","no","yes","no",
           "no","no","no","no","yes","no","no","no","no","no","no","yes","no","no","no","no","no","no","no",
           "yes","no","no","no","no","no","no","no","yes","no","no","no","no","no","no"]
    # pimples?
    # participated in rio 2016 singles or team event?
    # participated in tokyo 2021 singles or team event?
    # ever won an olympic medal in singles or in team event?
    # sponsored butterfly
    # nationalities
    # backhand serve
    # forehand hook serve?

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
    AFRICA = ("MESHREF Dina", "HELMY Yousra")

    # left handed?
    Q_1 = ["yes", "no"]
    # participated in rio 2016 singles or team event?
    Q_2 = ["yes", "no"]

    dict_json = {}
    for k in range(0, len(Countries)):
        dict_question = {}
        for j in range(0, len(Questions)):
            dict_question[Questions[j]] = locals()[f"Q_{j + 1}"][k]
        dict_json[Countries[k]] = dict_question

    json_file = json.dumps(dict_json, indent=4)
    with open(filename, "w", encoding='utf-8') as f:
        return f.write(json_file)


def create_json_americas(filename, Questions, Countries):

    AMERICAS = ("DIAZ Adriana", "ZHANG Lily", "WU Yue", "ZHANG Mo", "TAKAHASHI Bruna", "DIAZ Melanie", "VEGA Paulina")

    Q_1 = ["no", "no", "no", "no", "no", "no", "yes"]  # left handed?

    Q_2 = ["no", "no", "yes", "yes", "no", "no", "yes"]  # older than 30

    Q_3 = ["yes", "yes", "yes", "yes", "yes", "no", "no"]  # participated in rio 2016 singles or team event?

    Q_4 = ["yes", "yes", "no", "yes", "yes", "yes", "yes"]  # participated in tokyo 2021 singles or team event?

    Q_5 = ["yes", "no", "no", "yes", "no", "no", "no"]  # sponsored butterfly

    Q_6 = ["yes", "no", "no", "no", "no", "yes", "yes"]  # forehand hook serve?

    Q_7 = ["no", "no", "no", "no", "no", "yes", "no"]  # backhand serve

    Q_8 = ["yes","no","no","no","no","yes","no"]  # come from puerto Rico

    Q_9 = ["no","yes","yes","no","no","no","no"]  # come from USA

    Q_10 = ["no","no","no","no","yes","no","no"]  # come from Brazil

    dict_json = {}
    for k in range(0, len(Countries)):
        dict_question = {}
        for j in range(0, len(Questions)):
            dict_question[Questions[j]] = locals()[f"Q_{j + 1}"][k]
        dict_json[Countries[k]] = dict_question

    json_file = json.dumps(dict_json, indent=4)
    with open(filename, "w", encoding='utf-8') as f:
        return f.write(json_file)
