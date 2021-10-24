import json


def create_json_europe(filename, Questions, Countries):
    Europe = ("POLCANOVA Sofia","SOLJA Petrissa","HAN Ying","SZOCS Bernadette","EERLAND Britt","PESOTSKA Margaryta",
          "LI Qian","SAMARA Elizabeta","MITTELHAM Nina","NI Xia Lian","SHAN ^ Xiaona","YANG ^ Xiaoxin",
          "MIKHAILOVA Polina","EKHOLM Matilda","MATELOVA Hana","POTA Georgina","BALAZOVA Barbora","YU ^ Fu","LI Jie",
          "NOSKOVA Yana","SHAO ^ Jieni","MADARASZ Dora","GAPONOVA Ganna","VIVARELLI Debora",
          "XIAO Maria","PERGEL Szandra","DE NUTTE Sarah","DVORAK Galia","SOLJA Amelie","PARTYKA Natalia",
          "BERGSTROM Linda","GASNIER Laura","MORET Rachel","LOEUILLETTE Stephanie","BAJOR Natalia",
          "HO Tin-Tin","LUPULESKU Izabela","CIOBANU Irina")

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
    Asia = ("CHEN Meng","SUN Yingsha","ITO Mima","WANG Manyu","DING Ning","ZHU Yuling",
        "LIU Shiwen","CHENG I-Ching","ISHIKAWA Kasumi","WANG Yidi","HIRANO Miu","FENG Tianwei","CHEN Xingtong",
        "DOO Hoi Kem","JEON Jihee","SATO Hitomi","HE Zhuojia","SUH Hyowon","KATO Miyu","QIAN Tianyi","CHEN Szu-Yu",
        "SOO Wai Yam Minnie","HAYATA Hina","HASHIMOTO Honoka","SHIBATA Saki","GU Yuting","SAWETTABUT Suthasini",
        "LEE Ho Ching","KIHARA Miyuu","YU Mengyu","KIM Song I","NAGASAKI Miyu","CHENG Hsien-Tzu",
        "LIN Ye","ZHANG Rui","BATRA Manika","CHOI Hyojoo","MORI Sakura","LIU Fei","CHA Hyo Sim",
        "ZENG ^^ Jian","YANG Haeun","ANDO Minami","SUN Mingyang","LIU Hsing-Yin","PARANANG Orawan",
        "OJIO Haruna","ZHU Chengzhu","SHIOMI Maki","SHIN Yubin","MUKHERJEE Sutirtha","KIM Nam Hae",
        "LIU Weishan")

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
    Africa = ("MESHREF Dina","HELMY Yousra")

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
    Americas = ("DIAZ Adriana","ZHANG Lily","WU Yue","ZHANG Mo","TAKAHASHI Bruna","DIAZ Melanie","VEGA Paulina")

    dict_json = {}
    for k in range(0, len(Countries)):
        dict_question = {}
        for j in range(0, len(Questions)):
            dict_question[Questions[j]] = locals()[f"Q_{j + 1}"][k]
        dict_json[Countries[k]] = dict_question

    json_file = json.dumps(dict_json, indent=4)
    with open(filename, "w", encoding='utf-8') as f:
        return f.write(json_file)