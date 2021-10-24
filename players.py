import json
from kivy.app import App
import json_male
import players_start, europe_male_logic, africa_male_logic, asia_male_logic, americas_male_logic


class Players:

    def __init__(self):
        self.app = App.get_running_app()
        self.Contient_Players_Male = players_start.male_players_list()
        self.Male_Players_q = players_start.male_players_question()
        self.Initial_Male_Questions = players_start.start_question()
        self.index_transition = 0
        self.index_male_female = 0

    def male_or_female(self):
        ask1 = self.app.root.ids.fourth.answer
        if ask1 == "yes":
            self.index_male_female = 4
            print("executed11")
            self.app.root.ids.fourth.index = 0
            self.app.root.ids.fourth.set_question1(self.Initial_Male_Questions[0])

        if ask1 == "no":
            self.index_male_female = 8
            self.app.root.ids.fourth.index = 0
            self.app.root.ids.fourth.set_question1(self.Initial_Male_Questions[0])
            # self.questionmanager1()

        if ask1 == "dnk":
            sm = App.get_running_app().root
            sm.current = "fifth"
            self.app.root.ids.fifth.set_question("Sorry,couldn't guess your player.")

    def questionmanager1(self):
        if self.index_male_female == 8:
            # print("man")
            ask = self.app.root.ids.fourth.answer
            if ask == "yes":
                continent_players_male = self.Contient_Players_Male[self.index_transition]
                questions_male = self.Male_Players_q[self.index_transition]
                if self.index_transition == 3:
                    self.results = continent_players_male
                    json_male.create_json_north("answers.json", questions_male, continent_players_male)
                    with open("answers.json", "r", encoding='utf-8') as f:
                        self.transition1(json.loads(f.read()), continent_players_male, questions_male)
                if self.index_transition == 0:
                    self.results = continent_players_male
                    json_male.create_json_europe("answers.json", questions_male, continent_players_male)
                    with open("answers.json", "r", encoding='utf-8') as f:
                        self.transition1(json.loads(f.read()), continent_players_male, questions_male)
                if self.index_transition == 1:
                    self.results = continent_players_male
                    json_male.create_json_asia("answers.json", questions_male, continent_players_male)
                    with open("answers.json", "r", encoding='utf-8') as f:
                        self.transition1(json.loads(f.read()), continent_players_male, questions_male)
                if self.index_transition == 2:
                    self.results = continent_players_male
                    json_male.create_json_africa("answers.json", questions_male, continent_players_male)
                    with open("answers.json", "r", encoding='utf-8') as f:
                        self.transition1(json.loads(f.read()), continent_players_male, questions_male)
            if ask == "no" or ask == "dnk":
                self.index_transition += 1
                try:
                    self.app.root.ids.fourth.set_question1(self.Initial_Male_Questions[self.index_transition])
                except IndexError:
                    sm = App.get_running_app().root
                    sm.current = "fifth"
                    self.app.root.ids.fifth.set_question("Sorry,couldn't guess your player.")
        if self.index_male_female == 4:
            print("women")

    def bienvenu1(self):
        self.app.root.ids.fourth.set_question1("Is your player a woman?")
        # self.app.root.ids.fourth.set_question1("Is your player European?")

    def transition1(self, answers_recieved, continent, questions):
        # print(answers_recieved)
        self.answers = answers_recieved
        self.continent_country = continent
        self.questions_country = questions
        self.app.root.ids.fourth.set_question1(self.questions_country[0])
        self.app.root.ids.fourth.index += 10
        self.results = self.continent_country

    def get_answeer1(self):
        self.Q = self.app.root.ids.fourth.answer
        set_answer = []
        if self.Q == 'dnk':
            set_answer = self.results
        else:
            for country in self.continent_country:
                if self.answers[country][self.questions_country[0]] == self.Q:
                    set_answer.append(country)
        if len(self.continent_country) == 48:
            europe_male_logic.europe_male_check(self)
        if len(self.continent_country) == 35:
            asia_male_logic.asia_male_check(self)
        if len(self.continent_country) == 5:
            africa_male_logic.africa_male_check(self)
        if len(self.continent_country) == 12:
            americas_male_logic.americas_male_check(self)

        self.store_answer = self.results
        self.results = set(self.results) & set(set_answer)
        return self.results

    def game_manager1(self):

        self.results = self.get_answeer1()
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
                self.app.root.ids.fifth.set_question("Sorry, couldn't guess your player."
                                                     " These are the possible players: " + str(
                    result_without_quotes1))
            else:
                sm = App.get_running_app().root
                sm.current = "fifth"
                self.app.root.ids.fifth.set_question("Sorry, couldn't guess your player.")
        else:
            try:
                self.app.root.ids.fourth.set_question1(self.questions_country[0])
            except IndexError:
                if len(self.results) < 6:
                    sm = App.get_running_app().root
                    sm.current = "fifth"
                    result_without_quotes = ", ".join(list(self.results))
                    self.app.root.ids.fifth.set_question("Sorry,couldn't guess your player."
                                                         " These are the possible players: "
                                                         + str(result_without_quotes))
                else:
                    sm = App.get_running_app().root
                    sm.current = "fifth"
                    self.app.root.ids.fifth.set_question("Sorry,couldn't guess your player.")
