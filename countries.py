import json
from kivy.app import App
import main
import json_countries
import europelogic, oceany_logic, asia_logic, africa_logic, south_america_logic, north_central_logic
import countries_start


class Countries:

    def __init__(self):
        self.Contient = countries_start.countries_list()
        self.Continent_q = countries_start.countries_question()
        self.Questions_First = countries_start.start_question()
        self.app = App.get_running_app()
        self.index_question = 0

    def questionmanager(self):
        ask = self.app.root.ids.third.answer
        if ask == "yes":
            continent_countries = self.Contient[self.index_question]
            questions_ask = self.Continent_q[self.index_question]
            if self.index_question == 5:
                self.results = continent_countries
                json_countries.create_json_oceany("answers.json", questions_ask, continent_countries)
                with open("answers.json", "r", encoding='utf-8') as f:
                    self.transition(json.loads(f.read()), continent_countries, questions_ask)
            if self.index_question == 4:
                self.results = continent_countries
                json_countries.create_json_north("answers.json", questions_ask, continent_countries)
                with open("answers.json", "r", encoding='utf-8') as f:
                    self.transition(json.loads(f.read()), continent_countries, questions_ask)
            if self.index_question == 3:
                self.results = continent_countries
                json_countries.create_json_south("answers.json", questions_ask, continent_countries)
                with open("answers.json", "r", encoding='utf-8') as f:
                    self.transition(json.loads(f.read()), continent_countries, questions_ask)
            if self.index_question == 0:
                self.results = continent_countries
                json_countries.create_json_europe("answers.json", questions_ask, continent_countries)
                with open("answers.json", "r", encoding='utf-8') as f:
                    self.transition(json.loads(f.read()), continent_countries, questions_ask)
            if self.index_question == 1:
                self.results = continent_countries
                json_countries.create_json_asia("answers.json", questions_ask, continent_countries)
                with open("answers.json", "r", encoding='utf-8') as f:
                    self.transition(json.loads(f.read()), continent_countries, questions_ask)
            if self.index_question == 2:
                self.results = continent_countries
                json_countries.create_json_africa("answers.json", questions_ask, continent_countries)
                with open("answers.json", "r", encoding='utf-8') as f:
                    self.transition(json.loads(f.read()), continent_countries, questions_ask)
        if ask == "no" or ask == "dnk":
            self.index_question += 1
            try:
                self.app.root.ids.third.set_question(self.Questions_First[self.index_question])
            except IndexError:
                sm = App.get_running_app().root
                sm.current = "fifth"
                self.app.root.ids.fifth.set_question("Sorry,couldn't guess your country.")
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
        self.Q = self.app.root.ids.third.answer
        set_answer = []
        # if self.Q == 'yes' or self.Q == 'no' or self.Q == 'dnk':
        if self.Q == 'dnk':
            set_answer = self.results
        else:
            for country in self.continent_country:
                if self.answers[country][self.questions_country[0]] == self.Q:
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

        self.store_answer = self.results
        self.results = set(self.results) & set(set_answer)
        return self.results

    def game_manager(self):
        self.results = self.get_answeer()
        print(self.results)
        if len(self.results) == 1:
            self.displays = list(self.results)
            sm = App.get_running_app().root
            sm.current = "fifth"
            self.app.root.ids.fifth.set_question("Your guess was: " + self.displays[0])
        elif len(self.results) == 0:
            sm = App.get_running_app().root
            sm.current = "fifth"
            if len(self.store_answer) < 6:
                result_without_quotes1 = ", ".join(list(self.store_answer))
                self.app.root.ids.fifth.set_question("Sorry, couldn't guess your country."
                                                     " These are the possible countries: " + str(
                    result_without_quotes1))
            else:
                sm = App.get_running_app().root
                sm.current = "fifth"
                self.app.root.ids.fifth.set_question("Sorry, couldn't guess your country.")

        else:
            try:
                self.app.root.ids.third.set_question(self.questions_country[0])
            except IndexError:
                if len(self.results) < 6:
                    sm = App.get_running_app().root
                    sm.current = "fifth"
                    result_without_quotes = ", ".join(list(self.results))
                    self.app.root.ids.fifth.set_question("Sorry, couldn't guess your country."
                                                         " These are the possible countries: "
                                                         + str(result_without_quotes))
                else:
                    sm = App.get_running_app().root
                    sm.current = "fifth"
                    self.app.root.ids.fifth.set_question("Sorry, couldn't guess your country.")

    def change_screen(self):
        self.app.root.ids.fourth.index = 1001
        self.app.root.ids.third.index = 0
        main.Advanced.change_screen2(self)

    def change_screen1(self):
        self.app.root.ids.third.index = 0
        self.app.root.ids.fourth.index = 1001
        main.Advanced.change_screen3(self)

    def reset_index(self):
        self.app.root.ids.third.index = 0
        self.app.root.ids.fourth.index = 1001
        print("reset done1")


if __name__ == '__main__':
    Countries()
