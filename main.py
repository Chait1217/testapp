import questionslogic
import countrieslogic
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.utils import platform
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivy.graphics import Rectangle
from kivymd.icon_definitions import md_icons
from kivymd.uix.button import MDRoundFlatButton,MDRectangleFlatButton,MDRaisedButton,MDIconButton
from kivymd.color_definitions import colors, palette, hue
from kivymd.uix.navigationdrawer import MDNavigationDrawer




Window.size = (350,600)



class MainWindow(Screen):
    pass


class SecondWindow(Screen):
    pass


class ThirdWindow(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.answer = ''
        self.index = 0
        self.game = None
        self.test = None
        self.test1 = None

    def set_question(self, text):
        self.ids.question.text = text
        self.test1 = text

    def on_pre_enter(self, *args):
        self.test = questionslogic.Before()
        self.test.bienvenu()


    def set_answer(self, answer):
        self.answer = answer
        print(self.answer)
        self.test.game_manager()

    def teststart(self,answer1):
        self.index += 1
        print(self.index)
        if self.index < 7:
            self.answer = answer1
            print(self.answer)
            self.test.questionmanager()
        else:
            self.set_answer(answer1)


    def reset_game(self):
        self.indexverifier("reset")





class FourthWindow(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.answer = ''
        self.index = 0
        self.game = None
        self.test = None
        self.test1 = None


    def set_question1(self, text):
        self.ids.question.text = text
        self.test1 = text

    def on_pre_enter(self, *args):
        self.test = countrieslogic.Countries()
        self.test.bienvenu1()


    def set_answer1(self, answer):
        self.answer = answer
        print(self.answer)
        self.test.game_manager1()

    def teststart1(self,answer1):
        self.index += 1
        print(self.index)
        if self.index < 7:
            self.answer = answer1
            print(self.answer)
            self.test.questionmanager1()
        else:
            self.set_answer1(answer1)



class FifthWindow(Screen):
    def set_question(self, text):
        self.ids.question1.text = text


class WindowManager(ScreenManager):
    pass


class Advanced(MDApp):


    def change_screen(self):
        sm = App.get_running_app().root
        sm.current = "main"
        #attribut = ThirdWindow()
        #attribut.reset_game()
        print("executed")



    def build(self):
        self.theme_cls.primary_palette = "Orange"
        self.theme_cls.primary_hue = "100"
        self.theme_cls.theme_style = "Light"
        kv = Builder.load_file("best.kv")
        return kv


if __name__ == "__main__":
    Advanced().run()

