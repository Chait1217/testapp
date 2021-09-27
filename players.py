
Players = ['FAN Zhendong', 'XU Xin', 'MA Long', 'LIN Gaoyuan', 'HARIMOTO Tomokazu', 'CALDERANO Hugo',
           'LIN Yun-Ju', 'FALCK Mattias', 'LIANG Jingkun', 'BOLL Timo', 'JANG Woojin', 'OVTCHAROV Dimitrij',
           'JEOUNG Youngsik', 'WANG Chuqin', 'PITCHFORD Liam', 'FRANZISKA Patrick', 'NIWA Koki', 'MIZUTANI Jun',
           'WONG Chun Ting', 'GAUZY Simon', 'ARUNA Quadri', 'LEE Sangsu', 'ZHAO Zihao', 'GARDOS Robert',
           'FREITAS Marcos', 'CHUANG Chih-Yuan', 'SAMSONOV Vladimir', 'JHA Kanak', 'KARLSSON Kristian',
           'GROTH Jonathan', 'JORGIC Darko', 'ACHANTA Sharath Kamal', 'PUCAR Tomislav', 'WANG Yang',
           'UDA Yukiya', 'TSUBOI Gustavo', 'GNANASEKARAN Sathiyan', 'DUDA Benedikt', 'AN Jaehyun',
           'LEBESSON Emmanuel', 'ASSAR Omar', 'FILUS Ruwen', 'PERSSON Jon', 'HABESOHN Daniel',
           'JIN Takuya', 'GERASSIMENKO Kirill', 'GACINA Andrej', 'MORIZONO Masataka', 'GIONIS Panagiotis',
           'SALEH Ahmed', 'SIRUCEK Pavel', 'YOSHIMURA Kazuhiro', 'QIU Dang', 'KOU Lei', 'SKACHKOV Kirill',
           'APOLONIA Tiago', 'DRINKHALL Paul', 'KALLBERG Anton', 'ISHIY Vitor', 'IONESCU Ovidiu', 'MAJOROS Bence',
           'AGUIRRE Marcelo', 'OIKAWA Mizuki', 'ROBLES Alvaro', 'DYJAS Jakub', 'YOSHIMURA Maharu', 'TOKIC Bojan',
           'PISTEJ Lubomir', 'CHEN Chien-An', 'DIAW Ibrahima', 'LIM Jonghoon', 'NUYTINCK Cedric', 'ALAMIYAN Noshad',
           'DESAI Harmeet', 'CIFUENTES Horacio', 'MADRID Marcos', 'MINO Alberto', 'CHO Seungmin', 'AKKUZU Can',
           'MONTEIRO Joao', 'LIND Anders', 'BADOWSKI Marek', 'SHIBAEV Alexander', 'MONTEIRO Thiago', 'PLETEA Cristian',
           'OLAH Benedek', 'FEGERL Stefan', 'JOUTI Eric', 'WALTHER Ricardo', 'KOJIC Frane', 'AFANADOR Brian',
           'OMOTAYO Olajide', 'JANCARIK Lubomir', 'GERALDO Joao', 'LAM Siu Hang', 'WALKER Samuel', 'HIRANO Yuki',
           'ALTO Gaston', 'ANTHONY Amalraj', 'XU Chenhao']

Europe = ['FALCK Mattias','BOLL Timo','OVTCHAROV Dimitrij','PITCHFORD Liam','FRANZISKA Patrick',
          'GAUZY Simon','GARDOS Robert','FREITAS Marcos','SAMSONOV Vladimir','KARLSSON Kristian',
          'GROTH Jonathan','JORGIC Darko','PUCAR Tomislav','WANG Yang','DUDA Benedikt','LEBESSON Emmanuel',
          'FILUS Ruwen','PERSSON Jon','HABESOHN Daniel','GACINA Andrej','GIONIS Panagiotis',
          'SIRUCEK Pavel','QIU Dang', 'KOU Lei', 'SKACHKOV Kirill','APOLONIA Tiago',
          'DRINKHALL Paul', 'KALLBERG Anton','IONESCU Ovidiu', 'MAJOROS Bence',
          'ROBLES Alvaro', 'DYJAS Jakub','TOKIC Bojan','PISTEJ Lubomir','NUYTINCK Cedric',
          'AKKUZU Can','MONTEIRO Joao', 'LIND Anders', 'BADOWSKI Marek', 'SHIBAEV Alexander',
           'PLETEA Cristian','OLAH Benedek', 'FEGERL Stefan','WALTHER Ricardo',
          'KOJIC Frane','JANCARIK Lubomir', 'GERALDO Joao','WALKER Samuel']

