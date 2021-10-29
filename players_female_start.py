"""
Contains all the questions and the list of all the female table tennis players.
"""


def start_question():
    """Contains a list of the initial questions for the women table tennis players."""

    START_QUESTIONS = ["Is your player European?", "Is your player Asian?", "Is your player African?",
                       "Does your player come from North or South America?"]

    return START_QUESTIONS


def female_players_question():
    """Contains a list of all the questions for women players by continent.

    The first set of questions are for female European table tennis players,
    the second for female Asian table tennis players,
    the third for female African
    and the last set of questions are for female American players.
    """
    PLAYERS_QUESTIONS = [["Is your player left handed?", "Is your player older than 30 years old?",
                          "Is your player older than 25 years old?", "Is your player a defender?",
                          "Has your player ever won an olympic medal in singles or in team event?",
                          "Did your player participate in 2016 Olympics in singles or team event?",
                          "Did your player participate in 2021 Olympics in singles or team event?",
                          "Is your player sponsored by butterfly?", "Does your player serves the forehand hook serve?",
                          "Does your player serves with the backhand?",
                          "Does your player serves the forehand reverse pendulum serve?",
                          "Is your player Hungarian?",
                          "Is your player Polish?"],
                         ["Is your player left handed?", "Is your player older than 30 years old?",
                          "Is your player older than 25 years old?", "Is your player a defender?",
                          "Has your player ever won an olympic medal in singles or in team event?",
                          "Did your player participate in 2016 Olympics in singles or team event?",
                          "Did your player participate in 2021 Olympics in singles or team event?",
                          "Does your player serves the forehand hook serve?",
                          "Does your player serves with the backhand?",
                          "Does your player serves the forehand reverse pendulum serve?",
                          "Is your player Chinese?", "Is your player Japanese?"],
                         ["Is your player left handed?",
                          "Did your player participate in 2016 Olympics in singles or team event?"],
                         ["Is your player left handed?", "Is your player older than 30 years old?",
                          "Did your player participate in 2016 Olympics in singles or team event?",
                          "Did your player participate in 2021 Olympics in singles or team event?",
                          "Is your player sponsored by butterfly?",
                          "Does your player serves the forehand hook serve?",
                          "Does your player serves with the backhand?",
                          "Is your player from Puerto Rico?",
                          "Is your player from the USA?",
                          "Is your player from Brazil?"]]
    return PLAYERS_QUESTIONS


def female_players_list():
    """Contains a list of all the female table tennis players in the world separated by continent.

    The first set of female players come from Europe, the second from Asia,
    the third from Africa and the last set of female players come from the Americas.
    """
    PLAYERS_LIST = [
        ["POLCANOVA Sofia", "SOLJA Petrissa", "HAN Ying", "SZOCS Bernadette", "EERLAND Britt", "PESOTSKA Margaryta",
         "LI Qian", "SAMARA Elizabeta", "MITTELHAM Nina", "NI Xia Lian", "SHAN Xiaona", "YANG Xiaoxin",
         "MIKHAILOVA Polina", "EKHOLM Matilda", "MATELOVA Hana", "POTA Georgina", "BALAZOVA Barbora", "YU Fu", "LI Jie",
         "NOSKOVA Yana", "SHAO Jieni", "MADARASZ Dora", "GAPONOVA Ganna", "VIVARELLI Debora",
         "XIAO Maria", "PERGEL Szandra", "DE NUTTE Sarah", "DVORAK Galia", "SOLJA Amelie", "PARTYKA Natalia",
         "BERGSTROM Linda", "GASNIER Laura", "MORET Rachel", "LOEUILLETTE Stephanie", "BAJOR Natalia",
         "HO Tin-Tin", "LUPULESKU Izabela", "CIOBANU Irina"],
        ["CHEN Meng", "SUN Yingsha", "ITO Mima", "WANG Manyu", "DING Ning", "ZHU Yuling",
         "LIU Shiwen", "CHENG I-Ching", "ISHIKAWA Kasumi", "WANG Yidi", "HIRANO Miu", "FENG Tianwei", "CHEN Xingtong",
         "DOO Hoi Kem", "JEON Jihee", "SATO Hitomi", "HE Zhuojia", "SUH Hyowon", "KATO Miyu", "QIAN Tianyi",
         "CHEN Szu-Yu", "SOO Wai Yam Minnie", "HAYATA Hina", "HASHIMOTO Honoka", "SHIBATA Saki", "GU Yuting",
         "SAWETTABUT Suthasini", "LEE Ho Ching", "KIHARA Miyuu", "YU Mengyu", "KIM Song I", "NAGASAKI Miyu",
         "CHENG Hsien-Tzu", "LIN Ye", "ZHANG Rui", "BATRA Manika", "CHOI Hyojoo", "MORI Sakura", "LIU Fei",
         "CHA Hyo Sim", "ZENG Jian", "YANG Haeun", "ANDO Minami", "SUN Mingyang", "LIU Hsing-Yin",
         "PARANANG Orawan", "OJIO Haruna", "ZHU Chengzhu", "SHIOMI Maki", "SHIN Yubin", "MUKHERJEE Sutirtha",
         "KIM Nam Hae", "LIU Weishan"],["MESHREF Dina", "HELMY Yousra"],
        ["DIAZ Adriana", "ZHANG Lily", "WU Yue", "ZHANG Mo", "TAKAHASHI Bruna", "DIAZ Melanie", "VEGA Paulina"]]
    return PLAYERS_LIST
