"""
Table Tennis Players Theme.

Contains all the code to play the game.
"""

from kivy.app import App

import json
import africa_female_logic
import africa_male_logic
import americas_female_logic
import americas_male_logic
import asia_male_logic
import asia_female_logic
import europe_male_logic
import europe_female_logic
import json_male
import json_female
import players_male_start
import players_female_start


class Players:
    """
    Handles the Countries theme main logic and the results.

    ...
    Attributes
    ----------
    app : object
        Instance of the class Akiping.

    contient_players_male : list
        contains a list of all the male players separated by continents.

    male_players_q : list
        contains a list of all the questions for the male players.

    initial_male_questions : list
        contains a list of all the initial questions for the male table tennis players.

    contient_players_female : list
        contains a list of all the female players separated by continents.

    female_players_q : list
        contains a list of all the questions for the female players.

    initial_female_questions : list
        contains a list of all the initial questions for the female table tennis players.

    index_transition : int
        used for changing the questions.

    index_male_female : int
        used for changing checking if the player is a man or women.
    """

    SCREEN_NAME = "fifth"
    RESULT_MESSAGE = "You were thinking of: "
    NOT_FOUND_MESSAGE = "Sorry, couldn't guess your player."
    NOT_FOUND_MESSAGE1 = "Sorry, couldn't guess your player. These are the possible players: "

    def __init__(self):
        self.app = App.get_running_app()
        self.contient_players_male = players_male_start.male_players_list()
        self.male_players_q = players_male_start.male_players_question()
        self.initial_male_questions = players_male_start.start_question()
        self.contient_players_female = players_female_start.female_players_list()
        self.female_players_q = players_female_start.female_players_question()
        self.initial_female_questions = players_female_start.start_question()
        self.index_transition = 0
        self.index_male_female = 0

    def male_or_female(self):
        """Checks if the table tennis player is a man or women."""
        user_answer = self.app.root.ids.fourth.answer
        if user_answer == "yes":
            self.index_male_female = 4
            print("executed11")
            self.app.root.ids.fourth.index = 0
            self.app.root.ids.fourth.set_question(self.initial_female_questions[0])

        if user_answer == "no":
            self.index_male_female = 8
            print("executed12")
            self.app.root.ids.fourth.index = 0
            self.app.root.ids.fourth.set_question(self.initial_male_questions[0])

        if user_answer == "dnk":
            sm = App.get_running_app().root
            sm.current = self.SCREEN_NAME
            self.app.root.ids.fifth.display_answer(self.NOT_FOUND_MESSAGE)

    def question_manager(self):
        """
        Checks if the player is a man or a women.

        Then, checks in which continent is the user's player and creates the
        json file on the fly, which contains all the attributes of the players.

        Then transfers the information to the transition function.
        """
        if self.index_male_female == 8:
            print("read male")
            user_answer = self.app.root.ids.fourth.answer
            if user_answer == "yes":
                continent_players_male = self.contient_players_male[self.index_transition]
                questions_male = self.male_players_q[self.index_transition]
                if self.index_transition == 3:
                    self.results = continent_players_male
                    json_male.create_json_americas("answers.json", questions_male, continent_players_male)
                    with open("answers.json", "r", encoding='utf-8') as f:
                        self.transition(json.loads(f.read()), continent_players_male, questions_male)
                if self.index_transition == 0:
                    self.results = continent_players_male
                    json_male.create_json_europe("answers.json", questions_male, continent_players_male)
                    with open("answers.json", "r", encoding='utf-8') as f:
                        self.transition(json.loads(f.read()), continent_players_male, questions_male)
                if self.index_transition == 1:
                    self.results = continent_players_male
                    json_male.create_json_asia("answers.json", questions_male, continent_players_male)
                    with open("answers.json", "r", encoding='utf-8') as f:
                        self.transition(json.loads(f.read()), continent_players_male, questions_male)
                if self.index_transition == 2:
                    self.results = continent_players_male
                    json_male.create_json_africa("answers.json", questions_male, continent_players_male)
                    with open("answers.json", "r", encoding='utf-8') as f:
                        self.transition(json.loads(f.read()), continent_players_male, questions_male)
            if user_answer == "no" or user_answer == "dnk":
                self.index_transition += 1
                try:
                    self.app.root.ids.fourth.set_question(self.initial_male_questions[self.index_transition])
                except IndexError:
                    sm = App.get_running_app().root
                    sm.current = self.SCREEN_NAME
                    self.app.root.ids.fifth.display_answer(self.NOT_FOUND_MESSAGE)

        if self.index_male_female == 4:
            user_answer = self.app.root.ids.fourth.answer
            if user_answer == "yes":
                continent_players_female = self.contient_players_female[self.index_transition]
                questions_female = self.female_players_q[self.index_transition]
                if self.index_transition == 3:
                    self.results = continent_players_female
                    json_female.create_json_americas("answers.json", questions_female, continent_players_female)
                    with open("answers.json", "r", encoding='utf-8') as f:
                        self.transition(json.loads(f.read()), continent_players_female, questions_female)
                if self.index_transition == 0:
                    self.results = continent_players_female
                    json_female.create_json_europe("answers.json", questions_female, continent_players_female)
                    with open("answers.json", "r", encoding='utf-8') as f:
                        self.transition(json.loads(f.read()), continent_players_female, questions_female)
                if self.index_transition == 1:
                    self.results = continent_players_female
                    json_female.create_json_asia("answers.json", questions_female, continent_players_female)
                    with open("answers.json", "r", encoding='utf-8') as f:
                        self.transition(json.loads(f.read()), continent_players_female, questions_female)
                if self.index_transition == 2:
                    self.results = continent_players_female
                    json_female.create_json_africa("answers.json", questions_female, continent_players_female)
                    with open("answers.json", "r", encoding='utf-8') as f:
                        self.transition(json.loads(f.read()), continent_players_female, questions_female)
            if user_answer == "no" or user_answer == "dnk":
                self.index_transition += 1
                try:
                    self.app.root.ids.fourth.set_question(self.initial_female_questions[self.index_transition])
                except IndexError:
                    sm = App.get_running_app().root
                    sm.current = self.SCREEN_NAME
                    self.app.root.ids.fifth.display_answer(self.NOT_FOUND_MESSAGE)

    def welcome(self):
        """First question which is asked to the user."""
        self.app.root.ids.fourth.set_question("Is your player a woman?")

    def transition(self, answers_recieved, players, questions):
        """
        Receives the information of the json file, the list of questions
        and the list of the countries.

        ----------
        answers_recieved :
            contains the json file's information.

        players : list
            contains a list of the players.

        questions : list
            contains a list of the questions.
        """
        self.answers = answers_recieved
        self.continent_players = players
        self.questions_players = questions
        self.app.root.ids.fourth.set_question(self.questions_players[0])
        self.app.root.ids.fourth.index += 10
        self.results = self.continent_players

    def get_answer(self):
        """
        Checks the answer of the user for every question with the json file
        in order to try and guess the user's thought.

        After every answer given by the user, the function responsible for the
        logic of the specific players gets called.
        """
        self.answer_user = self.app.root.ids.fourth.answer
        set_answer = []
        if self.answer_user == 'dnk':
            set_answer = self.results
        else:
            for country in self.continent_players:
                if self.answers[country][self.questions_players[0]] == self.answer_user:
                    set_answer.append(country)
        if len(self.continent_players) == 48:
            europe_male_logic.europe_male_logic(self)
        if len(self.continent_players) == 35:
            asia_male_logic.asia_male_logic(self)
        if len(self.continent_players) == 5:
            africa_male_logic.africa_male_logic(self)
        if len(self.continent_players) == 12:
            americas_male_logic.americas_male_logic(self)
        if len(self.continent_players) == 2:
            africa_female_logic.africa_female_logic(self)
        if len(self.continent_players) == 7:
            americas_female_logic.americas_female_logic(self)
        if len(self.continent_players) == 53:
            asia_female_logic.asia_female_logic(self)
        if len(self.continent_players) == 38:
            europe_female_logic.europe_female_logic(self)

        self.store_answer = self.results
        self.results = set(self.results) & set(set_answer)
        return self.results

    def game_manager(self):
        """
        Calls the get_answer function and checks the length of result.
        If no answer is found, it moves on to the next question.

        If an answer is found it changes the screen to the result page.
        """
        self.results = self.get_answer()
        print(self.results)
        if len(self.results) == 1:
            guess = list(self.results)
            sm = App.get_running_app().root
            sm.current = self.SCREEN_NAME
            self.app.root.ids.fifth.display_answer(self.RESULT_MESSAGE + guess[0])
        elif len(self.results) == 0:
            sm = App.get_running_app().root
            sm.current = self.SCREEN_NAME
            if len(self.store_answer) < 6:
                result_without_quotes1 = ", ".join(list(self.store_answer))
                self.app.root.ids.fifth.display_answer(self.NOT_FOUND_MESSAGE1 + str(result_without_quotes1))
            else:
                sm = App.get_running_app().root
                sm.current = self.SCREEN_NAME
                self.app.root.ids.fifth.display_answer(self.NOT_FOUND_MESSAGE)
        else:
            try:
                self.app.root.ids.fourth.set_question(self.questions_players[0])
            except IndexError:
                if len(self.results) < 6:
                    sm = App.get_running_app().root
                    sm.current = self.SCREEN_NAME
                    result_without_quotes = ", ".join(list(self.results))
                    self.app.root.ids.fifth.display_answer(self.NOT_FOUND_MESSAGE1 + str(result_without_quotes))
                else:
                    sm = App.get_running_app().root
                    sm.current = self.SCREEN_NAME
                    self.app.root.ids.fifth.display_answer(self.NOT_FOUND_MESSAGE)

    def reset_index(self):
        """Resets the index variable to it's original value."""
        self.app.root.ids.fourth.index = 1001
        print("reset players index")


if __name__ == '__main__':
    Players()