Europe_q = ["left handed?","older than 30?","participated in rio 2016 singles or team event?",
            "participated in tokyo 2021 singles or team event?"]



#left handed?
Q_1 = ["no","yes","no","no","no","no","no","yes","no","yes","yes","no","no","no","yes","yes",
       "no","no","no","no","no","no","no","no","no","yes","no","no","no","no","no","no","no",
       "no","yes","no","yes","yes","no","no","no","no","no","no","no","no","yes","no"]
#older than 30
Q_2 = ["no","yes","yes","no","no","no","yes","yes","yes","no","no","no","no","no","no","yes","yes","yes",
       "yes","yes","yes","no","no","yes","yes","yes","yes","no","yes","no","no","no","yes","yes","no",
       "no","yes","no","no","yes","no","yes","yes","no","no","yes","no","no"]

#participated in rio 2016 singles or team event?
Q_3 = ["yes","yes","yes","yes","no","yes","yes","yes","yes","yes","yes","no","no","yes","no","yes",
       "no","no","yes","yes","yes","no","no","yes","no","yes","yes","no","yes","no","no","yes",
       "yes","no","no","no","yes","no","no","yes","no","yes","yes","no","no","no","no","yes"]

#participated in tokyo 2021 singles or team event?
Q_4 = ["yes","yes","yes","yes","yes","yes","yes","yes","no","yes","yes","yes","yes","yes",
       "no","yes","no","no","yes","yes","yes","no","no","yes","yes","yes","yes","yes","yes",
       "yes","yes","no","yes","no","no","no","yes","no","no","no","no","no","no","no",
       "yes","yes","no","no"]




Amercicas = ['CALDERANO Hugo','JHA Kanak','TSUBOI Gustavo','ISHIY Vitor','AGUIRRE Marcelo','CIFUENTES Horacio',
             'MADRID Marcos', 'MINO Alberto','MONTEIRO Thiago','JOUTI Eric','AFANADOR Brian','ALTO Gaston']
Amercicas_q = ["left handed","older than 30 years old","participated in rio 2016 singles or team event?",
               "particpated in olympics 2021 tokyo singles or team event?","is he argentinian?",
               "ranked in the top 30 of the world?","known for his shots with two hands on the racket?",
               "sponsored butterfly?"]
#left handed
Q_1 = ["no","no","yes","no","yes","no","no","no","no","no","no","no"]

# older than 30 years old
Q_2 = ["no","no","yes","no","no","no","yes","yes","yes","no","no","yes"]

# participated in rio 2016 singles or team event?
Q_3 = ["yes","yes","yes","no","yes","no","yes","no","no","no","yes","no"]

# particpated in olympics 2021 tokyo singles or team event?
Q_4 = ["yes","yes","yes","yes","no","yes","no","yes","no","no","yes","yes"]

#is he argentinian?
Q_5 = ["no","no","no","no","no","yes","no","no","no","no","no","yes"]

#ranked in the top 30 of the world?
Q_6 = ["yes","yes","no","no","no","no","no","no","no","no","no","no",]

#known for his shots with two hands on the racket?
Q_7 = ["yes","no","no","no","no","no","no","no","no","no","no","no",]

#sponsored butterfly?
Q_8 = ["no","yes","yes","no","yes","no","no","yes","no","yes","yes","no",]

Africa = ['ARUNA Quadri','ASSAR Omar','SALEH Ahmed','DIAW Ibrahima','OMOTAYO Olajide']
Africa_q = ["older than 30 years?","participated in rio 2016 singles or team event?",
            "particpated in olympics 2021 tokyo singles or team event?",
            "know for his extremely powerful forehand?",
            "reached quarter final in 2021 olympics?",
            "older than 40 years old?","used to represent france when he was under 18?",
            "2nd best player of nigeria?","sponsored butterfly?","sponsor gewo?"]

