"""Json files.

Creates a json file with the questions and answers for every female table tennis player.
"""

import json


def create_json_europe(filename, questions, players):
    """
    Creates a json file for the female European table tennis players with all their attributes.

    Q_1, Q_2, etc., are lists containing the answers 'yes' or 'no' for every question
    related to the female European players.

    Each element of the list, either 'yes' or 'no', corresponds to the answer in the order of the EUROPE tuple.

    For example, in Q_1, the corresponding question is: "Is your player left handed?".
    The first element of the tuple, 'yes', corresponds to 'POLCANOVA Sofia',
    the second element of the tuple, 'yes', corresponds to 'SOLJA Petrissa', etc.

    -------------
    filename : .json
        name of json file created.

    questions : list
        list of all the questions for the female European table tennis players.

    players : list
        list of all the female European table tennis players.
    """

    EUROPE = (
        "POLCANOVA Sofia", "SOLJA Petrissa", "HAN Ying", "SZOCS Bernadette", "EERLAND Britt", "PESOTSKA Margaryta",
        "LI Qian", "SAMARA Elizabeta", "MITTELHAM Nina", "NI Xia Lian", "SHAN Xiaona", "YANG Xiaoxin",
        "MIKHAILOVA Polina", "EKHOLM Matilda", "MATELOVA Hana", "POTA Georgina", "BALAZOVA Barbora", "YU Fu", "LI Jie",
        "NOSKOVA Yana", "SHAO Jieni", "MADARASZ Dora", "GAPONOVA Ganna", "VIVARELLI Debora",
        "XIAO Maria", "PERGEL Szandra", "DE NUTTE Sarah", "DVORAK Galia", "SOLJA Amelie", "PARTYKA Natalia",
        "BERGSTROM Linda", "GASNIER Laura", "MORET Rachel", "LOEUILLETTE Stephanie", "BAJOR Natalia",
        "HO Tin-Tin", "LUPULESKU Izabela", "CIOBANU Irina")

    # "Is your player left handed?"
    Q_1 = ("yes", "yes", "no", "no", "no", "no", "no", "yes", "no", "yes", "no", "no", "no", "yes", "no", "no", "yes",
           "no", "no", "no", "yes", "no", "no", "no", "yes", "yes", "no", "no", "no", "yes", "no", "yes", "yes",
           "yes", "no", "no", "no", "no")

    # "Is your player older than 30 years old?"
    Q_2 = ("no", "no", "yes", "no", "no", "yes", "yes", "yes", "no", "yes", "yes", "yes", "yes", "yes", "yes", "yes",
           "no", "yes", "yes", "no", "no", "no", "yes", "no", "no", "yes", "no", "yes", "yes", "yes", "no", "no",
           "yes", "no", "no", "no", "no", "no")

    # "Is your player older than 25 years old?"
    Q_3 = ("yes", "yes", "yes", "yes", "yes", "yes", "yes", "yes", "no", "yes", "yes", "yes", "yes", "yes", "yes",
           "yes", "yes", "yes", "yes", "yes", "yes", "yes", "yes", "yes", "yes", "yes", "yes", "yes", "yes",
           "yes", "yes", "yes", "yes", "yes", "no", "no", "no", "yes")

    # "Is your player have a defender?"
    Q_4 = ("no", "no", "yes", "no", "no", "no", "yes", "no", "no", "yes", "no", "no", "yes", "no", "no", "no", "no",
           "no", "yes", "no", "no", "no", "yes", "no", "no", "no", "no", "no", "no", "no", "yes", "no", "no", "no",
           "no", "no", "no", "no")

    # "Has your player ever won an olympic medal in singles or in team event?
    Q_5 = ("no", "yes", "yes", "no", "no", "no", "no", "no", "no", "no", "yes", "no", "no", "no", "no", "no", "no",
           "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no",
           "no", "no", "no", "no")

    # "Did your player participate in 2016 Olympics in singles or team event?"
    Q_6 = ("yes", "yes", "yes", "yes", "yes", "no", "yes", "yes", "no", "yes", "yes", "no", "yes", "yes", "yes", "yes",
           "yes", "yes", "yes", "no", "yes", "no", "no", "no", "no", "no", "no", "yes", "no", "yes", "no", "no",
           "no", "no", "no", "no", "no", "no")

    # "Did your player participate in 2021 Olympics in singles or team event?"
    Q_7 = ("yes", "yes", "yes", "yes", "yes", "yes", "yes", "yes", "no", "yes", "yes", "yes", "yes", "no", "yes", "yes",
           "yes", "yes", "no", "yes", "yes", "yes", "yes", "yes", "yes", "yes", "yes", "yes", "no", "yes", "yes",
           "no", "yes", "yes", "yes", "yes", "no", "no")

    # "Is your player sponsored by butterfly?"
    Q_8 = ("yes", "no", "no", "no", "yes", "no", "no", "yes", "no", "no", "no", "no", "yes", "no", "yes", "no", "yes",
           "no", "no", "yes", "no", "yes", "no", "no", "no", "no", "no", "no", "no", "yes", "no", "no", "no", "no",
           "no", "no", "no", "no")

    # "Does your player serves the forehand hook serve?"
    Q_9 = ("no", "no", "no", "yes", "no", "no", "no", "no", "no", "no", "no", "yes", "no", "no", "yes", "no", "no",
           "no", "no", "yes", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no",
           "no", "no", "no", "no")

    # "Does your player serves with the backhand?"
    Q_10 = ("no", "no", "yes", "no", "no", "yes", "yes", "no", "no", "no", "no", "no", "no", "no", "no", "yes",
            "no", "no", "yes", "yes", "no", "yes", "yes", "no", "no", "no", "yes", "no", "no", "no", "yes",
            "yes", "no", "no", "yes", "no", "yes", "yes")

    # "Does your player serves the forehand reverse pendulum serve?"
    Q_11 = ("yes", "no", "no", "no", "yes", "no", "no", "no", "no", "no", "no", "no", "no", "yes", "no", "no", "no",
            "no", "no", "no", "no", "no", "no", "yes", "no", "no", "no", "no", "no", "no", "no", "no", "no", "yes",
            "yes", "no", "no", "no")

    # "Is your player Hungarian?"
    Q_12 = ("no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "yes",
            "no", "no", "no", "no", "no", "yes", "no", "no", "no", "yes", "no", "no", "no", "no", "no", "no",
            "no", "no", "no", "no", "no", "no", )

    # "Is your player Polish?"
    Q_13 = ("no", "no", "no", "no", "no", "no", "yes", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no",
            "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "yes", "no", "no", "no",
            "no", "yes", "no", "no", "no")

    dict_json = {}
    for k in range(0, len(players)):
        dict_question = {}
        for j in range(0, len(questions)):
            dict_question[questions[j]] = locals()[f"Q_{j + 1}"][k]
        dict_json[players[k]] = dict_question

    json_file = json.dumps(dict_json, indent=4)
    with open(filename, "w", encoding='utf-8') as f:
        return f.write(json_file)


