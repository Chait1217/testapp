"""
Contains all the questions and the list of all the male table tennis players.
"""


def start_question():
    """Contains a list of the initial questions for the men table tennis players."""
    START_QUESTIONS = ["Is your player European?", "Is your player Asian?", "Is your player African?",
                       "Does your player come from North or South America?"]
    return START_QUESTIONS


def male_players_question():
    """Contains a list of all the questions for men players by continent.

    The first set of questions are for male European table tennis players,
    the second for male Asian table tennis players,
    the third for male African
    and the last set of questions are for male American players.
    """
    PLAYERS_QUESTIONS = [["Does your player play with pimples?",
                          "Is your player left handed?",
                          "Is your player older than 30 years old?",
                          "Did your player participate in 2016 Olympics in singles or team event?",
                          "Did your player participate in 2021 Olympics in singles or team event?",
                          "Has your player ever won an olympic medal in singles or in team event?",
                          "Is your player sponsored by butterfly?",
                          "Does your player serves with the backhand?",
                          "Does your player serves the forehand reverse pendulum serve?",
                          "Does your player serves the forehand hook serve?",
                          "Is your player Swedish?",
                          "Is your player German?",
                          "Is your player from England?",
                          "Is your player Austrian?",
                          "Is your player Croatian?"],
                         ["Is your player left handed?",
                          "Does your player play with the pen hold grip?",
                          "Is your player older than 30 years old?",
                          "Has your player ever won an olympic medal in singles or in team event?",
                          "Did your player participate in 2016 Olympics in singles or team event?",
                          "Did your player participate in 2021 Olympics in singles or team event?",
                          "Is your player sponsored by butterfly?",
                          "Is your player Chinese?",
                          "Is your player Korean?",
                          "Is your player Indian?",
                          "Does your player serves the forehand reverse pendulum serve?",
                          "Does your player serves the forehand hook serve?"],
                         ["Is your player older than 30 years old?",
                          "Did your player participate in 2016 Olympics in singles or team event?",
                          "Did your player participate in 2021 Olympics in singles or team event?",
                          "Is your player sponsored by gewo?",
                          "Is he known for his extremely powerful forehand?",
                          "Did he reach the quarter finals in 2021 olympics in singles?",
                          "Is your player older than 40 years old?",
                          "Did he use to represent france when he was under 18?",
                          "Is your player the 2nd best player of nigeria?",
                          "Is your player sponsored by butterfly?"],
                         ["Is your player left handed?",
                          "Is your player older than 30 years old?",
                          "Did your player participate in 2016 Olympics in singles or team event?",
                          "Did your player participate in 2021 Olympics in singles or team event?",
                          "Is your player sponsored by butterfly?",
                          "Is your player Argentinian?",
                          "Is your player ranked in the top 30 of the world?",
                          "Is your player known for his shots with two hands?"]]
    return PLAYERS_QUESTIONS


def male_players_list():
    """Contains a list of all the male table tennis players in the world separated by continent.

    The first set of male players come from Europe, the second from Asia,
    the third from Africa and the last set of male players come from the Americas.
    """
    PLAYERS_LIST = [['FALCK Mattias', 'BOLL Timo', 'OVTCHAROV Dimitrij', 'PITCHFORD Liam', 'FRANZISKA Patrick',
                     'GAUZY Simon', 'GARDOS Robert', 'FREITAS Marcos', 'SAMSONOV Vladimir', 'KARLSSON Kristian',
                     'GROTH Jonathan', 'JORGIC Darko', 'PUCAR Tomislav', 'WANG Yang', 'DUDA Benedikt',
                     'LEBESSON Emmanuel',
                     'FILUS Ruwen', 'PERSSON Jon', 'HABESOHN Daniel', 'GACINA Andrej', 'GIONIS Panagiotis',
                     'SIRUCEK Pavel', 'QIU Dang', 'KOU Lei', 'SKACHKOV Kirill', 'APOLONIA Tiago',
                     'DRINKHALL Paul', 'KALLBERG Anton', 'IONESCU Ovidiu', 'MAJOROS Bence',
                     'ROBLES Alvaro', 'DYJAS Jakub', 'TOKIC Bojan', 'PISTEJ Lubomir', 'NUYTINCK Cedric',
                     'AKKUZU Can', 'MONTEIRO Joao', 'LIND Anders', 'BADOWSKI Marek', 'SHIBAEV Alexander',
                     'PLETEA Cristian', 'OLAH Benedek', 'FEGERL Stefan', 'WALTHER Ricardo',
                     'KOJIC Frane', 'JANCARIK Lubomir', 'GERALDO Joao', 'WALKER Samuel'],
                    ['FAN Zhendong', 'XU Xin', 'MA Long', 'LIN Gaoyuan', 'HARIMOTO Tomokazu', 'LIN Yun-Ju',
                     'LIANG Jingkun', 'JANG Woojin', 'JEOUNG Youngsik', 'WANG Chuqin', 'NIWA Koki', 'MIZUTANI Jun',
                     'WONG Chun Ting', 'LEE Sangsu', 'ZHAO Zihao', 'CHUANG Chih-Yuan', 'ACHANTA Sharath Kamal',
                     'UDA Yukiya', 'GNANASEKARAN Sathiyan', 'AN Jaehyun', 'JIN Takuya', 'GERASSIMENKO Kirill',
                     'MORIZONO Masataka', 'YOSHIMURA Kazuhiro', 'OIKAWA Mizuki', 'YOSHIMURA Maharu', 'CHEN Chien-An',
                     'LIM Jonghoon', 'ALAMIYAN Noshad', 'DESAI Harmeet', 'CHO Seungmin', 'LAM Siu Hang', 'HIRANO Yuki',
                     'ANTHONY Amalraj', 'XU Chenhao'],
                    ['ARUNA Quadri', 'ASSAR Omar', 'SALEH Ahmed', 'DIAW Ibrahima', 'OMOTAYO Olajide'],
                    ['CALDERANO Hugo', 'JHA Kanak', 'TSUBOI Gustavo', 'ISHIY Vitor', 'AGUIRRE Marcelo',
                     'CIFUENTES Horacio',
                     'MADRID Marcos', 'MINO Alberto', 'MONTEIRO Thiago', 'JOUTI Eric', 'AFANADOR Brian',
                     'ALTO Gaston']]
    return PLAYERS_LIST