# older than 30 years
Q_1 = ["yes","no","yes","no","no"]
# participated in rio 2016 singles or team event?
Q_2 = ["yes","yes","no","no","no"]
#particpated in olympics 2021 tokyo singles or team event?
Q_3 = ["yes","yes","no","yes","no"]
#know for his extremely powerful forehand?
Q_4 = ["yes","no","no","no","no",]
#reached quarter final in 2021 olympics?
Q_5 = ["no","yes","no","no","no"]
#older than 40 years old?
Q_6 = ["no","no","yes","no","no",]
#used to represent france when he was under 18?
Q_7 = ["no","no","no","yes","no"]
#2nd best player of nigeria?
Q_8 = ["no","no","no","no","yes"]
#sponsored butterfly?
Q_9 = ["no","yes", "no","no","no"]
#sponsor gewo
Q_10 = ["yes","no","no","no","yes"]



Asia = ['FAN Zhendong', 'XU Xin', 'MA Long', 'LIN Gaoyuan', 'HARIMOTO Tomokazu','LIN Yun-Ju',
        'LIANG Jingkun','JANG Woojin','JEOUNG Youngsik','WANG Chuqin','NIWA Koki', 'MIZUTANI Jun',
        'WONG Chun Ting','LEE Sangsu', 'ZHAO Zihao','CHUANG Chih-Yuan','ACHANTA Sharath Kamal',
        'UDA Yukiya','GNANASEKARAN Sathiyan','AN Jaehyun','JIN Takuya','GERASSIMENKO Kirill','MORIZONO Masataka',
        'YOSHIMURA Kazuhiro','OIKAWA Mizuki',
        'YOSHIMURA Maharu','CHEN Chien-An','LIM Jonghoon','ALAMIYAN Noshad','DESAI Harmeet','CHO Seungmin',
        'LAM Siu Hang','HIRANO Yuki','ANTHONY Amalraj', 'XU Chenhao']

Asia_q = ["left handed?","pen holder?","older than 30 years old","participated in rio 2016 singles or team event?",
          "ever won an olympic medal in singles or in team event?","is he chinese?",
          "particpated in olympics 2021 tokyo singles or team event?","is he korean?",
          "sponsored butterfly?"]

#left handed
Q_1 = ["no","yes","no","yes","no","yes","no","no","no","yes","yes","no","no","no","no","no","no",
       "yes","no","no","no","no","yes","no","no","no","yes","yes","yes","no","yes","no","no","no","no"]
# pen holder
Q_2 = ["no", "yes", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "yes", "no", "yes", "no", "no", "no",
       "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no"]
#older than 30 years old
Q_3 = ["no","yes","yes","no","no","no","no","no","no","no","no","yes","no","yes","no","yes","yes",
       "no","no","no","no","no","no","no","no","no","yes","no","no","no","no","no","no","yes","no"]
# participated in rio 2016 singles or team event?
Q_4 = ["no", "yes", "yes", "no", "no", "no", "no", "no", "yes", "no", "yes", "yes", "yes", "yes", "no", "yes",
       "yes", "no", "no", "no", "no", "yes", "no", "no", "no", "yes", "yes", "no", "yes", "no", "no", "no", "no",
       "no", "no"]
# ever won an olympic medal in singles or in team event?
Q_5 = ["yes", "yes", "yes", "no", "yes", "no", "no", "no", "no", "no", "yes", "yes", "no", "no", "no", "no",
       "no", "no","no",
       "no", "no", "no", "no", "no", "no", "yes", "no", "no", "no", "no", "no", "no", "no", "no", "no"]
# is he chinese?
Q_6 = ["yes", "yes", "yes", "yes", "no", "no", "yes", "no", "no", "yes", "no", "no", "no", "no", "yes", "no", "no",
       "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "yes"]
# particpated in olympics 2021 tokyo singles or team event?
Q_7 = ["yes", "yes", "yes", "no", "yes", "yes", "no", "yes", "yes", "no", "yes", "yes", "yes", "yes", "no", "yes","yes",
       "no", "yes", "no", "no", "yes", "no", "no", "no", "no", "yes", "no", "no", "no", "no", "yes", "no", "no","no"]
#is he korean?
Q_8 = ["no","no","no","no","no","no","no","yes","yes","no","no","no","no","yes","no","no","no","no","no",
       "yes","no","no","no","no","no","no","no","yes","no","no","yes","no","no","no","no"]

#sponsored butterfly?
Q_9 = ["no","no","no","yes","yes","yes","no","no","no","no","no","yes","yes","yes","no","yes","no",
       "yes","yes","no","no","yes","no","no","no","yes","no","no","yes","no","no","no","no","no","no"]







print(len(Asia))
print(len(Q_2))


