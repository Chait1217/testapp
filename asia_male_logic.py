"""
A function that handles the logic of the questions.
"""


def asia_male_check(self):
    """
    Manages the logic of the questions according to the answers given by the user
    for men table tennis players situated in Asia.
    """
    if self.app.root.ids.fourth.questions == "Is your player left handed?":
        if self.answer_user == 'no' or self.answer_user == "dnk":
            self.questions_country.remove("Is your player left handed?")
        if self.answer_user == "yes":
            self.questions_country.remove("Is your player left handed?")
            self.questions_country.remove("Is your player Indian?")

    if self.app.root.ids.fourth.questions == "Does your player play with the pen hold grip?":
        if self.answer_user == 'no' or self.answer_user == "dnk":
            try:
                self.questions_country.remove("Does your player play with the pen hold grip?")
            except ValueError:
                pass
        if self.answer_user == "yes":
            try:
                self.questions_country.remove("Does your player play with the pen hold grip?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is your player Indian?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is your player Korean?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Does your player serves the forehand reverse pendulum serve?")
            except ValueError:
                pass
    if self.app.root.ids.fourth.questions == "Is your player older than 30 years old?":
        try:
            self.questions_country.remove("Is your player older than 30 years old?")
        except ValueError:
            pass

    if self.app.root.ids.fourth.questions == "Did your player participate in 2016 Olympics in singles or team event?":
        try:
            self.questions_country.remove("Did your player participate in 2016 Olympics in singles or team event?")
        except ValueError:
            pass

    if self.app.root.ids.fourth.questions == "Did your player participate in 2021 Olympics in singles or team event?":
        try:
            self.questions_country.remove("Did your player participate in 2021 Olympics in singles or team event?")
        except ValueError:
            pass

    if self.app.root.ids.fourth.questions == "Has your player ever won an olympic medal in singles or in team event?":
        if self.answer_user == 'no' or self.answer_user == "dnk":
            try:
                self.questions_country.remove("Has your player ever won an olympic medal in singles or in team event?")
            except ValueError:
                pass
        if self.answer_user == "yes":
            try:
                self.questions_country.remove("Has your player ever won an olympic medal in singles or in team event?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is your player Indian?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is your player Korean?")
            except ValueError:
                pass
    if self.app.root.ids.fourth.questions == "Is your player sponsored by butterfly?":
        try:
            self.questions_country.remove("Is your player sponsored by butterfly?")
        except ValueError:
            pass
    if self.app.root.ids.fourth.questions == "Is your player Chinese?":
        if self.answer_user == 'no' or self.answer_user == "dnk":
            try:
                self.questions_country.remove("Is your player Chinese?")
            except ValueError:
                pass
        if self.answer_user == "yes":
            try:
                self.questions_country.remove("Is your player Chinese?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is your player Indian?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is your player Korean?")
            except ValueError:
                pass
    if self.app.root.ids.fourth.questions == "Is your player Korean?":
        if self.answer_user == 'no' or self.answer_user == "dnk":
            try:
                self.questions_country.remove("Is your player Korean?")
            except ValueError:
                pass
        if self.answer_user == "yes":
            try:
                self.questions_country.remove("Is your player Indian?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is your player Korean?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Does your player serves the forehand reverse pendulum serve?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Does your player serves the forehand hook serve?")
            except ValueError:
                pass
    if self.app.root.ids.fourth.questions == "Is your player Indian?":
        if self.answer_user == 'no' or self.answer_user == "dnk":
            try:
                self.questions_country.remove("Is your player Indian?")
            except ValueError:
                pass
        if self.answer_user == "yes":
            try:
                self.questions_country.remove("Is your player Indian?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Does your player serves the forehand hook serve?")
            except ValueError:
                pass
    if self.app.root.ids.fourth.questions == "Does your player serves the forehand reverse pendulum serve?":
        if self.answer_user == 'no' or self.answer_user == "dnk":
            try:
                self.questions_country.remove("Does your player serves the forehand reverse pendulum serve?")
            except ValueError:
                pass
        if self.answer_user == "yes":
            try:
                self.questions_country.remove("Does your player serves the forehand reverse pendulum serve?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Does your player serves the forehand hook serve?")
            except ValueError:
                pass
    if self.app.root.ids.fourth.questions == "Does your player serves the forehand hook serve?":
        try:
            self.questions_country.remove("Does your player serves the forehand hook serve?")
        except ValueError:
            pass