def create_json_asia(filename, questions, players):
    """
    Creates a json file for the female Asian table tennis players with all their attributes.

    Q_1, Q_2, etc., are lists containing the answers 'yes' or 'no' for every question
    related to the female Asian players.

    Each element of the list, either 'yes' or 'no', corresponds to the answer in the order of the ASIA tuple.

    For example, in Q_1, the corresponding question is: 'Is your player left handed?'. The first 'no'
    corresponds to 'CHEN Meng', the second element of the tuple, 'no', corresponds to 'SUN Yingsha', etc.

    -------------
    filename : .json
        name of json file created.

    questions : list
        list of all the questions for the female Asian table tennis players.

    players : list
        list of all the female Asian table tennis players.
    """

    ASIA = ("CHEN Meng", "SUN Yingsha", "ITO Mima", "WANG Manyu", "DING Ning", "ZHU Yuling",
            "LIU Shiwen", "CHENG I-Ching", "ISHIKAWA Kasumi", "WANG Yidi", "HIRANO Miu", "FENG Tianwei",
            "CHEN Xingtong",
            "DOO Hoi Kem", "JEON Jihee", "SATO Hitomi", "HE Zhuojia", "SUH Hyowon", "KATO Miyu", "QIAN Tianyi",
            "CHEN Szu-Yu", "SOO Wai Yam Minnie", "HAYATA Hina", "HASHIMOTO Honoka", "SHIBATA Saki", "GU Yuting",
            "SAWETTABUT Suthasini", "LEE Ho Ching", "KIHARA Miyuu", "YU Mengyu", "KIM Song I", "NAGASAKI Miyu",
            "CHENG Hsien-Tzu", "LIN Ye", "ZHANG Rui", "BATRA Manika", "CHOI Hyojoo", "MORI Sakura", "LIU Fei",
            "CHA Hyo Sim", "ZENG Jian", "YANG Haeun", "ANDO Minami", "SUN Mingyang", "LIU Hsing-Yin",
            "PARANANG Orawan", "OJIO Haruna", "ZHU Chengzhu", "SHIOMI Maki", "SHIN Yubin", "MUKHERJEE Sutirtha",
            "KIM Nam Hae", "LIU Weishan")

    # "Is your player left handed?"
    Q_1 = ("no", "no", "no", "no", "yes", "no", "no", "no", "yes", "no", "no", "no", "no", "no", "yes", "no", "no",
           "no", "no", "yes", "no", "no", "yes", "no", "no", "yes", "no", "no", "no", "no", "no", "yes", "no",
           "no", "no", "no", "yes", "no", "no", "yes", "no", "no", "no", "no", "no", "yes", "no", "no", "no",
           "no", "no", "no", "no")

    # "Is your player older than 30 years old?"
    Q_2 = ("no", "no", "no", "no", "yes", "no", "yes", "no", "no", "no", "no", "yes", "no", "no", "no", "no", "no",
           "yes", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "yes", "no", "no", "no", "no",
           "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "yes", "no", "no", "no", "no", "no",
           "no", "yes", "no")

    # "Is your player older than 25 years old?"
    Q_3 = ("yes", "no", "no", "no", "yes", "yes", "yes", "yes", "yes", "no", "no", "yes", "no", "no", "yes", "no",
           "no", "yes", "no", "no", "yes", "no", "no", "no", "no", "yes", "yes", "no", "no", "yes", "yes", "no",
           "yes", "yes", "no", "yes", "no", "yes", "yes", "yes", "no", "yes", "no", "no", "yes", "no", "no",
           "no", "no", "no", "yes", "yes", "no")

    # "Is your player a defender?"
    Q_4 = ("no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "yes", "no",
           "yes","no", "no", "no", "no", "no", "yes", "no", "no", "no", "no", "no", "no", "yes", "no", "no", "no",
           "no", "no", "no", "no", "yes", "no", "no", "no", "no", "no", "no", "no", "yes", "no", "no", "no", "no",
           "no", "no")

    # "Has your player ever won an olympic medal in singles or in team event?"
    Q_5 = ("yes", "yes", "yes", "yes", "yes", "no", "yes", "no", "yes", "no", "yes", "yes", "no", "yes", "no", "no",
           "no", "no", "no", "no", "no", "yes", "no", "no", "no", "no", "no", "yes", "no", "no", "no", "no", "no", "no",
           "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no",
           "no")

    # "Did your player participate in 2016 Olympics in singles or team event?"
    Q_6 = ("no", "no", "yes", "no", "yes", "no", "yes", "yes", "yes", "no", "no", "yes", "no", "yes", "yes", "no", "no",
           "yes", "no", "no", "no", "no", "no", "no", "no", "no", "yes", "yes", "no", "yes", "yes", "no", "no", "no",
           "no", "yes", "no", "no", "no", "no", "no", "yes", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no",
           "no")

    # "Did your player participate in 2021 Olympics in singles or team event?"
    Q_7 = ("yes", "yes", "yes", "yes", "no", "no", "no", "yes", "yes", "no", "yes", "yes", "no", "yes", "yes", "no",
           "no", "no", "no", "no", "no", "yes", "no", "no", "no", "no", "yes", "yes", "no", "yes", "no", "no", "yes",
           "yes", "no", "yes", "yes", "no", "no", "no", "no", "no", "no", "no", "no", "yes", "no", "no", "no",
           "yes", "yes", "no", "no")

    # "Does your player serves the forehand hook serve?"
    Q_8 = ("no", "no", "yes", "yes", "no", "no", "yes", "no", "yes", "no", "yes", "no", "yes", "yes", "yes", "no",
           "no", "no", "yes", "no", "no", "no", "yes", "no", "yes", "no", "yes", "no", "yes", "no", "no", "no", "yes",
           "no", "yes", "no", "no", "yes", "no", "no", "yes", "no", "no", "no", "yes", "yes", "no", "no", "yes",
           "yes", "no", "no", "no")

    # "Does your player serves with the backhand?"
    Q_9 = ("no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "yes",
           "no", "yes", "no", "no", "no", "no", "no", "yes", "no", "no", "yes", "no", "no", "no", "yes", "no",
           "no", "no", "no", "yes", "no", "no", "yes", "no", "no", "no", "no", "no", "no", "no", "yes",
           "no", "no", "no", "yes", "no", "no")

    # "Does your player serves the forehand reverse pendulum serve?"
    Q_10 = ("no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no",
            "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "yes", "no",
            "no", "no", "no", "no", "no", "no", "no", "yes", "no", "no", "no", "no", "no", "no", "no",
            "no", "no", "no", "no", "no", "no", "no", "no", "no")

    # "Is your player Chinese?"
    Q_11 = ("yes", "yes", "no", "yes", "yes", "yes", "yes", "no", "no", "yes", "no", "no", "yes", "no",
            "no", "no", "yes", "no", "no", "yes", "no", "no", "no", "no", "no", "yes", "no", "no", "no",
            "no", "no", "no", "no", "no", "yes", "no", "no", "no", "yes", "no", "no", "no", "no", "yes",
            "no", "no", "no", "no", "no", "no", "no", "no", "yes")

    # "Is your player Japanese?"
    Q_12 = ("no", "no", "yes", "no", "no", "no", "no", "no", "yes", "no", "yes", "no", "no", "no", "no", "yes",
            "no", "no", "yes", "no", "no", "no", "yes", "yes", "yes", "no", "no", "no", "yes", "no", "no", "yes",
            "no", "no", "no", "no", "no", "yes", "no", "no", "no", "no", "yes", "no", "no", "no", "yes", "no",
            "yes", "no", "no", "no", "no")

    # south korea

    dict_json = {}
    for k in range(0, len(players)):
        dict_question = {}
        for j in range(0, len(questions)):
            dict_question[questions[j]] = locals()[f"Q_{j + 1}"][k]
        dict_json[players[k]] = dict_question
    json_file = json.dumps(dict_json, indent=4)
    with open(filename, "w", encoding='utf-8') as f:
        return f.write(json_file)


