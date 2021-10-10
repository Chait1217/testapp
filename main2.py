import json


def create_json_europe(filename, Questions, Countries):
    EUROPE = ["Albania", "Andorra", "Austria", "Belarus", "Belgium", "Bosnia and Herzegovina", "Bulgaria", "Croatia",
     "Czech Republic", "Cyprus", "Denmark", "Estonia", "Finland", "France", "Georgia", "Germany", "Greece",
     "Hungary", "Iceland", "Ireland", "Italy", "Latvia", "Liechtenstein", "Lithuania", "Luxembourg",
     "Malta",
     "Moldova", "Monaco", "Montenegro", "Netherlands", "North Macedonia", "Norway", "Poland", "Portugal",
     "Romania", "Russia", "San Marino", "Serbia", "Slovakia", "Slovenia", "Spain", "Sweden", "Switzerland",
     "Turkey", "Ukraine", "United Kingdom"]

    # Q1 = input("In Europe Union ?")Q_16
    Q_9 = ['no', 'no', 'yes', 'no', 'yes', 'no', 'yes', 'yes', 'yes', 'no', 'yes', 'yes', 'yes', 'yes', 'no', 'yes',
           'yes',
           'yes', 'no', 'yes', 'yes', 'yes', 'no', 'yes', 'yes', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no',
           'yes', 'yes', 'yes', 'no', 'no', 'no', 'yes', 'yes', 'yes', 'yes', 'no', 'no', 'no', 'no']

    # Q2 = input("Touches sea mediterean ?") Q_8
    Q_12 = ['yes', 'no', 'no', 'no', 'no', 'yes', 'no', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no', 'yes','no',
           'no', 'no', 'yes', 'no', 'no', 'no', 'no', 'yes', 'no', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no','no',
           'no', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes', 'no', 'no']

    # Q3 = input("Population over 5m")Q_15
    Q_3 = ['no', 'no', 'yes', 'yes', 'yes', 'no', 'yes', 'no', 'no', 'yes', 'no', 'yes', 'yes', 'yes', 'yes', 'yes','yes',
           'yes', 'no', 'no', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'yes', 'no', 'yes', 'yes', 'yes','yes',
           'yes', 'no', 'yes', 'yes', 'no', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes']

    # Q4 = input("Pop over 10m ?")Q_14
    Q_2 = ['no', 'no', 'no', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no', 'no', 'no', 'yes', 'no', 'yes', 'yes','no',
           'no', 'no', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'yes',
           'yes', 'no', 'no', 'no', 'no', 'yes', 'yes', 'no', 'yes', 'yes', 'yes']

    # Q5 = input("Pop over 30m ?") Q_13
    Q_1 = ['no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'yes', 'no', 'yes', 'no', 'no',
           'no', 'no', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'yes', 'no', 'no','yes',
           'no', 'no', 'no', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'yes']

    # Q6 = input("Speaks German ?")Q_6
    Q_8 = ['no', 'no', 'yes', 'no', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'yes', 'no','no',
           'no', 'no', 'no', 'no', 'yes', 'no', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no',
           'no', 'no', 'no', 'no', 'no', 'no', 'yes', 'no', 'no', 'no']

    # Q7 = input("Speaks French ?") Q_5
    Q_7 = ['no', 'no', 'no', 'no', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'yes', 'no', 'no', 'no', 'no',
           'no', 'no', 'no', 'no', 'no', 'no', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no',
           'no', 'no', 'no', 'no', 'no', 'no', 'yes', 'no', 'no', 'no']

    # Q8 = input("Part of Yougoslavia ?") Q_9
    Q_13 = ['no', 'no', 'no', 'no', 'no', 'yes', 'no', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no',
           'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'yes', 'no', 'yes', 'no', 'no', 'no', 'no', 'no',
           'no', 'yes', 'no', 'yes', 'no', 'no', 'no', 'no', 'no', 'no']

    # Q9 = input("Flag contains red?") Q_12
    Q_17 = ['yes', 'yes', 'yes', 'yes', 'yes', 'no', 'yes', 'yes', 'yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'yes','no',
           'yes', 'yes', 'no', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes',
           'yes', 'yes', 'yes', 'no', 'yes', 'yes', 'yes', 'yes', 'no', 'yes', 'yes', 'no', 'yes']

    # Q10 = input("Flag with a cross?") Q_11
    Q_16 = ['no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'yes', 'no', 'yes', 'no', 'yes', 'no', 'yes',
            'no', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'yes', 'no', 'no',
            'no',
            'no', 'no', 'no', 'no', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']

    # input("Flag with Blue cross?")Q_2
    Q_15 = ['no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'yes', 'no', 'no', 'no', 'no', 'no',
            'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'yes', 'no', 'no', 'no', 'no',
            'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no']

    # q12 = input("Speaks Dutch") Q_1
    Q_4 = ['no', 'no', 'no', 'no', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no',
            'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'yes', 'no', 'no', 'no', 'no', 'no', 'no',
            'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no']

    # q13 = input("Speaks English") Q_3
    Q_5 = ['no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no',
            'no', 'yes', 'no', 'no', 'no', 'no', 'no', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no','no',
            'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'yes']

    # q14 = input("Flag has 3 or more colors ?") Q_10
    Q_14 = ['no', 'yes', 'no', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'no', 'yes', 'no', 'yes', 'no', 'yes',
            'no',
            'yes', 'yes', 'yes', 'yes', 'no', 'yes', 'yes', 'yes', 'no', 'yes', 'no', 'yes', 'yes', 'no', 'yes', 'no',
            'yes',
            'yes', 'yes', 'no', 'yes', 'yes', 'yes', 'yes', 'no', 'no', 'no', 'no', 'yes']

    # Q15 = input("Speaks Italien")Q_4
    Q_6 = ['no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no',
            'no', 'no', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no',
            'yes', 'no', 'no', 'no', 'no', 'no', 'yes', 'no', 'no', 'no']

    # Q16 = input("Situated in the Nordic region?") Q_7
    Q_11 = ['no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'yes', 'no', 'yes', 'no', 'no', 'no', 'no',
            'no',
            'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'yes', 'no', 'no', 'no',
            'no',
            'no', 'no', 'no', 'no', 'no', 'yes', 'no', 'no', 'no', 'no']

    # "euro in your country?" Q_17
    Q_10 = ['no', "yes", "yes", 'no', "yes", 'no', 'no', 'no', 'no', "yes", 'no', "yes", "yes", "yes", 'no', "yes",
            "yes",
            'no', 'no', "yes", "yes", "yes", "no", 'yes', "yes", "yes", 'no', "yes", "yes", "yes", "no", 'no', 'no',
            "yes",
            'no', 'no', "yes", "no", 'yes', "yes", "yes", 'no', 'no', "no", 'no', 'no']

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
    ASIA = ["Afghanistan", "Armenia", "Azerbaijan", "Bahrain",
     "Bangladesh", "Bhutan", "Brunei", "Cambodia", "China",
     "India", "Indonesia", "Iran", "Iraq", "Israel",
     "Japan", "Jordan", "Kazakhstan", "Kuwait", "Kyrgyzstan",
     "Laos", "Lebanon", "Malaysia", "Maldives",
     "Mongolia", "Myanmar", "Nepal", "North Korea", "Oman",
     "Pakistan", "Philippines", "Qatar", "Saudi Arabia",
     "Singapore", "South Korea", "Sri Lanka", "Palestine", "Syria",
     "Tajikistan", "Thailand", "Timor-Leste",
     "Turkmenistan", "United Arab Emirates", "Uzbekistan",
     "Vietnam", "Yemen"]
    # "pop over 5m?" 4
    Q_4 = ["yes", "no", "yes", "no", "yes", "no", "no", "yes", "yes", "yes", "yes", "yes", "yes", "yes", "yes", "yes",
           "yes", "no", "yes", "yes", "yes", "yes", "no", "no", "yes", "yes", "yes", "yes", "yes", "yes", "no", "yes",
           "yes", "yes", "yes", "yes", "yes", "yes", "yes", "no", "yes", "yes", "yes", "yes", "yes"]
    # "pop over 10m?" 3
    Q_3 = ['yes', 'no', 'yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'no',
           'yes', 'yes', 'yes', 'no', 'no', 'no', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'yes', 'no', 'yes',
           'yes', 'no', 'yes', 'no', 'yes', 'yes', 'no', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'yes', 'yes']
    # "pop over 30m?" 2
    Q_2 = ['yes', 'no', 'no', 'no', 'yes', 'no', 'no', 'no', 'yes', 'yes', 'yes', 'yes', 'yes', 'no', 'yes',
           'no', 'no', 'no', 'no', 'no', 'no', 'yes', 'no', 'no', 'yes', 'no', 'no', 'no', 'yes', 'yes', 'no', 'yes',
           'no', 'yes', 'no', 'no', 'no', 'no', 'yes', 'no', 'no', 'no', 'yes', 'yes', 'no']
    # "pop over 100m?" 1
    Q_1 = ['no', 'no', 'no', 'no', 'yes', 'no', 'no', 'no', 'yes', 'yes', 'yes', 'no', 'no', 'no', 'yes', 'no',
           'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'yes', 'yes', 'no',
           'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no']

    # "middle east?"
    Q_6 = ["no", "no", "no", "yes", "no", "no", "no", "no", "no", "no", "no", "yes", "yes", "yes", "no", "yes", "no",
           "yes", "no","no", "yes", "no", "no", "no", "no", "no", "no", "yes", "no", "no", "yes", "yes", "no", "no",
           "no", "yes","yes","no", "no", "no", "no", "yes", "no", "no", "yes"]

    # "arabic?"
    Q_5 = ["no", "no", "no", "yes", "no", "no", "no", "no", "no", "no", "no", "no", "yes", "no", "no", "yes", "no",
           "yes", "no", "no","yes", "no", "no", "no", "no", "no", "no", "yes", "no", "no", "yes", "yes", "no", "no",
           "no", "no", "yes","no", "no","no", "no", "yes", "no", "no", "yes"]

    # "muslim?" 11
    Q_11 = ["yes", "no", "yes", "yes", "yes", "no", "yes", "no", "no", "no", "yes", "yes", "yes", "no", "no", "yes",
           "yes","yes", "yes", "no", "yes", "yes", "yes", "no", "no", "no", "no", "yes", "yes", "no", "yes", "yes",
           "no","no", "no","yes", "yes", "yes", "no", "no", "yes", "yes", "yes", "no", "yes", ]

    # "christian?" 9
    Q_9 = ['no', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no',
           'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'yes', 'no',
           'no', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'yes', 'no', 'no', 'no', 'no','no']

    # "Buddhist?" 10
    Q_10 = ['no', 'no', 'no', 'no', 'no', 'yes', 'no', 'yes', 'no', 'no', 'no', 'no', 'no', 'no',
           'yes', 'no', 'no', 'no', 'no', 'yes', 'no', 'no', 'no', 'yes', 'yes', 'no', 'no', 'no', 'no',
           'no', 'no', 'no', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no', 'no', 'no', 'no', 'no']

    # "Folk religion?" 8
    Q_8 = ['no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'yes', 'no', 'no', 'no', 'no', 'no', 'no',
            'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no',
            'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'yes', 'no']

    # "Hindu?" 7
    Q_7 = ['no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'yes', 'no', 'no', 'no', 'no', 'no',
            'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'yes', 'no', 'no', 'no', 'no',
            'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no']

    # "touches indian ocean?"
    Q_13 = ["no", "no", "no", "yes", "yes", "no", "no", "no", "no", "yes", "yes", "yes", "yes", "yes", "no",
            "yes", "no", "yes", "no", "no", "no", "yes", "yes", "no", "yes", "no", "no", "yes", "yes", "no", "yes",
            "yes", "yes", "no", "yes", "no", "no", "no", "yes", "yes", "no", "yes", "no", "no", "yes"]

    # "pacific ocean?"
    Q_14 = ["no", "no", "no", "no", "no", "no", "yes", "yes", "yes", "no", "yes", "no", "no", "no", "yes", "no",
            "no", "no", "no", "no", "no", "yes", "no", "no", "no", "no", "yes", "no", "no", "yes", "no", "no",
            "yes", "yes", "no", "no", "no", "no", "yes", "yes", "no", "no", "no", "yes", "no"]

    # "flag contains red?" 12
    Q_15 = ["yes", "yes", "yes", "yes", "yes", "no", "yes", "yes", "yes", "no", "yes", "yes", "yes", "no", "yes", "yes",
            "no","yes", "yes", "yes", "yes", "yes", "yes", "yes", "yes", "yes", "yes", "yes", "no", "yes", "yes", "no",
            "yes", "yes", "yes", "yes", "yes", "yes", "yes", "yes", "yes", "yes", "yes", "yes", "yes"]

    # "flag contains blue?"
    Q_16 = ["no", "yes", "yes", "no", "no", "no", "no", "yes", "no", "yes", "no", "no", "no", "yes", "no", "no", "yes",
            "no","no", "yes", "no", "yes", "no", "yes", "no", "yes", "yes", "no", "no", "yes", "no", "no", "no", "yes",
            "no","no", "no", "no", "yes", "no", "no", "no", "yes", "no", "no"]

    # "flag contains green?"
    Q_17 = ["yes", "no", "yes", "no", "yes", "no", "no", "no", "no", "yes", "no", "yes", "yes", "no", "no", "yes",
            "no","yes","no", "no", "yes", "no", "yes", "no", "yes", "no", "no", "yes", "yes", "no", "no", "yes", "no",
            "no", "yes","yes","yes", "yes", "no", "no", "yes", "yes", "yes", "no", "no", ]

    # "flag contains yellow?"
    Q_18 = ["no", "yes", "no", "no", "no", "yes", "yes", "no", "yes", "no", "no", "no", "no", "no", "no", "no", "yes",
            "no", "yes","no", "no", "yes", "no", "yes", "yes", "no", "no", "no", "no", "yes", "no", "no", "no", "no",
            "yes", "no","no", "yes","no", "yes", "no", "no", "no", "yes", "no"]

    # "island?"
    Q_12 = ["no", "no", "no", "no", "no", "no", "yes", "no", "no", "no", "yes", "no", "no", "no", "yes", "no", "no",
            "no", "no", "no", "no","yes", "yes", "no", "no", "no", "no", "no", "no", "yes", "no", "no", "yes", "no",
            "yes", "no", "no", "no","no", "yes","no", "no", "no", "no", "no"]

    # "star on the flag?"
    Q_19 = ["no", "no", "yes", "no", "no", "no", "no", "no", "yes", "no", "no", "no", "no", "yes", "no", "yes", "no",
            "no", "no","no", "no", "no", "no", "no", "yes", "no", "yes", "no", "yes", "no", "no", "no", "yes", "no",
            "no", "no","yes", "yes","no", "yes", "yes", "no", "yes", "yes", "no"]

    # "moon on the flag?"
    Q_20 = ["no", "no", "yes", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no",
            "no","no", "no", "yes", "yes", "no", "no", "no", "no", "no", "yes", "no", "no", "no", "yes", "no", "no",
            "no","no","no", "no", "no", "yes", "no", "yes", "no", "no"]

    # "circled object or sun on the flag?"
    Q_21 = ["no", "no", "no", "no", "yes", "no", "no", "no", "no", "yes", "no", "no", "no", "no", "yes", "no", "yes",
            "no","yes", "yes", "no", "no", "no", "no", "no", "no", "yes", "no", "no", "yes", "no", "no", "no", "yes",
            "no","no","no", "no", "no", "no", "no", "no", "no", "no", "no"]
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
    AFRICA = ["Algeria", "Angola", "Benin", "Botswana", "Burkina Faso", "Burundi", "Cabo Verde", "Cameroon",
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
     "Zambia", "Zimbabwe"]
    # "Pop over 5m?"
    Q_3 = ["yes", "yes", "yes", "no", "yes", "yes", "no", "yes", "no", "yes", "no", "yes", "yes", "no", "yes", "yes",
           "no", "no", "no", "yes","no", "no", "yes", "yes", "no", "yes", "no", "yes", "yes", "yes", "yes", "yes", "no",
           "no", "yes", "yes","no", "yes", "yes", "yes","no", "yes", "no", "yes", "yes", "yes", "yes", "yes", "yes",
           "yes", "yes", "yes", "yes", "yes"]

    # "Pop over 10m?"
    Q_2 = ["yes", "yes", "yes", "no", "yes", "yes", "no", "yes", "no", "yes", "no", "no", "yes", "no", "yes", "yes",
           "no"
        , "no", "no", "yes",
           "no", "no", "yes", "yes", "no", "yes", "no", "no", "no", "yes", "yes", "yes", "no", "no", "yes", "yes", "no"
        , "yes", "yes", "yes",
           "no", "yes", "no", "no", "yes", "yes", "yes", "yes", "yes", "no", "yes", "yes", "yes", "yes"]

    # "Pop over 30m?"
    Q_1 = ["yes", "yes", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "yes", "yes", "no",
           "no"
        , "no", "yes", "no",
           "no", "yes", "no", "no", "yes", "no", "no", "no", "no", "no", "no", "no", "no", "yes", "yes", "no", "no",
           "yes"
        , "no", "no", "no",
           "no", "no", "no", "yes", "no", "yes", "yes", "no", "no", "yes", "no", "no"]

    # "Island ?"
    Q_8 = ["no", "no", "no", "no", "no", "no", "yes", "no", "no", "no", "yes", "no", "no", "no", "no", "no", "no", "no"
        , "no", "no", "no", "no",
           "no", "no", "no", "no", "no", "no", "no", "yes", "no", "no", "no", "yes", "no", "no", "no", "no", "no", "no"
        , "yes", "no", "yes",
           "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no"]

    # "french ?"
    Q_4 = ["no", "no", "yes", "no", "yes", "yes", "no", "yes", "yes", "yes", "yes", "yes", "yes", "yes", "yes", "no",
           "yes"
        , "no",
           "no", "no", "yes", "no", "no", "yes", "no", "no", "no", "no", "no", "yes", "no", "yes", "no", "no", "no",
           "no"
        , "no", "yes",
           "no", "yes", "no", "yes", "yes", "no", "no", "no", "no", "no", "no", "yes", "no", "no", "no", "no"]

    # "english?"
    Q_5 = ["no", "no", "no", "yes", "no", "yes", "no", "yes", "no", "no", "no", "no", "no", "no", "no", "no", "no",
           "yes"
        , "yes",
           "no", "no", "yes", "yes", "no", "no", "yes", "yes", "yes", "no", "no", "yes", "no", "no", "yes", "no", "no"
        , "yes",
           "no", "yes", "yes", "no", "no", "yes", "yes", "no", "yes", "yes", "yes", "yes", "no", "no", "yes", "yes",
           "yes"]

    # "arabic?"

    Q_6 = ["yes", "no", "no", "no", "no", "no", "no", "no", "no", "yes", "yes", "no", "no", "yes", "no", "yes", "no",
           "yes"
        , "no",
           "no", "no", "no", "no", "no", "no", "no", "no", "no", "yes", "no", "no", "no", "yes", "no", "yes", "no", "no"
        , "no",
           "no", "no", "no", "no", "no", "no", "yes", "no", "no", "yes", "no", "no", "yes", "no", "no", "no"]

    # "portuguese"
    Q_7 = ["no", "yes", "no", "no", "no", "no", "yes", "no", "no", "no", "no", "no", "no", "no", "no", "no", "yes", "no"
        , "no", "no",
           "no", "no", "no", "no", "yes", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "yes", "no", "no"
        , "no", "no",
           "yes", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", ]

    # "flag contains 3 or more color"
    Q_13 = ['yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes',
           'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes',
           'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'no', 'yes', 'yes', 'yes', 'no', 'yes', 'yes', 'yes',
           'yes', 'yes', 'no', 'yes', 'yes', 'yes', 'yes', 'yes', 'no', 'yes', 'yes', 'yes']

    # "flag contains red?"
    Q_14 = ["yes", "yes", "yes", "no", "yes", "yes", "yes", "yes", "yes", "yes", "yes", "yes", "no", "yes", "yes", "yes"
        , "yes",
            "yes", "yes", "yes", "no", "yes", "yes", "yes", "yes", "yes", "no", "yes", "yes", "yes", "yes", "yes", "yes"
        , "yes",
            "yes", "yes", "yes", "no", "no", "no", "yes", "yes", "yes", "no", "no", "yes", "yes", "yes", "no", "yes",
            "yes",
            "yes", "yes", "yes", ]

    # "flag contains blue?"
    Q_15 = ["no", "no", "no", "yes", "no", "no", "yes", "no", "yes", "yes", "yes", "no", "no", "yes", "yes", "no", "yes"
        , "yes",
            "yes", "yes", "yes", "yes", "no", "no", "no", "no", "yes", "yes", "no", "no", "no", "no", "no", "yes", "no"
        , "no",
            "yes", "no", "no", "yes", "no", "no", "yes", "yes", "yes", "yes", "yes", "no", "yes", "no", "no", "no", "no"
        , "no", ]

    # "flag contains green?"
    Q_16 = ["yes", "no", "yes", "no", "yes", "yes", "no", "yes", "yes", "no", "yes", "yes", "yes", "yes", "no", "no",
            "yes"
        , "yes",
            "no", "yes", "yes", "yes", "yes", "yes", "yes", "yes", "yes", "no", "yes", "yes", "yes", "yes", "yes", "yes"
        , "no",
            "yes", "yes", "yes", "yes", "yes", "yes", "yes", "yes", "yes", "no", "yes", "yes", "yes", "yes", "yes", "no"
        , "no",
            "yes", "yes"]

    # "flag contains yellow?"
    Q_17 = ["no", "yes", "yes", "no", "yes", "no", "no", "yes", "yes", "yes", "yes", "yes", "no", "no", "yes", "yes",
            "no"
        , "yes", "yes", "yes", "yes", "no", "yes", "yes", "yes", "no", "no", "no", "no", "no", "no", "yes", "yes",
            "yes", "no", "yes", "yes", "no", "no", "yes", "yes", "yes", "yes", "no", "no", "yes", "yes", "no", "yes",
            "yes", "no", "yes", "no", "yes"]

    # "Dominant Religion Muslim?"
    Q_9 = ["yes", "no", "no", "no", "yes", "no", "no", "no", "no", "yes", "yes", "no", "yes", "yes", "no", "yes", "no"
        , "no", "no", "no", "no", "yes", "no", "yes", "yes", "no", "no", "no", "yes", "no", "no", "yes", "yes", "no",
            "yes", "no", "no", "yes", "yes", "no", "no", "yes", "no", "yes", "yes", "no", "no", "yes", "no", "no",
            "yes",
            "no", "no", "no"]

    # "Dominant Religion Christian?"
    Q_10 = ['no', 'yes', 'yes', 'yes', 'no', 'yes', 'yes', 'yes', 'yes', 'no', 'no', 'yes', 'no', 'no', 'yes',
            'no', 'yes', 'yes', 'yes', 'yes', 'yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'yes', 'no', 'yes',
            'yes', 'no', 'no', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'yes', 'no', 'no',
            'yes', 'yes', 'no', 'yes', 'yes', 'no', 'yes', 'yes', 'yes']

    # "touches atlantic ocean?(including mediterranen sea)"
    Q_11 = ["yes", "yes", "yes", "no", "no", "no", "yes", "yes", "no", "no", "no", "yes", "yes", "no", "yes", "yes",
            "yes"
        , "no", "no", "no", "yes", "yes", "yes", "yes", "yes", "no", "no", "yes", "yes", "no", "no", "no", "yes", "no",
            "yes", "no", "yes", "no", "yes", "no", "yes", "yes", "no", "yes", "no", "yes", "no", "no", "no", "yes",
            "yes",
            "no", "no", "no"]

    # "countries touching indian ocean?(including the red sea,arabian sea")
    Q_12 = ['no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'yes', 'no', 'no', 'yes',
            'no', 'yes', 'no', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'yes', 'no', 'no',
            'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'yes', 'no', 'no', 'no', 'no', 'no', 'no',
            'yes', 'no', 'yes', 'yes', 'no', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no']

    # "star on your flag?"
    Q_18 = ["yes", "yes", "no", "no", "yes", "yes", "yes", "yes", "yes", "no", "yes", "no", "no", "yes", "yes",
            "no", "no", "no", "no", "yes", "no", "no", "yes", "no", "yes", "no", "no", "yes", "yes", "no", "no",
            "no", "yes", "no", "yes", "yes", "no", "no", "no", "no", "yes", "yes", "no", "no", "yes", "no",
            "yes", "no", "no", "yes", "yes", "no", "no", "yes"]
    # "moon on the flag?"
    Q_19 = ["yes", "no", "no", "no", "no", "no", "no", "no", "no", "no", "yes", "no", "no", "no", "no", "no",
            "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "yes", "no", "no", "no",
            "yes", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no",
            "no", "no", "yes", "no", "no", "no", ]
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
    NORTH_AMERICA = ["Antigua and Barbuda", "Bahamas", "Barbados", "Belize", "Canada", "Costa Rica", "Cuba",
     "Dominica", "Dominican Republic", "El Salvador", "Grenada", "Guatemala", "Haiti",
     "Honduras", "Jamaica", "Mexico", "Nicaragua", "Panama", "Saint Kitts and Nevis",
     "Saint Lucia", "St. Vincent and Grenadines", "Trinidad and Tobago",
     "United States of America"]
    # "pop over 5m"
    Q_3 = ["no", "no", "no", "no", "yes", "yes", "yes", "no", "yes", "yes", "no", "yes", "yes", "yes", "no", "yes",
           "yes", "no", "no", "no", "no", "no", "yes"]

    # "pop over 10m"
    Q_2 = ['no', 'no', 'no', 'no', 'yes', 'no', 'yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no',
           'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'yes']
    # "pop over 30m"
    Q_1 = ['no', 'no', 'no', 'no', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no',
           'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'yes']
    # "spanish?"
    Q_4 = ["no", "no", "no", "no", "no", "yes", "yes", "no", "yes", "yes", "no", "yes", "no", "yes", "no",
           "yes", "yes", "yes", "no", "no", "no", "no", "no"]

    # "english?"
    Q_5 = ["yes", "yes", "yes", "yes", "yes", "no", "no", "yes", "no", "no", "yes", "no", "no", "no", "yes",
           "no", "no", "no", "yes", "yes", "yes", "yes", "yes"]

    # "flag contains red?"
    Q_8 = ["yes", "no", "no", "yes", "yes", "yes", "yes", "yes", "yes", "no", "yes", "no", "yes", "no", "no",
           "yes", "no", "yes", "yes", "no", "no", "yes", "yes", ]

    # "Flag contains blue?"
    Q_9 = ["yes", "yes", "yes", "yes", "no", "yes", "yes", "no", "yes", "yes", "no", "yes", "yes", "yes",
           "no", "no", "yes", "yes", "no", "yes", "yes", "no", "yes"]

    # "flag contains yellow?"
    Q_10 = ["yes", "yes", "yes", "no", "no", "no", "no", "yes", "no", "no", "yes", "no", "no", "no", "yes", "no",
           "no", "no", "yes", "yes", "yes", "no", "no"]

    # "flag contains green?"
    Q_11 = ["no", "no", "no", "no", "no", "no", "no", "yes", "no", "no", "yes", "no", "no", "no", "yes", "yes", "no",
           "no", "yes", "no", "yes", "no", "no"]

    # "flag contains star?"
    Q_13 = ["no", "no", "no", "no", "no", "no", "yes", "no", "no", "no", "yes", "no", "no", "yes", "no", "no", "no",
            "yes", "yes", "no", "no", "no", "yes"]

    # "flag contains black?"
    Q_12 = ["yes", "yes", "no", "no", "no", "no", "no", "yes", "no", "no", "no", "no", "no", "no", "yes", "no",
            "no", "no", "yes", "yes", "no", "yes", "no"]

    # "country touches atlantic ocean?"
    Q_6 = ["yes", "yes", "yes", "yes", "yes", "yes", "yes", "yes", "yes", "no", "yes", "yes", "yes", "yes", "yes",
            "yes",
            "yes", "yes", "yes", "yes", "yes", "yes", "yes"]

    # "country touching pacific ocean?"
    Q_7 = ["no", "no", "no", "no", "yes", "yes", "no", "no", "no", "yes", "no", "yes", "no", "no", "no", "yes",
            "yes", "yes", "no", "no", "no", "no", "yes"]
    dict_json = {}
    for k in range(0, len(Countries)):
        dict_question = {}
        for j in range(0, len(Questions)):
            dict_question[Questions[j]] = locals()[f"Q_{j + 1}"][k]
        dict_json[Countries[k]] = dict_question

    json_file = json.dumps(dict_json, indent=4)
    with open(filename, "w", encoding='utf-8') as f:
        return f.write(json_file)




def create_json_south(filename, Questions, Countries):
    SOUTH_AMERICA = ["Argentina", "Bolivia", "Brazil", "Chile", "Colombia", "Ecuador", "Guyana", "Paraguay",
     "Peru", "Suriname", "Uruguay", "Venezuela"]
    # "Speaks Spanish ?"
    Q_4 = ["yes", "yes", "no", "yes", "yes", "yes", "no", "yes", "yes", "no", "yes", "yes"]

    # "Amazon forest in your country ?"

    Q_5 = ["no", "yes", "yes", "no", "yes", "yes", "yes", "no", "yes", "yes", "no", "yes"]

    # "Population over 5m?

    Q_3 = ["yes", "yes", "yes", "yes", "yes", "yes", "no", "yes", "yes", "no", "no", "yes"]

    # "Pop over 10m? "

    Q_2 = ["yes", "yes", "yes", "yes", "yes", "yes", "no", "no", "yes", "no", "no", "yes"]

    # "Pop over 30m?

    Q_1 = ["yes", "no", "yes", "no", "yes", "no", "no", "no", "yes", "no", "no", "no"]

    # "Touch atlantic ocean ?"

    Q_6 = ["yes", "no", "yes", "yes", "yes", "no", "yes", "no", "no", "yes", "yes", "yes"]

    # "Touch pacific ocean?"

    Q_7 = ["no", "no", "no", "yes", "yes", "yes", "no", "no", "yes", "no", "no", "no"]

    # "Flag contains red? "

    Q_8 = ["no", "yes", "no", "yes", "yes", "yes", "yes", "yes", "yes", "yes", "no", "yes"]

    # "Flag contains Blue?"

    Q_9 = ["yes", "no", "yes", "yes", "yes", "yes", "no", "yes", "no", "no", "yes", "yes"]

    # "Flag contains Green?"

    Q_10 = ["no", "yes", "yes", "no", "no", "no", "yes", "no", "no", "yes", "no", "no"]

    # "star on your flag?"
    Q_11 = ["no", "no", "no", "yes", "no", "no", "no", "no", "no", "yes", "no", "yes"]

    # "cicrle or sun on your flag?"
    Q_12 = ["yes", "no", "yes", "no", "no", "no", "no", "yes", "no", "no", "yes", "no",]
    dict_json = {}
    for k in range(0, len(Countries)):
        dict_question = {}
        for j in range(0, len(Questions)):
            dict_question[Questions[j]] = locals()[f"Q_{j + 1}"][k]
        dict_json[Countries[k]] = dict_question

    json_file = json.dumps(dict_json, indent=4)
    with open(filename, "w", encoding='utf-8') as f:
        return f.write(json_file)


def create_json_oceany(filename, Questions, Countries):
    """Creates a json file for the oceany contient."""
    OCEANIA = ["Australia", "Fiji", "Kiribati", "Marshall Islands", "Micronesia", "Nauru", "New Zealand", "Palau",
     "Papua New Guinea", "Samoa", "Solomon Islands", "Tonga", "Tuvalu", "Vanuatu"]
    # "pop over 1 million?" 2
    Q_2 = ["yes", "no", "no", "no", "no", "no", "yes", "no", "yes", "no", "no", "no", "no", "no"]

    # "flag contains red?" 6
    Q_5 = ["yes", "yes", "yes", "no", "no", "no", "yes", "no", "yes", "yes", "no", "yes", "yes", "yes"]

    # "flag contains blue?" 4
    Q_4 = ["yes", "yes", "yes", "yes", "yes", "yes", "yes", "yes", "no", "yes", "yes", "no", "yes", "no"]

    # "flag contains yellow?" 7
    Q_6 = ["no", "no", "yes", "no", "no", "yes", "no", "yes", "yes", "no", "yes", "no", "yes", "yes"]

    # "flag contains stars?" 5
    Q_7 = ["yes", "no", "no", "no", "yes", "yes", "yes", "no", "yes", "yes", "yes", "no", "yes", "no", ]

    # "flag contains green?" 3
    Q_3 = ["no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "yes", "no", "no", "yes"]

    # "pop over 10m?" 1
    Q_1 = ["yes", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", ]
    dict_json = {}
    for k in range(0, len(Countries)):
        dict_question = {}
        for j in range(0, len(Questions)):
            dict_question[Questions[j]] = locals()[f"Q_{j + 1}"][k]
        dict_json[Countries[k]] = dict_question

    json_file = json.dumps(dict_json, indent=4)
    with open(filename, "w", encoding='utf-8') as f:
        return f.write(json_file)
