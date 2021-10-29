"""
Akiping.

This a game where you can choose between two themes: Countries and Top 100 table tennis players.
Think of either a country or a table tennis player and the computer will try to read your mind by asking questions.

Designed by Chaitanya Vepa.
"""

from kivy.lang import Builder
from kivy.config import Config
from kivy.core.window import Window
from kivy.utils import platform
from kivy.uix.screenmanager import ScreenManager, Screen

from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.icon_definitions import md_icons
from kivymd.uix.button import MDFillRoundFlatButton, MDRaisedButton, MDIconButton
from kivymd.color_definitions import colors, palette, hue

import countries
import players


if platform == 'win':
    Window.size = (350, 600)
#  Simulate a phone screen

Config.set('kivy', 'exit_on_escape', '0')  # To avoid app shutdown by pressing 'return' on phone


class WelcomeScreen(Screen):
    """Welcome page screen."""
    pass


class ThemeScreen(Screen):
    """Choose your theme screen.
    Choose between 2 themes: Countries or Table tennis players.
    """
    pass


class CountriesScreen(Screen):
    """
    Screen for Countries theme.

    ...
    Attributes
    ----------
    answer : str
        answer given by the user.

    index : int
        number used to handle the logic and the questions.

    game: object
        creates an instance of the Countries class.

    questions : str
        stores the question shown to the user.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.answer = ''
        self.index = 0
        self.game = None
        self.questions = None

    def set_question(self, text):
        """
        Shows the question to the user.

        ----------
        text : str
            The future question
        """
        self.ids.question.text = text
        self.questions = text

    def on_pre_enter(self, *args):
        """Is called just before the user sees the screen."""
        self.game = countries.Countries()
        self.game.welcome()

    def call_manager(self, answer):
        """Saves the answer of the user and calls the game_manager function."""
        self.answer = answer
        self.game.game_manager()

    def logic(self, answer_given):
        """
        Calls different function depending on the current value of the index.

        ----------
        answer_given : str
            The answer received by the user.
        """
        if self.index < 7:
            self.answer = answer_given
            self.game.question_manager()
        else:
            self.call_manager(answer_given)


class TTPlayersScreen(Screen):
    """
    Screen for Table Tennis theme.

    ...
    Attributes
    ----------
    answer : str
        answer given by the user.

    index : int
        number used to handle the logic and the questions.

    game: object
        creates an instance of the Players class.

    questions : str
        stores the question shown to the user.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.answer = ''
        self.index = 1001
        self.game = None
        self.questions = None

    def set_question(self, text):
        """
        Shows the question to the user.

        ----------
        text : str
            The future question
        """
        self.ids.question.text = text
        self.questions = text

    def on_pre_enter(self, *args):
        """Is called just before the user sees the screen."""
        self.game = players.Players()
        self.game.welcome()

    def call_manager(self, answer):
        """Saves the answer of the user and calls the game_manager function."""
        self.answer = answer
        self.game.game_manager()

    def logic(self, answer_given):
        """
        Calls different functions depending on the current value of the index.

        ----------
        answer_given :
            The answer given by the user.
        """
        if self.index == 1001:
            self.answer = answer_given
            self.game.male_or_female()
        elif self.index < 7:
            self.answer = answer_given
            self.game.question_manager()
        else:
            self.call_manager(answer_given)


class ResultScreen(Screen):
    """Result Screen."""
    def display_answer(self, text):
        """Stores the final result."""
        self.ids.answer.text = text


class NavDrawer(Screen):
    """Navigation drawer screen."""
    pass


class LanguageScreen(Screen):
    """Choose to play the game in french or in english."""
    pass


class WindowManager(ScreenManager):
    """Manages all the screens."""
    pass


class AkipingApp(MDApp):
    """
    This class represents the app.
    It is necessary in order to use the kivy/kivyMD module.
    """
    def reset_index(self):
        """Resets the game index in order to play the game multiple times."""
        object_countries = countries.Countries()
        object_countries.reset_index()
        object_players = players.Players()
        object_players.reset_index()

    def change_screen_and_call_reset_function(self, screen_name):
        """
        Changes the current screen using the ScreenManager
        Parameters and calls the reset_index function.

        ----------
        screen_name : str
            The name of the future current screen
        """
        sm = MDApp.get_running_app().root
        sm.current = screen_name
        self.reset_index()

    def build(self):
        """
        Creates the app.
        Returns A file containing all the kv code.
        """
        self.theme_cls.primary_palette = "Orange"
        self.theme_cls.primary_hue = "100"
        self.theme_cls.theme_style = "Light"
        kv = Builder.load_file("main.kv")
        return kv


if __name__ == "__main__":
    AkipingApp().run()
