import questionslogic
import countrieslogic
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen


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


    def set_question(self, text):
        self.ids.question.text = text

    def on_pre_enter(self, *args):
        #self.game = questionslogic.Game()
        #self.set_question(self.game.questions1[0])
        #self.game.get_answer_json()
        self.test = questionslogic.Before()
        self.test.bienvenu()


    def set_answer(self, answer):
        self.answer = answer
        print(self.answer)
        self.test.game_manager()

    def teststart(self,answer1):
        self.index += 1
        if self.index < 7:
            self.answer = answer1
            print(self.answer)
            self.test.questionmanager()
        else:
            self.set_answer(answer1)


class FourthWindow(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.answer = ''
        self.index = 0
        self.game = None
        self.test = None


    def set_question1(self, text):
        self.ids.question.text = text

    def on_pre_enter(self, *args):
        #self.game = questionslogic.Game()
        #self.set_question(self.game.questions1[0])
        #self.game.get_answer_json()
        self.test = countrieslogic.Countries()
        self.test.bienvenu1()


    def set_answer1(self, answer):
        self.answer = answer
        print(self.answer)
        self.test.game_manager1()

    def teststart1(self,answer1):
        self.index += 1
        if self.index < 7:
            self.answer = answer1
            print(self.answer)
            self.test.questionmanager1()
        else:
            self.set_answer1(answer1)



class WindowManager(ScreenManager):
    pass


class Advanced(App):
    def build(self):
        kv = Builder.load_file("best.kv")
        return kv


if __name__ == "__main__":
    Advanced().run()

