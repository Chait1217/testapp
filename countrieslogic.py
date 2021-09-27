import json
from kivy.app import App
import main3

class Countries:
    Contient_Players = [['FALCK Mattias','BOLL Timo','OVTCHAROV Dimitrij','PITCHFORD Liam','FRANZISKA Patrick',
          'GAUZY Simon','GARDOS Robert','FREITAS Marcos','SAMSONOV Vladimir','KARLSSON Kristian',
          'GROTH Jonathan','JORGIC Darko','PUCAR Tomislav','WANG Yang','DUDA Benedikt','LEBESSON Emmanuel',
          'FILUS Ruwen','PERSSON Jon','HABESOHN Daniel','GACINA Andrej','GIONIS Panagiotis',
          'SIRUCEK Pavel','QIU Dang', 'KOU Lei', 'SKACHKOV Kirill','APOLONIA Tiago',
          'DRINKHALL Paul', 'KALLBERG Anton','IONESCU Ovidiu', 'MAJOROS Bence',
          'ROBLES Alvaro', 'DYJAS Jakub','TOKIC Bojan','PISTEJ Lubomir','NUYTINCK Cedric',
          'AKKUZU Can','MONTEIRO Joao', 'LIND Anders', 'BADOWSKI Marek', 'SHIBAEV Alexander',
           'PLETEA Cristian','OLAH Benedek', 'FEGERL Stefan','WALTHER Ricardo',
          'KOJIC Frane','JANCARIK Lubomir', 'GERALDO Joao','WALKER Samuel'],['FAN Zhendong', 'XU Xin', 'MA Long', 'LIN Gaoyuan', 'HARIMOTO Tomokazu','LIN Yun-Ju',
        'LIANG Jingkun','JANG Woojin','JEOUNG Youngsik','WANG Chuqin','NIWA Koki', 'MIZUTANI Jun',
        'WONG Chun Ting','LEE Sangsu', 'ZHAO Zihao','CHUANG Chih-Yuan','ACHANTA Sharath Kamal',
        'UDA Yukiya','GNANASEKARAN Sathiyan','AN Jaehyun','JIN Takuya','GERASSIMENKO Kirill','MORIZONO Masataka',
        'YOSHIMURA Kazuhiro','OIKAWA Mizuki',
        'YOSHIMURA Maharu','CHEN Chien-An','LIM Jonghoon','ALAMIYAN Noshad','DESAI Harmeet','CHO Seungmin',
        'LAM Siu Hang','HIRANO Yuki','ANTHONY Amalraj', 'XU Chenhao'],['ARUNA Quadri','ASSAR Omar','SALEH Ahmed','DIAW Ibrahima','OMOTAYO Olajide'],
                        ['CALDERANO Hugo', 'JHA Kanak', 'TSUBOI Gustavo', 'ISHIY Vitor', 'AGUIRRE Marcelo',
                         'CIFUENTES Horacio',
                         'MADRID Marcos', 'MINO Alberto', 'MONTEIRO Thiago', 'JOUTI Eric', 'AFANADOR Brian',
                         'ALTO Gaston']]

    Continent_q = [["left handed?","older than 30?","participated in rio 2016 singles or team event?",
            "participated in tokyo 2021 singles or team event?"],["left handed?","pen holder?","older than 30 years old","participated in rio 2016 singles or team event?",
          "ever won an olympic medal in singles or in team event?","is he chinese?",
          "particpated in olympics 2021 tokyo singles or team event?","is he korean?",
          "sponsored butterfly?"],["older than 30 years?","participated in rio 2016 singles or team event?",
            "particpated in olympics 2021 tokyo singles or team event?",
            "know for his extremely powerful forehand?",
            "reached quarter final in 2021 olympics?",
            "older than 40 years old?","used to represent france when he was under 18?",
            "2nd best player of nigeria?","sponsored butterfly?","sponsor gewo?"],
                   ["left handed", "older than 30 years old", "participated in rio 2016 singles or team event?",
                    "particpated in olympics 2021 tokyo singles or team event?", "is he argentinian?",
                    "ranked in the top 30 of the world?", "known for his shots with two hands on the racket?",
                    "sponsored butterfly?"]]


    Questions_First = ["Is he European", "Is he Asian?", "Is he African?",
                       "Does he come from north or south America?"]

    def __init__(self):
        self.app = App.get_running_app()
        self.indexchange = 0
        self.index1 = 0
        self.index = 1

    def questionmanager1(self):
        ask = self.app.root.ids.fourth.answer
        if ask == "yes":
            continent_countries = self.Contient_Players[self.indexchange]
            questions_ask = self.Continent_q[self.indexchange]
            if self.indexchange == 3:
                self.results = continent_countries
                main3.create_json_north("answers.json", questions_ask, continent_countries)
                with open("answers.json", "r", encoding='utf-8') as f:
                    self.transition1(json.loads(f.read()), continent_countries, questions_ask)
            if self.indexchange == 0:
                self.results = continent_countries
                main3.create_json_europe("answers.json", questions_ask, continent_countries)
                with open("answers.json", "r", encoding='utf-8') as f:
                    self.transition1(json.loads(f.read()), continent_countries, questions_ask)
            if self.indexchange == 1:
                self.results = continent_countries
                main3.create_json_asia("answers.json", questions_ask, continent_countries)
                with open("answers.json", "r", encoding='utf-8') as f:
                    self.transition1(json.loads(f.read()), continent_countries, questions_ask)
            if self.indexchange == 2:
                self.results = continent_countries
                main3.create_json_africa("answers.json", questions_ask, continent_countries)
                with open("answers.json", "r", encoding='utf-8') as f:
                    self.transition1(json.loads(f.read()), continent_countries, questions_ask)
        if ask == "no" or ask == "dnk":
            self.indexchange += 1
            try:
                self.app.root.ids.fourth.set_question1(self.Questions_First[self.indexchange])
            except IndexError:
                self.app.root.ids.fourth.set_question1("Sorry,coudn't guess your country?")
            print(self.app.root.ids.third.index)

    def bienvenu1(self):
        self.app.root.ids.fourth.set_question1("Is he European")

    def transition1(self, answers_recieved, continent, questions):
        # print(answers_recieved)
        self.answers = answers_recieved
        self.continent_country = continent
        self.questions_country = questions
        self.app.root.ids.fourth.set_question1(self.questions_country[0])
        self.app.root.ids.fourth.index += 10
        self.results = self.continent_country

    def get_answeer1(self):
        answers = self.answers
        Q = self.app.root.ids.fourth.answer
        set_answer = []
        if Q == 'yes' or Q == 'no' or Q == 'dnk':
            if Q == 'dnk':
                set_answer = self.results
            else:
                for country in self.continent_country:
                    if answers[country][self.questions_country[self.index1]] == Q:
                        set_answer.append(country)

        self.results = set(self.results) & set(set_answer)
        return self.results

    def game_manager1(self):
        self.results = self.get_answeer1()
        print(self.results)

        if len(self.results) == 1:
            self.displays = list(self.results)
            self.app.root.ids.fourth.set_question1(self.displays[0])
        elif len(self.results) == 0:
            self.app.root.ids.fourth.set_question1("Sorry,coudn't guess your country?")
        else:
            self.app.root.ids.fourth.set_question1(self.questions_country[self.index])
        self.index += 1
        self.index1 += 1