def create_json_africa(filename, questions, players):
    """
    Creates a json file for the female African table tennis players with all their attributes.

    Q_1, Q_2, etc., are lists containing the answers 'yes' or 'no' for every question
    related to the female African players.

    Each element of the list, either 'yes' or 'no', corresponds to the answer in the order of the AFRICA tuple.

    For example, in Q_1, the corresponding question is: 'Is your player left handed?'. The first 'yes'
    corresponds to 'MESHREF Dina', the second element of the tuple, 'no', corresponds to 'HELMY Yousra', etc.

    -------------
    filename : .json
        name of json file created.

    questions : list
        list of all the questions for the female African table tennis players.

    players : list
        list of all the female African table tennis players.
    """
    AFRICA = ("MESHREF Dina", "HELMY Yousra")

    # "Is your player left handed?"
    Q_1 = ("yes", "no")

    # "Did your player participate in 2016 Olympics in singles or team event?"
    Q_2 = ("yes", "no")

    dict_json = {}
    for k in range(0, len(players)):
        dict_question = {}
        for j in range(0, len(questions)):
            dict_question[questions[j]] = locals()[f"Q_{j + 1}"][k]
        dict_json[players[k]] = dict_question

    json_file = json.dumps(dict_json, indent=4)
    with open(filename, "w", encoding='utf-8') as f:
        return f.write(json_file)


