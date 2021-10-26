"""
A function that handles the logic of the questions.
"""


def europe_male_check(self):
    """
    Manages the logic of the questions according to the answers given by the user
    for men table tennis players situated in Europe.
    """
    if self.app.root.ids.fourth.questions == "Does your player play with pimples?":
        if self.answer_user == 'no' or self.answer_user == "dnk":
            self.questions_country.remove("Does your player play with pimples?")
        if self.answer_user == "yes":
            self.questions_country.remove("Does your player play with pimples?")
            self.questions_country.remove("Is your player left handed?")
            self.questions_country.remove("Has your player ever won an olympic medal in singles or in team event?")
            self.questions_country.remove("Is your player from England?")
            self.questions_country.remove("Is your player Austrian?")
            self.questions_country.remove("Is your player Croatian?")

    if self.app.root.ids.fourth.questions == "Is your player left handed?":
        if self.answer_user == 'no' or self.answer_user == "dnk":
            try:
                self.questions_country.remove("Is your player left handed?")
            except ValueError:
                pass
        if self.answer_user == "yes":
            try:
                self.questions_country.remove("Is your player left handed?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Does your player serves with the backhand?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is your player from England?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is your player Austrian?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is your player Croatian?")
            except ValueError:
                pass

    if self.app.root.ids.fourth.questions == "Is your player older than 30 years old?":
        if self.answer_user == 'yes' or self.answer_user == "dnk":
            try:
                self.questions_country.remove("Is your player older than 30 years old?")
            except ValueError:
                pass
        if self.answer_user == "no":
            try:
                self.questions_country.remove("Is your player older than 30 years old?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is your player Austrian?")
            except ValueError:
                pass
    if self.app.root.ids.fourth.questions == "Did your player participate in 2016 Olympics in singles or team event?":
        if self.answer_user == "no":
            try:
                self.questions_country.remove("Did your player participate in 2016 Olympics in singles or team event?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is your player Austrian?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is your player from England?")
            except ValueError:
                pass
        if self.answer_user == 'yes' or self.answer_user == "dnk":
            try:
                self.questions_country.remove("Did your player participate in 2016 Olympics in singles or team event?")
            except ValueError:
                pass
    if self.app.root.ids.fourth.questions == "Did your player participate in 2021 Olympics in singles or team event?":
        if self.answer_user == 'yes' or self.answer_user == "dnk":
            try:
                self.questions_country.remove("Did your player participate in 2021 Olympics in singles or team event?")
            except ValueError:
                pass
        if self.answer_user == "no":
            try:
                self.questions_country.remove("Did your player participate in 2021 Olympics in singles or team event?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Has your player ever won an olympic medal in singles or in team event?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is your player Croatian?")
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
                self.questions_country.remove("Is your player sponsored by butterfly?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Does your player serves the forehand hook serve?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is your player from England?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is your player Austrian?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is your player Croatian?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is your player Swedish?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is your player German?")
            except ValueError:
                pass
    if self.app.root.ids.fourth.questions == "Is your player sponsored by butterfly?":
        if self.answer_user == 'no' or self.answer_user == "dnk":
            try:
                self.questions_country.remove("Is your player sponsored by butterfly?")
            except ValueError:
                pass
        if self.answer_user == "yes":
            try:
                self.questions_country.remove("Is your player sponsored by butterfly?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is your player from England?")
            except ValueError:
                pass

    if self.app.root.ids.fourth.questions == "Does your player serves with the backhand?":
        if self.answer_user == 'no' or self.answer_user == "dnk":
            try:
                self.questions_country.remove("Does your player serves with the backhand?")
            except ValueError:
                pass
        if self.answer_user == "yes":
            try:
                self.questions_country.remove("Does your player serves with the backhand?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is your player from England?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is your player Austrian?")
            except ValueError:
                pass

    if self.app.root.ids.fourth.questions == "Does your player serves the forehand reverse pendulum serve?":
        try:
            self.questions_country.remove("Does your player serves the forehand reverse pendulum serve?")
        except ValueError:
            pass

    if self.app.root.ids.fourth.questions == "Does your player serves the forehand hook serve?":
        if self.answer_user == 'no' or self.answer_user == "dnk":
            try:
                self.questions_country.remove("Does your player serves the forehand hook serve?")
            except ValueError:
                pass
        if self.answer_user == "yes":
            try:
                self.questions_country.remove("Does your player serves the forehand hook serve?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is your player Austrian?")
            except ValueError:
                pass

    if self.app.root.ids.fourth.questions == "Is your player Swedish?":
        if self.answer_user == 'no' or self.answer_user == "dnk":
            try:
                self.questions_country.remove("Is your player Swedish?")
            except ValueError:
                pass
        if self.answer_user == "yes":
            try:
                self.questions_country.remove("Is your player Swedish?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is your player from England?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is your player Austrian?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is your player Croatian?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is your player German?")
            except ValueError:
                pass
    if self.app.root.ids.fourth.questions == "Is your player German?":
        if self.answer_user == 'no' or self.answer_user == "dnk":
            try:
                self.questions_country.remove("Is your player German?")
            except ValueError:
                pass
        if self.answer_user == "yes":
            try:
                self.questions_country.remove("Is your player German?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is your player from England?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is your player Austrian?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is your player Croatian?")
            except ValueError:
                pass
    if self.app.root.ids.fourth.questions == "Is your player from England?":
        if self.answer_user == 'no' or self.answer_user == "dnk":
            try:
                self.questions_country.remove("Is your player from England?")
            except ValueError:
                pass
        if self.answer_user == "yes":
            try:
                self.questions_country.remove("Is your player from England?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is your player Austrian?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is your player Croatian?")
            except ValueError:
                pass
    if self.app.root.ids.fourth.questions == "Is your player Austrian?":
        if self.answer_user == 'no' or self.answer_user == "dnk":
            try:
                self.questions_country.remove("Is your player Austrian?")
            except ValueError:
                pass
        if self.answer_user == "yes":
            try:
                self.questions_country.remove("Is your player Austrian?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is your player Croatian?")
            except ValueError:
                pass
    if self.app.root.ids.fourth.questions == "Is your player Croatian?":
        try:
            self.questions_country.remove("Is your player Croatian?")
        except ValueError:
            pass
