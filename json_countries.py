"""
Json files.

Creates a json file with the questions and answers for all the countries in the world.
"""

import json


def create_json_europe(filename, questions, countries):
    """
    Creates a json file for the countries situated in Europe with all their attributes.

    Q_1, Q_2, etc., are lists containing the answers 'yes' or 'no' for every question
    related to the European countries.

    Each element of the list, either 'yes' or 'no', corresponds to the answer in the order of the EUROPE tuple.

    For example, in Q_1, the corresponding question is: "Is the population of your country over 30 million?".
    The first element of the tuple, 'no', corresponds to 'Albania',
    the second element of the tuple, 'no', corresponds to 'Andorra', etc.

    -------------
    filename : .json
        name of json file created.

    questions : tuple
        list of all the questions for the European countries.

    countries : tuple
        list of all the European countries.
    """
    EUROPE = ("Albania", "Andorra", "Austria", "Belarus", "Belgium", "Bosnia and Herzegovina", "Bulgaria", "Croatia",
              "Czech Republic", "Cyprus", "Denmark", "Estonia", "Finland", "France", "Georgia", "Germany", "Greece",
              "Hungary", "Iceland", "Ireland", "Italy", "Latvia", "Liechtenstein", "Lithuania", "Luxembourg", "Malta",
              "Moldova", "Monaco", "Montenegro", "Netherlands", "North Macedonia", "Norway", "Poland", "Portugal",
              "Romania", "Russia", "San Marino", "Serbia", "Slovakia", "Slovenia", "Spain", "Sweden", "Switzerland",
              "Turkey", "Ukraine", "United Kingdom")

    # "Is the population of your country over 30 million?"
    Q_1 = ('no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'yes', 'no', 'yes', 'no', 'no',
           'no', 'no', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'yes', 'no', 'no',
           'yes', 'no', 'no', 'no', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'yes')

    # "Is the population of your country over 10 million?"
    Q_2 = ('no', 'no', 'no', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no', 'no', 'no', 'yes', 'no', 'yes', 'yes',
           'no', 'no', 'no', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'yes', 'no', 'no', 'yes', 'yes',
           'yes', 'yes', 'no', 'no', 'no', 'no', 'yes', 'yes', 'no', 'yes', 'yes', 'yes')

    # "Is the population of your country over 5 million?"
    Q_3 = ('no', 'no', 'yes', 'yes', 'yes', 'no', 'yes', 'no', 'no', 'yes', 'no', 'yes', 'yes', 'yes', 'yes', 'yes',
           'yes', 'yes', 'no', 'no', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'yes', 'no', 'yes', 'yes',
           'yes', 'yes', 'yes', 'no', 'yes', 'yes', 'no', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes')

    # "Is Dutch an official language in your country?"
    Q_4 = ('no', 'no', 'no', 'no', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no',
           'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'yes', 'no', 'no', 'no', 'no', 'no', 'no',
           'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no')

    # "Is English an official language in your country?"
    Q_5 = ('no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no',
           'no', 'yes', 'no', 'no', 'no', 'no', 'no', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no',
           'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'yes')

    # "Is Italian an official language in your country?"
    Q_6 = ('no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no',
           'no', 'no', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no',
           'yes', 'no', 'no', 'no', 'no', 'no', 'yes', 'no', 'no', 'no')

    # "Is French an official language in your country?"
    Q_7 = ('no', 'no', 'no', 'no', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'yes', 'no', 'no', 'no', 'no',
           'no', 'no', 'no', 'no', 'no', 'no', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no',
           'no', 'no', 'no', 'no', 'no', 'no', 'yes', 'no', 'no', 'no')

    # "Is German an official language in your country?"
    Q_8 = ('no', 'no', 'yes', 'no', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'yes', 'no',
           'no', 'no', 'no', 'no', 'no', 'yes', 'no', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no',
           'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'yes', 'no', 'no', 'no')

    # "Is your country part of the European Union?"
    Q_9 = ('no', 'no', 'yes', 'no', 'yes', 'no', 'yes', 'yes', 'yes', 'no', 'yes', 'yes', 'yes', 'yes', 'no', 'yes',
           'yes', 'yes', 'no', 'yes', 'yes', 'yes', 'no', 'yes', 'yes', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no',
           'yes', 'yes', 'yes', 'no', 'no', 'no', 'yes', 'yes', 'yes', 'yes', 'no', 'no', 'no', 'no')

    # "Is Euro the official currency of your country?"
    Q_10 = ('no', "yes", "yes", 'no', "yes", 'no', 'no', 'no', 'no', "yes", 'no', "yes", "yes", "yes", 'no', "yes",
            "yes", 'no', 'no', "yes", "yes", "yes", "no", 'yes', "yes", "yes", 'no', "yes", "yes", "yes", "no",
            'no', 'no', "yes", 'no', 'no', "yes", "no", 'yes', "yes", "yes", 'no', 'no', "no", 'no', 'no')

    # "Is your country situated in the Nordic region?"
    Q_11 = ('no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'yes', 'no', 'yes', 'no', 'no', 'no', 'no',
            'no', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'yes', 'no', 'no',
            'no', 'no', 'no', 'no', 'no', 'no', 'no', 'yes', 'no', 'no', 'no', 'no')

    # "Does your country touches The Mediterranean Sea?"
    Q_12 = ('yes', 'no', 'no', 'no', 'no', 'yes', 'no', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no', 'yes',
            'no', 'no', 'no', 'yes', 'no', 'no', 'no', 'no', 'yes', 'no', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no',
            'no', 'no', 'no', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes', 'no', 'no')

    # "Was your country part of Yougoslavia?"
    Q_13 = ('no', 'no', 'no', 'no', 'no', 'yes', 'no', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no',
            'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'yes', 'no', 'yes', 'no', 'no',
            'no', 'no', 'no', 'no', 'yes', 'no', 'yes', 'no', 'no', 'no', 'no', 'no', 'no')

    # "Does the flag of your country has 3 or more colors?"
    Q_14 = ('no', 'yes', 'no', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'no', 'yes', 'no', 'yes', 'no', 'yes',
            'no', 'yes', 'yes', 'yes', 'yes', 'no', 'yes', 'yes', 'yes', 'no', 'yes', 'no', 'yes', 'yes', 'no',
            'yes', 'no', 'yes', 'yes', 'yes', 'no', 'yes', 'yes', 'yes', 'yes', 'no', 'no', 'no', 'no', 'yes')

    # "Does the flag of your country has blue cross?"
    Q_15 = ('no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'yes', 'no', 'no', 'no', 'no', 'no',
            'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'yes', 'no', 'no', 'no', 'no',
            'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no')

    # "Does the flag of your country has a cross?"
    Q_16 = ('no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'yes', 'no', 'yes', 'no', 'yes', 'no', 'yes',
            'no', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'yes', 'no', 'no',
            'no', 'no', 'no', 'no', 'no', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes')

    # "Does the flag of your country contains red?"
    Q_17 = ('yes', 'yes', 'yes', 'yes', 'yes', 'no', 'yes', 'yes', 'yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'yes',
            'no', 'yes', 'yes', 'no', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes',
            'yes', 'yes', 'yes', 'yes', 'yes', 'no', 'yes', 'yes', 'yes', 'yes', 'no', 'yes', 'yes', 'no', 'yes')

    dict_json = {}
    for k in range(0, len(countries)):
        dict_question = {}
        for j in range(0, len(questions)):
            dict_question[questions[j]] = locals()[f"Q_{j + 1}"][k]
        dict_json[countries[k]] = dict_question

    json_file = json.dumps(dict_json, indent=4)
    with open(filename, "w", encoding='utf-8') as f:
        return f.write(json_file)


def create_json_asia(filename, questions, countries):
    """
    Creates a json file for the countries situated in Asia with all their attributes.

    Q_1, Q_2, etc., are lists containing the answers 'yes' or 'no' for every question
    related to the Asian countries.

    Each element of the list, either 'yes' or 'no', corresponds to the answer in the order of the ASIA tuple.

    For example, in Q_1, the corresponding question is: "Is the population of your country over 100 million?".
    The first element of the tuple, 'no', corresponds to 'Afghanistan',
    the second element of the tuple, 'no', corresponds to 'Armenia', etc.

    -------------
    filename : .json
        name of json file created.

    questions : tuple
        list of all the questions for the Asian countries.

    countries : tuple
        list of all the Asian countries.
    """
    ASIA = ("Afghanistan", "Armenia", "Azerbaijan", "Bahrain", "Bangladesh", "Bhutan", "Brunei", "Cambodia", "China",
            "India", "Indonesia", "Iran", "Iraq", "Israel", "Japan", "Jordan", "Kazakhstan", "Kuwait", "Kyrgyzstan",
            "Laos", "Lebanon", "Malaysia", "Maldives", "Mongolia", "Myanmar", "Nepal", "North Korea", "Oman",
            "Pakistan", "Philippines", "Qatar", "Saudi Arabia", "Singapore", "South Korea", "Sri Lanka",
            "Palestine", "Syria", "Tajikistan", "Thailand", "Timor-Leste", "Turkmenistan", "United Arab Emirates",
            "Uzbekistan", "Vietnam", "Yemen")

    # "Is the population of your country over 100 million?"
    Q_1 = ('no', 'no', 'no', 'no', 'yes', 'no', 'no', 'no', 'yes', 'yes', 'yes', 'no', 'no', 'no', 'yes', 'no',
           'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'yes', 'yes', 'no',
           'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no')

    # "Is the population of your country over 30 million?"
    Q_2 = ('yes', 'no', 'no', 'no', 'yes', 'no', 'no', 'no', 'yes', 'yes', 'yes', 'yes', 'yes', 'no', 'yes',
           'no', 'no', 'no', 'no', 'no', 'no', 'yes', 'no', 'no', 'yes', 'no', 'no', 'no', 'yes', 'yes', 'no', 'yes',
           'no', 'yes', 'no', 'no', 'no', 'no', 'yes', 'no', 'no', 'no', 'yes', 'yes', 'no')

    # "Is the population of your country over 10 million?"
    Q_3 = ('yes', 'no', 'yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'no',
           'yes', 'yes', 'yes', 'no', 'no', 'no', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'yes', 'no', 'yes',
           'yes', 'no', 'yes', 'no', 'yes', 'yes', 'no', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'yes', 'yes')

    # "Is the population of your country over 5 million?"
    Q_4 = ("yes", "no", "yes", "no", "yes", "no", "no", "yes", "yes", "yes", "yes", "yes", "yes", "yes", "yes", "yes",
           "yes", "no", "yes", "yes", "yes", "yes", "no", "no", "yes", "yes", "yes", "yes", "yes", "yes", "no", "yes",
           "yes", "yes", "yes", "yes", "yes", "yes", "yes", "no", "yes", "yes", "yes", "yes", "yes")

    # "Is Arabic an official language in your country?"
    Q_5 = ("no", "no", "no", "yes", "no", "no", "no", "no", "no", "no", "no", "no", "yes", "no", "no", "yes", "no",
           "yes", "no", "no", "yes", "no", "no", "no", "no", "no", "no", "yes", "no", "no", "yes", "yes", "no", "no",
           "no", "no", "yes", "no", "no", "no", "no", "yes", "no", "no", "yes")

    # "Is your country situated in Middle East region?"
    Q_6 = ("no", "no", "no", "yes", "no", "no", "no", "no", "no", "no", "no", "yes", "yes", "yes", "no", "yes", "no",
           "yes", "no", "no", "yes", "no", "no", "no", "no", "no", "no", "yes", "no", "no", "yes", "yes", "no", "no",
           "no", "yes", "yes", "no", "no", "no", "no", "yes", "no", "no", "yes")

    # "Is Hinduism the most practiced religion in your country?"
    Q_7 = ('no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'yes', 'no', 'no', 'no', 'no', 'no',
           'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'yes', 'no', 'no', 'no', 'no',
           'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no')

    # "Is Folk religion the most practiced religion in your country?"
    Q_8 = ('no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'yes', 'no', 'no', 'no', 'no', 'no', 'no',
           'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no',
           'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'yes', 'no')

    # "Is Christianity the most practiced religion in your country?"
    Q_9 = ('no', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no',
           'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'yes', 'no',
           'no', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'yes', 'no', 'no', 'no', 'no', 'no')

    # "Is Buddhism the most practiced religion in your country?"
    Q_10 = ('no', 'no', 'no', 'no', 'no', 'yes', 'no', 'yes', 'no', 'no', 'no', 'no', 'no', 'no',
            'yes', 'no', 'no', 'no', 'no', 'yes', 'no', 'no', 'no', 'yes', 'yes', 'no', 'no', 'no', 'no',
            'no', 'no', 'no', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no', 'no', 'no', 'no', 'no')

    # "Is Islam the most practiced religion in your religion?"
    Q_11 = ("yes", "no", "yes", "yes", "yes", "no", "yes", "no", "no", "no", "yes", "yes", "yes", "no", "no", "yes",
            "yes", "yes", "yes", "no", "yes", "yes", "yes", "no", "no", "no", "no", "yes", "yes", "no", "yes", "yes",
            "no", "no", "no", "yes", "yes", "yes", "no", "no", "yes", "yes", "yes", "no", "yes",)

    # "Is your country an island?"
    Q_12 = ("no", "no", "no", "no", "no", "no", "yes", "no", "no", "no", "yes", "no", "no", "no", "yes", "no", "no",
            "no", "no", "no", "no", "yes", "yes", "no", "no", "no", "no", "no", "no", "yes", "no", "no", "yes", "no",
            "yes", "no", "no", "no", "no", "yes", "no", "no", "no", "no", "no")

    # "Does your country touches the Indian Ocean?"
    Q_13 = ("no", "no", "no", "yes", "yes", "no", "no", "no", "no", "yes", "yes", "yes", "yes", "yes", "no",
            "yes", "no", "yes", "no", "no", "no", "yes", "yes", "no", "yes", "no", "no", "yes", "yes", "no", "yes",
            "yes", "yes", "no", "yes", "no", "no", "no", "yes", "yes", "no", "yes", "no", "no", "yes")

    # "Does your country touches the Pacific Ocean?"
    Q_14 = ("no", "no", "no", "no", "no", "no", "yes", "yes", "yes", "no", "yes", "no", "no", "no", "yes", "no",
            "no", "no", "no", "no", "no", "yes", "no", "no", "no", "no", "yes", "no", "no", "yes", "no", "no",
            "yes", "yes", "no", "no", "no", "no", "yes", "yes", "no", "no", "no", "yes", "no")

    # "Does the flag of your country contains red?"
    Q_15 = ("yes", "yes", "yes", "yes", "yes", "no", "yes", "yes", "yes", "no", "yes", "yes", "yes", "no", "yes", "yes",
            "no", "yes", "yes", "yes", "yes", "yes", "yes", "yes", "yes", "yes", "yes", "yes", "no", "yes", "yes", "no",
            "yes", "yes", "yes", "yes", "yes", "yes", "yes", "yes", "yes", "yes", "yes", "yes", "yes")

    # "Does the flag of your country contains blue?"
    Q_16 = ("no", "yes", "yes", "no", "no", "no", "no", "yes", "no", "yes", "no", "no", "no", "yes", "no", "no", "yes",
            "no", "no", "yes", "no", "yes", "no", "yes", "no", "yes", "yes", "no", "no", "yes", "no", "no", "no", "yes",
            "no", "no", "no", "no", "yes", "no", "no", "no", "yes", "no", "no")

    # "Does the flag of your country contains green?"
    Q_17 = ("yes", "no", "yes", "no", "yes", "no", "no", "no", "no", "yes", "no", "yes", "yes", "no", "no", "yes",
            "no", "yes", "no", "no", "yes", "no", "yes", "no", "yes", "no", "no", "yes", "yes", "no", "no", "yes", "no",
            "no", "yes", "yes", "yes", "yes", "no", "no", "yes", "yes", "yes", "no", "no",)

    #  "Does the flag of your country contains yellow?"
    Q_18 = ("no", "yes", "no", "no", "no", "yes", "yes", "no", "yes", "no", "no", "no", "no", "no", "no", "no", "yes",
            "no", "yes", "no", "no", "yes", "no", "yes", "yes", "no", "no", "no", "no", "yes", "no", "no", "no", "no",
            "yes", "no", "no", "yes", "no", "yes", "no", "no", "no", "yes", "no")

    # "Is there a star on the flag of your country?"
    Q_19 = ("no", "no", "yes", "no", "no", "no", "no", "no", "yes", "no", "no", "no", "no", "yes", "no", "yes", "no",
            "no", "no", "no", "no", "no", "no", "no", "yes", "no", "yes", "no", "yes", "no", "no", "no", "yes", "no",
            "no", "no", "yes", "yes", "no", "yes", "yes", "no", "yes", "yes", "no")

    # "Is there a moon on the flag your country?"
    Q_20 = ("no", "no", "yes", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no",
            "no", "no", "no", "yes", "yes", "no", "no", "no", "no", "no", "yes", "no", "no", "no", "yes", "no", "no",
            "no", "no", "no", "no", "no", "yes", "no", "yes", "no", "no")

    # "Is there a circled object or a sun on the flag of your country?"
    Q_21 = ("no", "no", "no", "no", "yes", "no", "no", "no", "no", "yes", "no", "no", "no", "no", "yes", "no", "yes",
            "no", "yes", "yes", "no", "no", "no", "no", "no", "no", "yes", "no", "no", "yes", "no", "no", "no", "yes",
            "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no")
    dict_json = {}
    for k in range(0, len(countries)):
        dict_question = {}
        for j in range(0, len(questions)):
            dict_question[questions[j]] = locals()[f"Q_{j + 1}"][k]
        dict_json[countries[k]] = dict_question

    json_file = json.dumps(dict_json, indent=4)
    with open(filename, "w", encoding='utf-8') as f:
        return f.write(json_file)


def create_json_africa(filename, questions, countries):
    """
    Creates a json file for the countries situated in Africa with all their attributes.

    Q_1, Q_2, etc., are lists containing the answers 'yes' or 'no' for every question
    related to the African countries.

    Each element of the list, either 'yes' or 'no', corresponds to the answer in the order of the AFRICA tuple.

    For example, in Q_1, the corresponding question is: "Is the population of your country over 100 million?".
    The first element of the tuple, 'no', corresponds to 'Afghanistan',
    the second element of the tuple, 'no', corresponds to 'Armenia', etc.

    -------------
    filename : .json
        name of json file created.

    questions : tuple
        list of all the questions for the Asian countries.

    countries : tuple
        list of all the Asian countries.
    """
    AFRICA = ("Algeria", "Angola", "Benin", "Botswana", "Burkina Faso", "Burundi", "Cabo Verde", "Cameroon",
              "Central African Republic", "Chad", "Comoros", "Congo", "Côte d'Ivoire", "Djibouti", "DR Congo",
              "Egypt",
              "Equatorial Guinea", "Eritrea", "Eswatini", "Ethiopia", "Gabon", "Gambia", "Ghana", "Guinea",
              "Guinea-Bissau",
              "Kenya", "Lesotho", "Liberia", "Libya", "Madagascar", "Malawi", "Mali", "Mauritania", "Mauritius",
              "Morocco",
              "Mozambique", "Namibia", "Niger", "Nigeria", "Rwanda", "Sao Tome and Principe", "Senegal",
              "Seychelles",
              "Sierra Leone", "Somalia", "South Africa", "South Sudan", "Sudan", "Tanzania", "Togo", "Tunisia",
              "Uganda",
              "Zambia", "Zimbabwe")

    # "Is the population of your country over 30 million?"
    Q_1 = ("yes", "yes", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "yes", "yes", "no",
           "no", "no", "yes", "no", "no", "yes", "no", "no", "yes", "no", "no", "no", "no", "no", "no", "no", "no",
           "yes", "yes", "no", "no", "yes", "no", "no", "no", "no", "no", "no", "yes", "no", "yes", "yes", "no", "no",
           "yes", "no", "no")

    # "Is the population of your country over 10 million?"
    Q_2 = ("yes", "yes", "yes", "no", "yes", "yes", "no", "yes", "no", "yes", "no", "no", "yes", "no", "yes", "yes",
           "no", "no", "no", "yes", "no", "no", "yes", "yes", "no", "yes", "no", "no", "no", "yes", "yes", "yes",
           "no", "no", "yes", "yes", "no", "yes", "yes", "yes", "no", "yes", "no", "no", "yes", "yes", "yes",
           "yes", "yes", "no", "yes", "yes", "yes", "yes")

    # "Is the population of your country over 5 million?"
    Q_3 = ("yes", "yes", "yes", "no", "yes", "yes", "no", "yes", "no", "yes", "no", "yes", "yes", "no", "yes", "yes",
           "no", "no", "no", "yes", "no", "no", "yes", "yes", "no", "yes", "no", "yes", "yes", "yes", "yes", "yes",
           "no", "no", "yes", "yes", "no", "yes", "yes", "yes", "no", "yes", "no", "yes", "yes", "yes", "yes", "yes",
           "yes", "yes", "yes", "yes", "yes", "yes")

    # "Is French an official language in your country?"
    Q_4 = ("no", "no", "yes", "no", "yes", "yes", "no", "yes", "yes", "yes", "yes", "yes", "yes", "yes", "yes", "no",
           "yes", "no", "no", "no", "yes", "no", "no", "yes", "no", "no", "no", "no", "no", "yes", "no", "yes", "no",
           "no", "no", "no", "no", "yes", "no", "yes", "no", "yes", "yes", "no", "no", "no", "no", "no", "no", "yes",
           "no", "no", "no", "no")

    # "Is English an official language in your country?"
    Q_5 = ("no", "no", "no", "yes", "no", "yes", "no", "yes", "no", "no", "no", "no", "no", "no", "no", "no", "no",
           "yes", "yes", "no", "no", "yes", "yes", "no", "no", "yes", "yes", "yes", "no", "no", "yes", "no", "no",
           "yes", "no", "no", "yes", "no", "yes", "yes", "no", "no", "yes", "yes", "no", "yes", "yes", "yes", "yes",
           "no", "no", "yes", "yes", "yes")

    # "Is Arabic an official language in your country?"
    Q_6 = ("yes", "no", "no", "no", "no", "no", "no", "no", "no", "yes", "yes", "no", "no", "yes", "no", "yes",
           "no", "yes", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "yes", "no", "no", "no", "yes",
           "no", "yes", "no", "no", "no", "no", "no", "no", "no", "no", "no", "yes", "no", "no", "yes", "no",
           "no", "yes", "no", "no", "no")

    # "Is Portuguese an official language in your country?"
    Q_7 = ("no", "yes", "no", "no", "no", "no", "yes", "no", "no", "no", "no", "no", "no", "no", "no", "no", "yes",
           "no", "no", "no", "no", "no", "no", "no", "yes", "no", "no", "no", "no", "no", "no", "no", "no", "no",
           "no", "yes", "no", "no", "no", "no", "yes", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no",
           "no", "no", "no",)

    # "Is your country an island?"
    Q_8 = ("no", "no", "no", "no", "no", "no", "yes", "no", "no", "no", "yes", "no", "no", "no", "no", "no",
           "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "yes", "no", "no", "no", "yes",
           "no", "no", "no", "no", "no", "no", "yes", "no", "yes", "no", "no", "no", "no", "no", "no", "no", "no",
           "no", "no", "no")

    # "Is Islam the most practiced religion in your religion?"
    Q_9 = ("yes", "no", "no", "no", "yes", "no", "no", "no", "no", "yes", "yes", "no", "yes", "yes", "no", "yes",
           "no", "no", "no", "no", "no", "yes", "no", "yes", "yes", "no", "no", "no", "yes", "no", "no", "yes",
           "yes", "no", "yes", "no", "no", "yes", "yes", "no", "no", "yes", "no", "yes", "yes", "no", "no", "yes",
           "no", "no", "yes", "no", "no", "no")

    # "Is Christianity the most practiced religion in your country?"
    Q_10 = ('no', 'yes', 'yes', 'yes', 'no', 'yes', 'yes', 'yes', 'yes', 'no', 'no', 'yes', 'no', 'no', 'yes',
            'no', 'yes', 'yes', 'yes', 'yes', 'yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'yes', 'no', 'yes',
            'yes', 'no', 'no', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'yes', 'no', 'no',
            'yes', 'yes', 'no', 'yes', 'yes', 'no', 'yes', 'yes', 'yes')

    # "Does your country touches the Atlantic Ocean?(including The Mediterranean Sea)"
    Q_11 = ("yes", "yes", "yes", "no", "no", "no", "yes", "yes", "no", "no", "no", "yes", "yes", "no", "yes", "yes",
            "yes", "no", "no", "no", "yes", "yes", "yes", "yes", "yes", "no", "no", "yes", "yes", "no", "no", "no",
            "yes", "no", "yes", "no", "yes", "no", "yes", "no", "yes", "yes", "no", "yes", "no", "yes", "no", "no",
            "no", "yes", "yes", "no", "no", "no")

    # "Does your country touches the Indian Ocean?(including The Red Sea and The Arabian Sea)"
    Q_12 = ('no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'yes', 'no', 'no', 'yes',
            'no', 'yes', 'no', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'yes', 'no', 'no',
            'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'yes', 'no', 'no', 'no', 'no', 'no', 'no',
            'yes', 'no', 'yes', 'yes', 'no', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no')

    # "Does the flag of your country contains at least 3 or more colors?"
    Q_13 = ('yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes',
            'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes',
            'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'no', 'yes', 'yes', 'yes', 'no', 'yes', 'yes', 'yes',
            'yes', 'yes', 'no', 'yes', 'yes', 'yes', 'yes', 'yes', 'no', 'yes', 'yes', 'yes')

    # "Does the flag of your country contains red?"
    Q_14 = ("yes", "yes", "yes", "no", "yes", "yes", "yes", "yes", "yes", "yes", "yes", "yes", "no", "yes", "yes",
            "yes", "yes", "yes", "yes", "yes", "no", "yes", "yes", "yes", "yes", "yes", "no", "yes", "yes", "yes",
            "yes", "yes", "yes", "yes", "yes", "yes", "yes", "no", "no", "no", "yes", "yes", "yes", "no", "no",
            "yes", "yes", "yes", "no", "yes", "yes", "yes", "yes", "yes",)

    # "Does the flag of your country contains blue?"
    Q_15 = ("no", "no", "no", "yes", "no", "no", "yes", "no", "yes", "yes", "yes", "no", "no", "yes", "yes", "no",
            "yes", "yes", "yes", "yes", "yes", "yes", "no", "no", "no", "no", "yes", "yes", "no", "no", "no", "no",
            "no", "yes", "no", "no", "yes", "no", "no", "yes", "no", "no", "yes", "yes", "yes", "yes", "yes", "no",
            "yes", "no", "no", "no", "no", "no",)

    # "Does the flag of your country contains green?"
    Q_16 = ("yes", "no", "yes", "no", "yes", "yes", "no", "yes", "yes", "no", "yes", "yes", "yes", "yes", "no", "no",
            "yes", "yes", "no", "yes", "yes", "yes", "yes", "yes", "yes", "yes", "yes", "no", "yes", "yes", "yes",
            "yes", "yes", "yes", "no", "yes", "yes", "yes", "yes", "yes", "yes", "yes", "yes", "yes", "no", "yes",
            "yes", "yes", "yes", "yes", "no", "no", "yes", "yes")

    # "Does the flag of your country contains yellow?"
    Q_17 = ("no", "yes", "yes", "no", "yes", "no", "no", "yes", "yes", "yes", "yes", "yes", "no", "no", "yes", "yes",
            "no", "yes", "yes", "yes", "yes", "no", "yes", "yes", "yes", "no", "no", "no", "no", "no", "no", "yes",
            "yes", "yes", "no", "yes", "yes", "no", "no", "yes", "yes", "yes", "yes", "no", "no", "yes", "yes",
            "no", "yes", "yes", "no", "yes", "no", "yes")

    # "Is there a star on the flag of your country?"
    Q_18 = ("yes", "yes", "no", "no", "yes", "yes", "yes", "yes", "yes", "no", "yes", "no", "no", "yes", "yes",
            "no", "no", "no", "no", "yes", "no", "no", "yes", "no", "yes", "no", "no", "yes", "yes", "no", "no",
            "no", "yes", "no", "yes", "yes", "no", "no", "no", "no", "yes", "yes", "no", "no", "yes", "no",
            "yes", "no", "no", "yes", "yes", "no", "no", "yes")

    # "Is there a moon on the flag your country?"
    Q_19 = ("yes", "no", "no", "no", "no", "no", "no", "no", "no", "no", "yes", "no", "no", "no", "no", "no",
            "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "yes", "no", "no", "no",
            "yes", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no",
            "no", "no", "yes", "no", "no", "no",)
    dict_json = {}
    for k in range(0, len(countries)):
        dict_question = {}
        for j in range(0, len(questions)):
            dict_question[questions[j]] = locals()[f"Q_{j + 1}"][k]
        dict_json[countries[k]] = dict_question

    json_file = json.dumps(dict_json, indent=4)
    with open(filename, "w", encoding='utf-8') as f:
        return f.write(json_file)


def create_json_north(filename, questions, countries):
    """
    Creates a json file for the countries situated in Africa with all their attributes.

    Q_1, Q_2, etc., are lists containing the answers 'yes' or 'no' for every question
    related to the African countries.

    Each element of the list, either 'yes' or 'no', corresponds to the answer in the order of the AFRICA tuple.

    For example, in Q_1, the corresponding question is: "Is the population of your country over 100 million?".
    The first element of the tuple, 'no', corresponds to 'Afghanistan',
    the second element of the tuple, 'no', corresponds to 'Armenia', etc.

    -------------
    filename : .json
        name of json file created.

    questions : tuple
        list of all the questions for the Asian countries.

    countries : tuple
        list of all the Asian countries.
    """
    NORTH_AMERICA = ("Antigua and Barbuda", "Bahamas", "Barbados", "Belize", "Canada", "Costa Rica", "Cuba",
                     "Dominica", "Dominican Republic", "El Salvador", "Grenada", "Guatemala", "Haiti",
                     "Honduras", "Jamaica", "Mexico", "Nicaragua", "Panama", "Saint Kitts and Nevis",
                     "Saint Lucia", "St. Vincent and Grenadines", "Trinidad and Tobago",
                     "United States of America")
    # "pop over 30m"
    Q_1 = ('no', 'no', 'no', 'no', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no',
           'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'yes')

    # "pop over 10m"
    Q_2 = ('no', 'no', 'no', 'no', 'yes', 'no', 'yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no',
           'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'yes')

    # "pop over 5m"
    Q_3 = ("no", "no", "no", "no", "yes", "yes", "yes", "no", "yes", "yes", "no", "yes", "yes", "yes", "no", "yes",
           "yes", "no", "no", "no", "no", "no", "yes")

    # "spanish?"
    Q_4 = ("no", "no", "no", "no", "no", "yes", "yes", "no", "yes", "yes", "no", "yes", "no", "yes", "no",
           "yes", "yes", "yes", "no", "no", "no", "no", "no")

    # "english?"
    Q_5 = ("yes", "yes", "yes", "yes", "yes", "no", "no", "yes", "no", "no", "yes", "no", "no", "no", "yes",
           "no", "no", "no", "yes", "yes", "yes", "yes", "yes")

    # "country touches atlantic ocean?"
    Q_6 = ("yes", "yes", "yes", "yes", "yes", "yes", "yes", "yes", "yes", "no", "yes", "yes", "yes", "yes", "yes",
           "yes", "yes", "yes", "yes", "yes", "yes", "yes", "yes")

    # "country touching pacific ocean?"
    Q_7 = ("no", "no", "no", "no", "yes", "yes", "no", "no", "no", "yes", "no", "yes", "no", "no", "no", "yes",
           "yes", "yes", "no", "no", "no", "no", "yes")

    # "flag contains red?"
    Q_8 = ("yes", "no", "no", "yes", "yes", "yes", "yes", "yes", "yes", "no", "yes", "no", "yes", "no", "no",
           "yes", "no", "yes", "yes", "no", "no", "yes", "yes",)

    # "Flag contains blue?"
    Q_9 = ("yes", "yes", "yes", "yes", "no", "yes", "yes", "no", "yes", "yes", "no", "yes", "yes", "yes",
           "no", "no", "yes", "yes", "no", "yes", "yes", "no", "yes")

    # "flag contains yellow?"
    Q_10 = ("yes", "yes", "yes", "no", "no", "no", "no", "yes", "no", "no", "yes", "no", "no", "no", "yes", "no",
            "no", "no", "yes", "yes", "yes", "no", "no")

    # "flag contains green?"
    Q_11 = ("no", "no", "no", "no", "no", "no", "no", "yes", "no", "no", "yes", "no", "no", "no", "yes", "yes", "no",
            "no", "yes", "no", "yes", "no", "no")

    # "flag contains black?"
    Q_12 = ("yes", "yes", "no", "no", "no", "no", "no", "yes", "no", "no", "no", "no", "no", "no", "yes", "no",
            "no", "no", "yes", "yes", "no", "yes", "no")

    # "flag contains star?"
    Q_13 = ("no", "no", "no", "no", "no", "no", "yes", "no", "no", "no", "yes", "no", "no", "yes", "no", "no", "no",
            "yes", "yes", "no", "no", "no", "yes")

    dict_json = {}
    for k in range(0, len(countries)):
        dict_question = {}
        for j in range(0, len(questions)):
            dict_question[questions[j]] = locals()[f"Q_{j + 1}"][k]
        dict_json[countries[k]] = dict_question

    json_file = json.dumps(dict_json, indent=4)
    with open(filename, "w", encoding='utf-8') as f:
        return f.write(json_file)


def create_json_south(filename, questions, countries):
    """
    Creates a json file for the countries situated in Africa with all their attributes.

    Q_1, Q_2, etc., are lists containing the answers 'yes' or 'no' for every question
    related to the African countries.

    Each element of the list, either 'yes' or 'no', corresponds to the answer in the order of the AFRICA tuple.

    For example, in Q_1, the corresponding question is: "Is the population of your country over 100 million?".
    The first element of the tuple, 'no', corresponds to 'Afghanistan',
    the second element of the tuple, 'no', corresponds to 'Armenia', etc.

    -------------
    filename : .json
        name of json file created.

    questions : tuple
        list of all the questions for the Asian countries.

    countries : tuple
        list of all the Asian countries.
    """
    SOUTH_AMERICA = ("Argentina", "Bolivia", "Brazil", "Chile", "Colombia", "Ecuador", "Guyana", "Paraguay",
                     "Peru", "Suriname", "Uruguay", "Venezuela")
    # "Is the population of your country over 30 million?"
    Q_1 = ("yes", "no", "yes", "no", "yes", "no", "no", "no", "yes", "no", "no", "no")

    # "Is the population of your country over 10 million?"
    Q_2 = ("yes", "yes", "yes", "yes", "yes", "yes", "no", "no", "yes", "no", "no", "yes")

    # "Is the population of your country over 5 million?"
    Q_3 = ("yes", "yes", "yes", "yes", "yes", "yes", "no", "yes", "yes", "no", "no", "yes")

    # "Is Spanish an official language in your country?"
    Q_4 = ("yes", "yes", "no", "yes", "yes", "yes", "no", "yes", "yes", "no", "yes", "yes")

    # "Is the Amazon forest in your country?"
    Q_5 = ("no", "yes", "yes", "no", "yes", "yes", "yes", "no", "yes", "yes", "no", "yes")

    # "Does your country touches the Atlantic Ocean?"
    Q_6 = ("yes", "no", "yes", "yes", "yes", "no", "yes", "no", "no", "yes", "yes", "yes")

    # "Does your country touches the Pacific Ocean?"
    Q_7 = ("no", "no", "no", "yes", "yes", "yes", "no", "no", "yes", "no", "no", "no")

    # "Does the flag of your country contains red?"
    Q_8 = ("no", "yes", "no", "yes", "yes", "yes", "yes", "yes", "yes", "yes", "no", "yes")

    # "Does the flag of your country contains blue?"
    Q_9 = ("yes", "no", "yes", "yes", "yes", "yes", "no", "yes", "no", "no", "yes", "yes")

    # "Does the flag of your country contains green?"
    Q_10 = ("no", "yes", "yes", "no", "no", "no", "yes", "no", "no", "yes", "no", "no")

    # "Is there a star on the flag of your country?"
    Q_11 = ("no", "no", "no", "yes", "no", "no", "no", "no", "no", "yes", "no", "yes")

    # "Is there a circled object or a sun on the flag of your country?"
    Q_12 = ("yes", "no", "yes", "no", "no", "no", "no", "yes", "no", "no", "yes", "no",)

    dict_json = {}
    for k in range(0, len(countries)):
        dict_question = {}
        for j in range(0, len(questions)):
            dict_question[questions[j]] = locals()[f"Q_{j + 1}"][k]
        dict_json[countries[k]] = dict_question

    json_file = json.dumps(dict_json, indent=4)
    with open(filename, "w", encoding='utf-8') as f:
        return f.write(json_file)


def create_json_oceany(filename, questions, countries):
    """
    Creates a json file for the countries situated in Africa with all their attributes.

    Q_1, Q_2, etc., are lists containing the answers 'yes' or 'no' for every question
    related to the African countries.

    Each element of the list, either 'yes' or 'no', corresponds to the answer in the order of the AFRICA tuple.

    For example, in Q_1, the corresponding question is: "Is the population of your country over 100 million?".
    The first element of the tuple, 'no', corresponds to 'Afghanistan',
    the second element of the tuple, 'no', corresponds to 'Armenia', etc.

    -------------
    filename : .json
        name of json file created.

    questions : tuple
        list of all the questions for the Asian countries.

    countries : tuple
        list of all the Asian countries.
    """
    OCEANIA = ("Australia", "Fiji", "Kiribati", "Marshall Islands", "Micronesia", "Nauru", "New Zealand", "Palau",
               "Papua New Guinea", "Samoa", "Solomon Islands", "Tonga", "Tuvalu", "Vanuatu")

    # "pop over 10m?" 1
    Q_1 = ("yes", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no")

    # "pop over 1 million?" 2
    Q_2 = ("yes", "no", "no", "no", "no", "no", "yes", "no", "yes", "no", "no", "no", "no", "no")

    # "flag contains green?" 3
    Q_3 = ("no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "yes", "no", "no", "yes")

    # "flag contains blue?" 4
    Q_4 = ("yes", "yes", "yes", "yes", "yes", "yes", "yes", "yes", "no", "yes", "yes", "no", "yes", "no")

    # "flag contains red?" 6
    Q_5 = ("yes", "yes", "yes", "no", "no", "no", "yes", "no", "yes", "yes", "no", "yes", "yes", "yes")

    # "flag contains yellow?" 7
    Q_6 = ("no", "no", "yes", "no", "no", "yes", "no", "yes", "yes", "no", "yes", "no", "yes", "yes")

    # "flag contains stars?" 5
    Q_7 = ("yes", "no", "no", "no", "yes", "yes", "yes", "no", "yes", "yes", "yes", "no", "yes", "no")

    dict_json = {}
    for k in range(0, len(countries)):
        dict_question = {}
        for j in range(0, len(questions)):
            dict_question[questions[j]] = locals()[f"Q_{j + 1}"][k]
        dict_json[countries[k]] = dict_question

    json_file = json.dumps(dict_json, indent=4)
    with open(filename, "w", encoding='utf-8') as f:
        return f.write(json_file)