def create_json_americas(filename, questions, players):
    """
    Creates a json file for the female American table tennis players with all their attributes.

    Q_1, Q_2, etc., are lists containing the answers 'yes' or 'no' for every question
    related to the female American players.

    Each element of the list, either 'yes' or 'no', corresponds to the answer in the order of the AMERICAS tuple.

    For example, in Q_1, the corresponding question is: 'Is your player left handed?'. The first 'no'
    corresponds to 'DIAZ Adriana', the second element of the tuple, 'no', corresponds to 'ZHANG Lily', etc.

    -------------
    filename : .json
        name of json file created.

    questions : list
        list of all the questions for the female American table tennis players.

    players : list
        list of all the female American table tennis players.
    """
    AMERICAS = ("DIAZ Adriana", "ZHANG Lily", "WU Yue", "ZHANG Mo", "TAKAHASHI Bruna", "DIAZ Melanie", "VEGA Paulina")

    # "Is your player left handed?"
    Q_1 = ("no", "no", "no", "no", "no", "no", "yes")

    # "Is your player older than 30 years old?"
    Q_2 = ("no", "no", "yes", "yes", "no", "no", "yes")

    # "Did your player participate in 2016 Olympics in singles or team event?"
    Q_3 = ("yes", "yes", "yes", "yes", "yes", "no", "no")

    # "Did your player participate in 2021 Olympics in singles or team event?"
    Q_4 = ("yes", "yes", "no", "yes", "yes", "yes", "yes")

    # "Is your player sponsored by butterfly?"
    Q_5 = ("yes", "no", "no", "yes", "no", "no", "no")

    # "Does your player serves the forehand hook serve?"
    Q_6 = ("yes", "no", "no", "no", "no", "yes", "yes")

    # "Does your player serves with the backhand?"
    Q_7 = ("no", "no", "no", "no", "no", "yes", "no")

    # "Is your player from Puerto Rico?"
    Q_8 = ("yes", "no", "no", "no", "no", "yes", "no")

    # "Is your player from the USA?"
    Q_9 = ("no", "yes", "yes", "no", "no", "no", "no")

    # "Is your player from Brazil?"
    Q_10 = ("no", "no", "no", "no", "yes", "no", "no")

    dict_json = {}
    for k in range(0, len(players)):
        dict_question = {}
        for j in range(0, len(questions)):
            dict_question[questions[j]] = locals()[f"Q_{j + 1}"][k]
        dict_json[players[k]] = dict_question

    json_file = json.dumps(dict_json, indent=4)
    with open(filename, "w", encoding='utf-8') as f:
        return f.write(json_file)
