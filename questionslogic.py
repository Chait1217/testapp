import json
from kivy.app import App
import main2
import europelogic,oceany_logic,asia_logic,africa_logic,south_america_logic,north_central_logic
import countries_start
from kivy.uix.screenmanager import ScreenManager, Screen
#

class Before:
    #sm = App.get_running_app().root
    Contient = countries_start.countries_list()
    Continent_q = countries_start.countries_question()
    Questions_First = countries_start.start_question()

    def __init__(self):
        self.app = App.get_running_app()
        self.indexchange = 0
        self.index = 0  # 1


    def questionmanager(self):
        ask = self.app.root.ids.third.answer
        if ask == "yes":
            continent_countries = self.Contient[self.indexchange]
            questions_ask = self.Continent_q[self.indexchange]
            if self.indexchange == 5:
                self.results = continent_countries
                main2.create_json_oceany("answers.json", questions_ask, continent_countries)
                with open("answers.json", "r", encoding='utf-8') as f:
                    self.transition(json.loads(f.read()), continent_countries, questions_ask)
            if self.indexchange == 4:
                self.results = continent_countries
                main2.create_json_north("answers.json", questions_ask, continent_countries)
                with open("answers.json", "r", encoding='utf-8') as f:
                    self.transition(json.loads(f.read()), continent_countries, questions_ask)
            if self.indexchange == 3:
                self.results = continent_countries
                main2.create_json_south("answers.json", questions_ask, continent_countries)
                with open("answers.json", "r", encoding='utf-8') as f:
                    self.transition(json.loads(f.read()), continent_countries, questions_ask)
            if self.indexchange == 0:
                self.results = continent_countries
                main2.create_json_europe("answers.json", questions_ask, continent_countries)
                with open("answers.json", "r", encoding='utf-8') as f:
                    self.transition(json.loads(f.read()), continent_countries, questions_ask)
            if self.indexchange == 1:
                self.results = continent_countries
                main2.create_json_asia("answers.json", questions_ask, continent_countries)
                with open("answers.json", "r", encoding='utf-8') as f:
                    self.transition(json.loads(f.read()), continent_countries, questions_ask)
            if self.indexchange == 2:
                self.results = continent_countries
                main2.create_json_africa("answers.json", questions_ask, continent_countries)
                with open("answers.json", "r", encoding='utf-8') as f:
                    self.transition(json.loads(f.read()), continent_countries, questions_ask)
        if ask == "no" or ask == "dnk":
            self.indexchange += 1
            try:
                self.app.root.ids.third.set_question(self.Questions_First[self.indexchange])
            except IndexError:
                self.app.root.ids.third.set_question("Sorry,coudn't guess your country?")
            print(self.app.root.ids.third.index)

    def bienvenu(self):
        self.app.root.ids.third.set_question("Situated in Europe?")

    def transition(self, answers_recieved, continent, questions):
        # print(answers_recieved)
        self.answers = answers_recieved
        self.continent_country = continent
        self.questions_country = questions
        self.app.root.ids.third.set_question(self.questions_country[0])
        self.app.root.ids.third.index += 10
        self.results = self.continent_country

    def get_answeer(self):
        answers = self.answers
        self.Q = self.app.root.ids.third.answer
        set_answer = []
        if self.Q == 'yes' or self.Q == 'no' or self.Q == 'dnk':
            if self.Q == 'dnk':
                set_answer = self.results
            else:
                for country in self.continent_country:
                    if answers[country][self.questions_country[self.index]] == self.Q:
                        set_answer.append(country)
            if len(self.continent_country) == 46:
                europelogic.europe_check(self)
            if len(self.continent_country) == 45:
                asia_logic.asia_logic(self)
            if len(self.continent_country) == 14:
                oceany_logic.oceany_logic(self)
            if len(self.continent_country) == 54:
                africa_logic.africa_logic(self)
            if len(self.continent_country) == 12:
                south_america_logic.south_america_logic(self)
            if len(self.continent_country) == 23:
                north_central_logic.north_central_america_logic(self)

        self.results = set(self.results) & set(set_answer)
        return self.results

    def game_manager(self):
        self.results = self.get_answeer()
        print(self.results)
        if len(self.results) == 1:
            self.displays = list(self.results)
            sm = App.get_running_app().root
            sm.current = "fifth"
            self.app.root.ids.fifth.set_question(self.displays[0])
            #self.app.root.ids.third.set_question(self.displays[0])
        elif len(self.results) == 0:
            self.app.root.ids.third.set_question("Sorry,coudn't guess your country?")
        else:
            self.app.root.ids.third.set_question(self.questions_country[self.index]) #error handling
            print(self.questions_country)
        # self.index += 1
        # self.index1 += 1


if __name__ == '__main__':
    Before()
