"""Json files.

Creates a json file with the questions and answers for every male table tennis player.
"""

import json


def create_json_europe(filename, questions, players):
    """
    Creates a json file for the male European table tennis players with all their attributes.

    Q_1, Q_2, etc., are lists containing the answers 'yes' or 'no' for every question
    related to the male European players.

    Each element of the list, either 'yes' or 'no', corresponds to the answer in the order of the EUROPE tuple.

    For example, in Q_1, the corresponding question is: 'Does your player play with pimples?'.
    The first element of the tuple, 'yes', corresponds to 'FALCK Mattias',
    the second element of the tuple, 'no', corresponds to 'BOLL Timo', etc.

    -------------
    filename : .json
        name of json file created.

    questions : list
        list of all the questions for the male European table tennis players.

    players : list
        list of all the male European table tennis players.
    """
    EUROPE = ('FALCK Mattias', 'BOLL Timo', 'OVTCHAROV Dimitrij', 'PITCHFORD Liam', 'FRANZISKA Patrick',
              'GAUZY Simon', 'GARDOS Robert', 'FREITAS Marcos', 'SAMSONOV Vladimir', 'KARLSSON Kristian',
              'GROTH Jonathan', 'JORGIC Darko', 'PUCAR Tomislav', 'WANG Yang', 'DUDA Benedikt', 'LEBESSON Emmanuel',
              'FILUS Ruwen', 'PERSSON Jon', 'HABESOHN Daniel', 'GACINA Andrej', 'GIONIS Panagiotis',
              'SIRUCEK Pavel', 'QIU Dang', 'KOU Lei', 'SKACHKOV Kirill', 'APOLONIA Tiago',
              'DRINKHALL Paul', 'KALLBERG Anton', 'IONESCU Ovidiu', 'MAJOROS Bence',
              'ROBLES Alvaro', 'DYJAS Jakub', 'TOKIC Bojan', 'PISTEJ Lubomir', 'NUYTINCK Cedric',
              'AKKUZU Can', 'MONTEIRO Joao', 'LIND Anders', 'BADOWSKI Marek', 'SHIBAEV Alexander',
              'PLETEA Cristian', 'OLAH Benedek', 'FEGERL Stefan', 'WALTHER Ricardo',
              'KOJIC Frane', 'JANCARIK Lubomir', 'GERALDO Joao', 'WALKER Samuel')

    # "Does your player play with pimples?"
    Q_1 = ("yes", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "yes", "no", "no", "yes",
           "no", "no", "no", "yes", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no",
           "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no")

    # "Is your player left handed?"
    Q_2 = ("no", "yes", "no", "no", "no", "no", "no", "yes", "no", "yes", "yes", "no", "no", "no", "yes", "yes",
           "no", "no", "no", "no", "no", "no", "no", "no", "no", "yes", "no", "no", "no", "no", "yes", "no", "no",
           "no", "yes", "no", "yes", "yes", "no", "no", "no", "no", "no", "no", "no", "no", "yes", "no")

    # "Is your player older than 30 years old?"
    Q_3 = ("no", "yes", "yes", "no", "no", "no", "yes", "yes", "yes", "yes", "no", "no", "no", "no", "no", "yes", "yes",
           "yes", "yes", "yes", "yes", "no", "no", "yes", "yes", "yes", "yes", "no", "yes", "no", "yes", "no", "yes",
           "yes", "no", "no", "yes", "no", "no", "yes", "no", "yes", "yes", "no", "no", "yes", "no", "no")

    # "Did your player participate in 2016 Olympics in singles or team event?"
    Q_4 = ("yes", "yes", "yes", "yes", "no", "yes", "yes", "yes", "yes", "yes", "yes", "no", "no", "yes", "no", "yes",
           "no", "no", "yes", "yes", "yes", "no", "no", "yes", "no", "yes", "yes", "no", "yes", "no", "no", "yes",
           "yes", "no", "no", "no", "yes", "no", "no", "yes", "no", "yes", "yes", "no", "no", "no", "no", "yes")

    # "Did your player participate in 2021 Olympics in singles or team event?"
    Q_5 = ("yes", "yes", "yes", "yes", "yes", "yes", "yes", "yes", "no", "yes", "yes", "yes", "yes", "yes",
           "no", "yes", "no", "no", "yes", "yes", "yes", "no", "no", "yes", "yes", "yes", "yes", "yes", "yes",
           "yes", "yes", "no", "yes", "no", "no", "no", "yes", "no", "no", "no", "no", "no", "no", "no",
           "yes", "yes", "no", "no")

    # "Has your player ever won an olympic medal in singles or in team event?"
    Q_6 = ("no", "yes", "yes", "no", "yes", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no",
           "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no",
           "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no")

    # "Is your player sponsored by butterfly?"
    Q_7 = ("no", "yes", "yes", "no", "yes", "no", "yes", "yes", "no", "yes", "yes", "no", "no", "no", "no", "no",
           "yes", "no", "no", "yes", "yes", "no", "yes", "no", "no", "yes", "no", "yes", "no", "no", "no", "no",
           "no", "no", "no", "no", "yes", "no", "no", "yes", "no", "no", "yes", "yes", "no", "no", "yes", "no")

    # "Does your player serves with the backhand?"
    Q_8 = ("yes", "no", "yes", "no", "no", "no", "no", "no", "no", "no", "no", "yes", "no", "yes", "no", "no", "yes",
           "no", "no", "no", "no", "yes", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "yes",
           "yes", "no", "no", "no", "no", "no", "yes", "no", "no", "no", "no", "yes", "no", "no", "no")

    # "Does your player serves the forehand reverse pendulum serve?"
    Q_9 = ("yes", "yes", "no", "yes", "yes", "no", "no", "yes", "no", "no", "no", "no", "yes", "no", "yes", "no", "no",
           "yes", "no", "yes", "no", "yes", "no", "yes", "yes", "no", "no", "no", "no", "yes", "yes", "yes", "no",
           "yes", "yes", "no", "no", "no", "yes", "no", "yes", "yes", "yes", "no", "no", "no", "yes", "no")

    # "Does your player serves the forehand hook serve?"
    Q_10 = ("no", "no", "no", "yes", "no", "no", "no", "no", "no", "no", "no", "no", "no", "yes", "no", "yes", "no",
            "no", "no", "no", "yes", "no", "no", "no", "no", "yes", "no", "yes", "yes", "no", "no", "no", "no",
            "no", "no", "no", "no", "no", "no", "no", "yes", "yes", "no", "yes", "yes", "no", "no", "no")

    # "Is your player Swedish?"
    Q_11 = ("yes", "no", "no", "no", "no", "no", "no", "no", "no", "yes", "no", "no", "no", "no", "no", "no", "no",
            "yes", "no", "no", "no", "no", "no", "no", "no", "no", "no", "yes", "no", "no", "no", "no", "no", "no",
            "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no")

    # "Is your player German?"
    Q_12 = ("no", "yes", "yes", "no", "yes", "no", "no", "no", "no", "no", "no", "no", "no", "no", "yes", "no",
            "yes", "no", "no", "no", "no", "no", "yes", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no",
            "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "yes", "no", "no", "no", "no")

    # "Is your player from England?"
    Q_13 = ("no", "no", "no", "yes", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no",
            "no", "no", "no", "no", "no", "no", "no", "no", "yes", "no", "no", "no", "no", "no", "no", "no", "no",
            "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "yes")

    # "Is your player Austrian?"
    Q_14 = ("no", "no", "no", "no", "no", "no", "yes", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no",
            "no", "yes", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no",
            "no", "no", "no", "no", "no", "no", "no", "no", "yes", "no", "no", "no", "no", "no")

    # "Is your player Croatian?"
    Q_15 = ("no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "yes", "no", "no", "no", "no",
            "no", "no", "yes", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no",
            "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "yes", "no", "no", "no")

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
    Creates a json file for the male Asian table tennis players with all their attributes.

    Q_1, Q_2, etc., are lists containing the answers 'yes' or 'no' for every question
    related to the male Asian players.

    Each element of the list, either 'yes' or 'no', corresponds to the answer in the order of the ASIA tuple.

    For example, in Q_1, the corresponding question is: 'Is your player left handed?'.
    The first element of the tuple, 'no', corresponds to 'FAN Zhendong',
    the second element of the tuple, 'yes', corresponds to 'XU Xin', etc.

    -------------
    filename : .json
        name of json file created.

    questions : list
        list of all the questions for the male Asian table tennis players.

    players : list
        list of all the male Asian table tennis players.
    """
    ASIA = ('FAN Zhendong', 'XU Xin', 'MA Long', 'LIN Gaoyuan', 'HARIMOTO Tomokazu', 'LIN Yun-Ju',
            'LIANG Jingkun', 'JANG Woojin', 'JEOUNG Youngsik', 'WANG Chuqin', 'NIWA Koki', 'MIZUTANI Jun',
            'WONG Chun Ting', 'LEE Sangsu', 'ZHAO Zihao', 'CHUANG Chih-Yuan', 'ACHANTA Sharath Kamal',
            'UDA Yukiya', 'GNANASEKARAN Sathiyan', 'AN Jaehyun', 'JIN Takuya', 'GERASSIMENKO Kirill',
            'MORIZONO Masataka','YOSHIMURA Kazuhiro', 'OIKAWA Mizuki',
            'YOSHIMURA Maharu', 'CHEN Chien-An', 'LIM Jonghoon', 'ALAMIYAN Noshad', 'DESAI Harmeet', 'CHO Seungmin',
            'LAM Siu Hang', 'HIRANO Yuki', 'ANTHONY Amalraj', 'XU Chenhao')

    # "Is your player left handed?"
    Q_1 = ("no", "yes", "no", "yes", "no", "yes", "no", "no", "no", "yes", "yes", "no", "no", "no", "no", "no", "no",
           "yes", "no", "no", "no", "no", "yes", "no", "no", "no", "yes", "yes", "yes", "no", "yes", "no", "no", "no",
           "no")

    # "Does your player play with the pen hold grip?"
    Q_2 = ("no", "yes", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "yes", "no", "yes", "no", "no",
           "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no")

    # "Is your player older than 30 years old?"
    Q_3 = ("no", "yes", "yes", "no", "no", "no", "no", "no", "no", "no", "no", "yes", "no", "yes", "no", "yes", "yes",
           "no", "no", "no", "no", "no", "no", "no", "no", "no", "yes", "no", "no", "no", "no", "no", "no", "yes", "no")

    # "Has your player ever won an olympic medal in singles or in team event?"
    Q_4 = ("yes", "yes", "yes", "no", "yes", "no", "no", "no", "no", "no", "yes", "yes", "no", "no", "no", "no",
           "no", "no", "no", "no", "no", "no", "no", "no", "no", "yes", "no", "no", "no", "no", "no", "no",
           "no", "no", "no")

    # "Did your player participate in 2016 Olympics in singles or team event?"
    Q_5 = ("no", "yes", "yes", "no", "no", "no", "no", "no", "yes", "no", "yes", "yes", "yes", "yes", "no", "yes",
           "yes", "no", "no", "no", "no", "yes", "no", "no", "no", "yes", "yes", "no", "yes", "no", "no", "no", "no",
           "no", "no")

    # "Did your player participate in 2021 Olympics in singles or team event?"
    Q_6 = ("yes", "yes", "yes", "no", "yes", "yes", "no", "yes", "yes", "no", "yes", "yes", "yes", "yes", "no", "yes",
           "yes", "no", "yes", "no", "no", "yes", "no", "no", "no", "no", "yes", "no", "no", "no", "no", "yes",
           "no", "no", "no")
    # "Is your player sponsored by butterfly?"
    Q_7 = ("no", "no", "no", "yes", "yes", "yes", "no", "no", "no", "no", "no", "yes", "yes", "yes", "no", "yes", "no",
           "yes", "yes", "no", "no", "yes", "no", "no", "no", "yes", "no", "no", "yes", "no", "no", "no", "no", "no",
           "no")
    # "Is your player Chinese?"
    Q_8 = ("yes", "yes", "yes", "yes", "no", "no", "yes", "no", "no", "yes", "no", "no", "no", "no", "yes", "no", "no",
           "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "yes")

    # "Is your player Korean?"
    Q_9 = ("no", "no", "no", "no", "no", "no", "no", "yes", "yes", "no", "no", "no", "no", "yes", "no", "no", "no",
           "no", "no", "yes", "no", "no", "no", "no", "no", "no", "no", "yes", "no", "no", "yes", "no", "no",
           "no", "no")

    # "Is your player Indian?"
    Q_10 = ("no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "yes",
            "no", "yes", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "yes", "no", "no", "no", "yes",
            "no")

    # "Does your player serves the forehand reverse pendulum serve?"
    Q_11 = ("yes", "no", "no", "yes", "no", "no", "yes", "no", "no", "no", "no", "yes", "no", "no", "no", "no", "no",
            "no", "yes", "no", "no", "no", "no", "no", "yes", "yes", "no", "no", "yes", "yes", "no", "no", "yes",
            "yes", "no")

    # "Does your player serves the forehand hook serve?"
    Q_12 = ("no", "yes", "no", "no", "no", "no", "no", "no", "no", "no", "yes", "no", "yes", "no", "no", "no", "no",
            "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "yes", "no", "no",
            "yes")

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
    Creates a json file for the male African table tennis players with all their attributes.

    Q_1, Q_2, etc., are lists containing the answers 'yes' or 'no' for every question
    related to the male African players.

    Each element of the list, either 'yes' or 'no', corresponds to the answer in the order of the AFRICA tuple.

    For example, in Q_1, the corresponding question is: 'Is your player older than 30 years?'. The first 'yes'
    corresponds to 'ARUNA Quadri', the second element of the tuple, 'no', corresponds to 'ASSAR Omar', etc.

    -------------
    filename : .json
        name of json file created.

    questions : list
        list of all the questions for the male African table tennis players.

    players : list
        list of all the male African table tennis players.
    """
    AFRICA = ('ARUNA Quadri', 'ASSAR Omar', 'SALEH Ahmed', 'DIAW Ibrahima', 'OMOTAYO Olajide')

    # "Is your player older than 30 years old?"
    Q_1 = ("yes", "no", "yes", "no", "no")

    # "Did your player participate in 2016 Olympics in singles or team event?"
    Q_2 = ("yes", "yes", "no", "no", "no")

    # "Did your player participate in 2021 Olympics in singles or team event?"
    Q_3 = ("yes", "yes", "no", "yes", "no")

    # "Is your player sponsored by gewo?"
    Q_4 = ("yes", "no", "no", "no", "yes")

    # "Is he known for his extremely powerful forehand?"
    Q_5 = ("yes", "no", "no", "no", "no",)

    # "Did he reach the quarter finals in 2021 olympics in singles?"
    Q_6 = ("no", "yes", "no", "no", "no")

    # "Is your player older than 40 years old?"
    Q_7 = ("no", "no", "yes", "no", "no",)

    # "Did he use to represent france when he was under 18?"
    Q_8 = ("no", "no", "no", "yes", "no")

    # "Is your player the 2nd best player of nigeria?"
    Q_9 = ("no", "no", "no", "no", "yes")

    # "Is your player sponsored by butterfly?"
    Q_10 = ("no", "yes", "no", "no", "no")

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
    Creates a json file for the male American table tennis players with all their attributes.

    Q_1, Q_2, etc., are lists containing the answers 'yes' or 'no' for every question
    related to the male American players.

    Each element of the list, either 'yes' or 'no', corresponds to the answer in the order of the AMERICAS tuple.

    For example, in Q_1, the corresponding question is: 'Is your player left handed?'. The first 'no'
    corresponds to 'CALDERANO Hugo', the second element of the tuple, 'no', corresponds to 'JHA Kanak', etc.

    -------------
    filename : .json
        name of json file created.

    questions : list
        list of all the questions for the male American table tennis players.

    players : list
        list of all the male American table tennis players.
    """
    AMERICAS = ('CALDERANO Hugo', 'JHA Kanak', 'TSUBOI Gustavo', 'ISHIY Vitor', 'AGUIRRE Marcelo', 'CIFUENTES Horacio',
                'MADRID Marcos', 'MINO Alberto', 'MONTEIRO Thiago', 'JOUTI Eric', 'AFANADOR Brian', 'ALTO Gaston')

    # "Is your player left handed?"
    Q_1 = ("no", "no", "yes", "no", "yes", "no", "no", "no", "no", "no", "no", "no")

    # "Is your player older than 30 years old?"
    Q_2 = ("no", "no", "yes", "no", "no", "no", "yes", "yes", "yes", "no", "no", "yes")

    # "Did your player participate in 2016 Olympics in singles or team event?"
    Q_3 = ("yes", "yes", "yes", "no", "yes", "no", "yes", "no", "no", "no", "yes", "no")

    # "Did your player participate in 2021 Olympics in singles or team event?"
    Q_4 = ("yes", "yes", "yes", "yes", "no", "yes", "no", "yes", "no", "no", "yes", "yes")

    # "Is your player sponsored by butterfly?"
    Q_5 = ("no", "yes", "yes", "no", "yes", "no", "no", "yes", "no", "yes", "yes", "no")

    # "Is your player Argentinian?"
    Q_6 = ("no", "no", "no", "no", "no", "yes", "no", "no", "no", "no", "no", "yes")

    # "Is your player ranked in the top 30 of the world?"
    Q_7 = ("yes", "yes", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no",)

    # "Is your player known for his shots with two hands?"
    Q_8 = ("yes", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no",)

    dict_json = {}
    for k in range(0, len(players)):
        dict_question = {}
        for j in range(0, len(questions)):
            dict_question[questions[j]] = locals()[f"Q_{j + 1}"][k]
        dict_json[players[k]] = dict_question

    json_file = json.dumps(dict_json, indent=4)
    with open(filename, "w", encoding='utf-8') as f:
        return f.write(json_file)

