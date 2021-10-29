"""
Countries Theme.

Contains all the code to play the game.
"""

from kivy.app import App

import json
import africa_logic
import asia_logic
import countries_start
import europe_logic
import json_countries
import north_central_logic
import oceania_logic
import south_america_logic


class Countries:
    """
    Handles the Countries theme main logic and the results.

    ...
    Attributes
    ----------
    continent : list
        contains a list of all the countries separated by continents.

    continent_q : list
        contains a list of all the questions for every continents.

    questions_first : list
        contains a list of all the initial questions.

    app : object
        Instance of the class Akiping.

    index_question : int
        used for changing the questions.
    """

    SCREEN_NAME = "fifth"
    RESULT_MESSAGE = "You were thinking of: "
    NOT_FOUND_MESSAGE = "Sorry, couldn't guess your country."
    NOT_FOUND_MESSAGE1 = "Sorry, couldn't guess your country. These are the possible countries: "

    def __init__(self):
        self.continent = countries_start.countries_list()
        self.continent_q = countries_start.countries_question()
        self.questions_first = countries_start.start_question()
        self.app = App.get_running_app()
        self.index_question = 0

    def question_manager(self):
        """
        Checks in which continent is the user's country and creates the
        json file on the fly, which contains all the attributes of the countries.

        Then transfers the information to the transition function.
        """
        user_answer = self.app.root.ids.third.answer
        if user_answer == "yes":
            continent_countries = self.continent[self.index_question]
            questions_ask = self.continent_q[self.index_question]
            if self.index_question == 5:
                self.results = continent_countries
                json_countries.create_json_oceania("answers.json", questions_ask, continent_countries)
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
        if user_answer == "no" or user_answer == "dnk":
            self.index_question += 1
            try:
                self.app.root.ids.third.set_question(self.questions_first[self.index_question])
            except IndexError:
                sm = App.get_running_app().root
                sm.current = self.SCREEN_NAME
                self.app.root.ids.fifth.display_answer(self.NOT_FOUND_MESSAGE)

    def welcome(self):
        """First question which is asked to the user."""
        self.app.root.ids.third.set_question("Is your country situated in Europe?")

    def transition(self, answers_received, continent, questions):
        """
        Receives the information of the json file, the list of questions
        and the list of the countries.

        ----------
        answers_received :
            contains the json file's information.

        continent : list
            contains a list of the countries.

        questions : list
            contains a list of the questions.
        """
        self.answers = answers_received
        self.continent_country = continent
        self.questions_country = questions
        self.app.root.ids.third.set_question(self.questions_country[0])
        self.app.root.ids.third.index += 10
        self.results = self.continent_country

    def get_answer(self):
        """
        Checks the answer of the user for every question with the json file
        in order to try and guess the user's thought.

        After every answer given by the user, the function responsible for the
        logic of the specific continent gets called.
        """
        self.answer_user = self.app.root.ids.third.answer
        set_answer = []
        if self.answer_user == 'dnk':
            set_answer = self.results
        else:
            for country in self.continent_country:
                if self.answers[country][self.questions_country[0]] == self.answer_user:
                    set_answer.append(country)
        if len(self.continent_country) == 46:
            europe_logic.europe_logic(self)
        if len(self.continent_country) == 45:
            asia_logic.asia_logic(self)
        if len(self.continent_country) == 14:
            oceania_logic.oceania_logic(self)
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
        """
        Calls the get_answer function and checks the length of result.
        If no answer is found, it moves on to the next question.

        If an answer is found it changes the screen to the result page.
        """
        self.results = self.get_answer()
        if len(self.results) == 1:
            guess = list(self.results)
            sm = App.get_running_app().root
            sm.current = self.SCREEN_NAME
            self.app.root.ids.fifth.display_answer(self.RESULT_MESSAGE + guess[0])
        elif len(self.results) == 0:
            sm = App.get_running_app().root
            sm.current = self.SCREEN_NAME
            if len(self.store_answer) < 6:
                result_without_quotes = ", ".join(list(self.store_answer))
                self.app.root.ids.fifth.display_answer(self.NOT_FOUND_MESSAGE1 + str(result_without_quotes))
            else:
                sm = App.get_running_app().root
                sm.current = self.SCREEN_NAME
                self.app.root.ids.fifth.display_answer(self.NOT_FOUND_MESSAGE)
        else:
            try:
                self.app.root.ids.third.set_question(self.questions_country[0])
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
        self.app.root.ids.third.index = 0


if __name__ == '__main__':
    Countries()
