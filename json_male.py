import json


def create_json_europe(filename, Questions, Countries):
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

    # left handed?
    Q_2 = ["no", "yes", "no", "no", "no", "no", "no", "yes", "no", "yes", "yes", "no", "no", "no", "yes", "yes",
           "no", "no", "no", "no", "no", "no", "no", "no", "no", "yes", "no", "no", "no", "no", "yes", "no", "no",
           "no", "yes", "no", "yes", "yes", "no", "no", "no", "no", "no", "no", "no", "no", "yes", "no"]
    # older than 30
    Q_3 = ["no", "yes", "yes", "no", "no", "no", "yes", "yes", "yes", "yes", "no", "no", "no", "no", "no", "yes", "yes",
           "yes",
           "yes", "yes", "yes", "no", "no", "yes", "yes", "yes", "yes", "no", "yes", "no", "yes", "no", "yes", "yes",
           "no",
           "no", "yes", "no", "no", "yes", "no", "yes", "yes", "no", "no", "yes", "no", "no"]

    # participated in rio 2016 singles or team event?
    Q_4 = ["yes", "yes", "yes", "yes", "no", "yes", "yes", "yes", "yes", "yes", "yes", "no", "no", "yes", "no", "yes",
           "no", "no", "yes", "yes", "yes", "no", "no", "yes", "no", "yes", "yes", "no", "yes", "no", "no", "yes",
           "yes", "no", "no", "no", "yes", "no", "no", "yes", "no", "yes", "yes", "no", "no", "no", "no", "yes"]

    # participated in tokyo 2021 singles or team event?
    Q_5 = ["yes", "yes", "yes", "yes", "yes", "yes", "yes", "yes", "no", "yes", "yes", "yes", "yes", "yes",
           "no", "yes", "no", "no", "yes", "yes", "yes", "no", "no", "yes", "yes", "yes", "yes", "yes", "yes",
           "yes", "yes", "no", "yes", "no", "no", "no", "yes", "no", "no", "no", "no", "no", "no", "no",
           "yes", "yes", "no", "no"]

    # sponsered butterfly
    Q_7 = ["no", "yes", "yes", "no", "yes", "no", "yes", "yes", "no", "yes", "yes", "no", "no", "no", "no", "no",
           "yes", "no", "no", "yes", "yes", "no", "yes", "no", "no", "yes", "no", "yes", "no", "no", "no", "no",
           "no", "no", "no", "no", "yes", "no", "no", "yes", "no", "no", "yes", "yes", "no", "no", "yes", "no"]

    # ever won an olympic medal in singles or in team event?
    Q_6 = ["no", "yes", "yes", "no", "yes", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no",
           "no", "no",
           "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no",
           "no",
           "no", "no", "no", "no", "no", "no", "no", "no", "no", "no"]
    # backhand serve
    Q_8 = ["yes", "no", "yes", "no", "no", "no", "no", "no", "no", "no", "no", "yes", "no", "yes", "no", "no", "yes",
           "no", "no",
           "no", "no", "yes", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "yes", "yes", "no", "no",
           "no", "no",
           "no", "yes", "no", "no", "no", "no", "yes", "no", "no", "no"]
    # forehand Reverse pendulum serve
    Q_9 = ["yes", "yes", "no", "yes", "yes", "no", "no", "yes", "no", "no", "no", "no", "yes", "no", "yes", "no", "no",
           "yes", "no",
           "yes", "no", "yes", "no", "yes", "yes", "no", "no", "no", "no", "yes", "yes", "yes", "no", "yes", "yes",
           "no", "no",
           "no", "yes", "no", "yes", "yes", "yes", "no", "no", "no", "yes", "no"]
    # forehand hook serve?
    Q_10 = ["no", "no", "no", "yes", "no", "no", "no", "no", "no", "no", "no", "no", "no", "yes", "no", "yes", "no",
            "no", "no",
            "no", "yes", "no", "no", "no", "no", "yes", "no", "yes", "yes", "no", "no", "no", "no", "no", "no", "no",
            "no", "no",
            "no", "no", "yes", "yes", "no", "yes", "yes", "no", "no", "no"]
    # pimples? #1
    Q_1 = ["yes", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "yes", "no", "no", "yes",
           "no", "no",
           "no", "yes", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no",
           "no", "no",
           "no", "no", "no", "no", "no", "no", "no", "no", "no"]
    # swedish?
    Q_11 = ["yes", "no", "no", "no", "no", "no", "no", "no", "no", "yes", "no", "no", "no", "no", "no", "no", "no",
            "yes",
            "no", "no", "no", "no", "no", "no", "no", "no", "no", "yes", "no", "no", "no", "no", "no", "no", "no", "no",
            "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no"]
    # german?
    Q_12 = ["no", "yes", "yes", "no", "yes", "no", "no", "no", "no", "no", "no", "no", "no", "no", "yes", "no", "yes",
            "no",
            "no", "no", "no", "no", "yes", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no",
            "no", "no", "no", "no", "no", "no", "no", "no", "yes", "no", "no", "no", "no"]
    # england?
    Q_13 = ["no", "no", "no", "yes", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no",
            "no", "no", "no", "no", "no", "no", "no", "no", "yes", "no", "no", "no", "no", "no", "no", "no", "no",
            "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "yes"]
    # austrian?
    Q_14 = ["no", "no", "no", "no", "no", "no", "yes", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no",
            "no", "yes", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no",
            "no", "no", "no", "no", "no", "no", "no", "no", "yes", "no", "no", "no", "no", "no"]
    # croatian?
    Q_15 = ["no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "yes", "no", "no", "no", "no",
            "no", "no", "yes", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no",
            "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "yes", "no", "no", "no", ]

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
    ASIA = ('FAN Zhendong', 'XU Xin', 'MA Long', 'LIN Gaoyuan', 'HARIMOTO Tomokazu', 'LIN Yun-Ju',
            'LIANG Jingkun', 'JANG Woojin', 'JEOUNG Youngsik', 'WANG Chuqin', 'NIWA Koki', 'MIZUTANI Jun',
            'WONG Chun Ting', 'LEE Sangsu', 'ZHAO Zihao', 'CHUANG Chih-Yuan', 'ACHANTA Sharath Kamal',
            'UDA Yukiya', 'GNANASEKARAN Sathiyan', 'AN Jaehyun', 'JIN Takuya', 'GERASSIMENKO Kirill',
            'MORIZONO Masataka',
            'YOSHIMURA Kazuhiro', 'OIKAWA Mizuki',
            'YOSHIMURA Maharu', 'CHEN Chien-An', 'LIM Jonghoon', 'ALAMIYAN Noshad', 'DESAI Harmeet', 'CHO Seungmin',
            'LAM Siu Hang', 'HIRANO Yuki', 'ANTHONY Amalraj', 'XU Chenhao')

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
    Q_5 = ["no", "yes", "yes", "no", "no", "no", "no", "no", "yes", "no", "yes", "yes", "yes", "yes", "no", "yes",
           "yes", "no", "no", "no", "no", "yes", "no", "no", "no", "yes", "yes", "no", "yes", "no", "no", "no", "no",
           "no", "no"]
    # ever won an olympic medal in singles or in team event?
    Q_4 = ["yes", "yes", "yes", "no", "yes", "no", "no", "no", "no", "no", "yes", "yes", "no", "no", "no", "no",
           "no", "no", "no",
           "no", "no", "no", "no", "no", "no", "yes", "no", "no", "no", "no", "no", "no", "no", "no", "no"]
    # is he chinese?
    Q_8 = ["yes", "yes", "yes", "yes", "no", "no", "yes", "no", "no", "yes", "no", "no", "no", "no", "yes", "no", "no",
           "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "yes"]
    # particpated in olympics 2021 tokyo singles or team event?
    Q_6 = ["yes", "yes", "yes", "no", "yes", "yes", "no", "yes", "yes", "no", "yes", "yes", "yes", "yes", "no", "yes",
           "yes",
           "no", "yes", "no", "no", "yes", "no", "no", "no", "no", "yes", "no", "no", "no", "no", "yes", "no", "no",
           "no"]
    # is he korean?
    Q_9 = ["no", "no", "no", "no", "no", "no", "no", "yes", "yes", "no", "no", "no", "no", "yes", "no", "no", "no",
           "no", "no",
           "yes", "no", "no", "no", "no", "no", "no", "no", "yes", "no", "no", "yes", "no", "no", "no", "no"]

    # sponsored butterfly?
    Q_7 = ["no", "no", "no", "yes", "yes", "yes", "no", "no", "no", "no", "no", "yes", "yes", "yes", "no", "yes", "no",
           "yes", "yes", "no", "no", "yes", "no", "no", "no", "yes", "no", "no", "yes", "no", "no", "no", "no", "no",
           "no"]
    # is indian?
    Q_10 = ["no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "yes",
            "no", "yes", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "yes", "no", "no", "no", "yes",
            "no"]
    # rentrant
    Q_11 = ["yes", "no", "no", "yes", "no", "no", "yes", "no", "no", "no", "no", "yes", "no", "no", "no", "no", "no",
            "no", "yes",
            "no", "no", "no", "no", "no", "yes", "yes", "no", "no", "yes", "yes", "no", "no", "yes", "yes", "no"]

    # pioche
    Q_12 = ["no", "yes", "no", "no", "no", "no", "no", "no", "no", "no", "yes", "no", "yes", "no", "no", "no", "no",
            "no",
            "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "yes", "no", "no", "yes"]

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
    AFRICA = ('ARUNA Quadri', 'ASSAR Omar', 'SALEH Ahmed', 'DIAW Ibrahima', 'OMOTAYO Olajide')

    # older than 30 years
    Q_1 = ["yes", "no", "yes", "no", "no"]
    # participated in rio 2016 singles or team event?
    Q_2 = ["yes", "yes", "no", "no", "no"]
    # particpated in olympics 2021 tokyo singles or team event?
    Q_3 = ["yes", "yes", "no", "yes", "no"]
    # know for his extremely powerful forehand?
    Q_5 = ["yes", "no", "no", "no", "no", ]
    # reached quarter final in 2021 olympics?
    Q_6 = ["no", "yes", "no", "no", "no"]
    # older than 40 years old?
    Q_7 = ["no", "no", "yes", "no", "no", ]
    # used to represent france when he was under 18?
    Q_8 = ["no", "no", "no", "yes", "no"]
    # 2nd best player of nigeria?
    Q_9 = ["no", "no", "no", "no", "yes"]
    # sponsored butterfly?
    Q_10 = ["no", "yes", "no", "no", "no"]
    # sponsor gewo
    Q_4 = ["yes", "no", "no", "no", "yes"]
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
    AMERICAS = ('CALDERANO Hugo', 'JHA Kanak', 'TSUBOI Gustavo', 'ISHIY Vitor', 'AGUIRRE Marcelo',
                'CIFUENTES Horacio',
                'MADRID Marcos', 'MINO Alberto', 'MONTEIRO Thiago', 'JOUTI Eric', 'AFANADOR Brian',
                'ALTO Gaston')
    # left handed
    Q_1 = ["no", "no", "yes", "no", "yes", "no", "no", "no", "no", "no", "no", "no"]

    # older than 30 years old
    Q_2 = ["no", "no", "yes", "no", "no", "no", "yes", "yes", "yes", "no", "no", "yes"]

    # participated in rio 2016 singles or team event?
    Q_3 = ["yes", "yes", "yes", "no", "yes", "no", "yes", "no", "no", "no", "yes", "no"]

    # particpated in olympics 2021 tokyo singles or team event?
    Q_4 = ["yes", "yes", "yes", "yes", "no", "yes", "no", "yes", "no", "no", "yes", "yes"]

    # is he argentinian?
    Q_6 = ["no", "no", "no", "no", "no", "yes", "no", "no", "no", "no", "no", "yes"]

    # ranked in the top 30 of the world?
    Q_7 = ["yes", "yes", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", ]

    # known for his shots with two hands on the racket?
    Q_8 = ["yes", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", ]

    # "sponsored butterfly?
    Q_5 = ["no", "yes", "yes", "no", "yes", "no", "no", "yes", "no", "yes", "yes", "no"]

    dict_json = {}
    for k in range(0, len(Countries)):
        dict_question = {}
        for j in range(0, len(Questions)):
            dict_question[Questions[j]] = locals()[f"Q_{j + 1}"][k]
        dict_json[Countries[k]] = dict_question

    json_file = json.dumps(dict_json, indent=4)
    with open(filename, "w", encoding='utf-8') as f:
        return f.write(json_file)
