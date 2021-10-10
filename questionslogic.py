import json
from kivy.app import App
import main
import main2
import europelogic, oceany_logic, asia_logic, africa_logic, south_america_logic, north_central_logic
import countries_start
from kivy.uix.screenmanager import ScreenManager, Screen


class Before:

    def __init__(self):
        self.Contient = countries_start.countries_list()
        self.Continent_q = countries_start.countries_question()
        self.Questions_First = countries_start.start_question()
        self.app = App.get_running_app()
        self.indexchange = 0
        self.index2 = 0  # 1

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
            # print(self.indexchange + 1000)
            try:
                self.app.root.ids.third.set_question(self.Questions_First[self.indexchange])
            except IndexError:
                self.app.root.ids.third.set_question("Sorry,coudn't guess your country?")
            # print(self.app.root.ids.third.index)

    def bienvenu(self):
        self.app.root.ids.third.set_question("Is your country situated in Europe?")

    def transition(self, answers_recieved, continent, questions):
        self.answers = answers_recieved
        self.continent_country = continent
        self.questions_country = questions
        self.app.root.ids.third.set_question(self.questions_country[0])
        self.app.root.ids.third.index += 10
        print(self.app.root.ids.third.index)
        self.results = self.continent_country
        # print(self.answers)
        # print(self.questions_country)

    def get_answeer(self):
        # self.answers1 = self.answers
        self.Q = self.app.root.ids.third.answer
        set_answer = []
        if self.Q == 'yes' or self.Q == 'no' or self.Q == 'dnk':
            if self.Q == 'dnk':
                set_answer = self.results
            else:
                for country in self.continent_country:
                    if self.answers[country][self.questions_country[self.index2]] == self.Q:
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
            # self.app.root.ids.third.set_question(self.displays[0])
        elif len(self.results) == 0:
            sm = App.get_running_app().root
            sm.current = "fifth"
            self.app.root.ids.fifth.set_question("Sorry,coudn't guess your country?")
        else:
            try:
                self.app.root.ids.third.set_question(self.questions_country[self.index2])
            except IndexError:
                sm = App.get_running_app().root
                sm.current = "fifth"
                self.app.root.ids.fifth.set_question("Sorry,coudn't guess your country?" + str(self.results))

    def change_screen(self):
        self.app.root.ids.third.index = 0
        main.Advanced.change_screen2(self)

    def change_screen1(self):
        self.app.root.ids.fourth.index = 0
        main.Advanced.change_screen3(self)

    def reset_index(self):
        self.app.root.ids.third.index = 0
        self.app.root.ids.fourth.index = 0
        print("reset done1")


if __name__ == '__main__':
    Before()
