"""
A function that handles the logic of the questions.
"""


def americas_male_check(self):
    """
    Manages the logic of the questions according to the answers given by the user
    for men table tennis players situated in the Americas.
    """
    if self.app.root.ids.fourth.questions == "Is your player left handed?":
        if self.answer_user == 'no' or self.answer_user == "dnk":
            self.questions_country.remove("Is your player left handed?")
        if self.answer_user == "yes":
            self.questions_country.remove("Is your player left handed?")
            self.questions_country.remove("Did your player participate in 2016 Olympics in singles or team event?")
            self.questions_country.remove("Is your player sponsored by butterfly?")
            self.questions_country.remove("Is your player Argentinian?")
            self.questions_country.remove("Is your player ranked in the top 30 of the world?")
            self.questions_country.remove("Is your player known for his shots with two hands?")

    if self.app.root.ids.fourth.questions == "Is your player older than 30 years old?":
        if self.answer_user == 'no' or self.answer_user == "dnk":
            try:
                self.questions_country.remove("Is your player older than 30 years old?")
            except ValueError:
                pass
        if self.answer_user == "yes":
            try:
                self.questions_country.remove("Is your player older than 30 years old?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is your player ranked in the top 30 of the world?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is your player known for his shots with two hands?")
            except ValueError:
                pass
    if self.app.root.ids.fourth.questions == "Did your player participate in 2016 Olympics in singles or team event?":
        if self.answer_user == "dnk":
            try:
                self.questions_country.remove("Did your player participate in 2016 Olympics in singles or team event?")
            except ValueError:
                pass
        if self.answer_user == "yes":
            try:
                self.questions_country.remove("Did your player participate in 2016 Olympics in singles or team event?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is your player Argentinian?")
            except ValueError:
                pass

        if self.answer_user == 'no':
            try:
                self.questions_country.remove("Did your player participate in 2016 Olympics in singles or team event?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is your player ranked in the top 30 of the world?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is your player known for his shots with two hands?")
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
                self.questions_country.remove("Is your player Argentinian?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is your player ranked in the top 30 of the world?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is your player known for his shots with two hands?")
            except ValueError:
                pass
    if self.app.root.ids.fourth.questions == "Is your player sponsored by butterfly?":
        if self.answer_user == "no" or self.answer_user == "dnk":
            try:
                self.questions_country.remove("Is your player sponsored by butterfly?")
            except ValueError:
                pass
        if self.answer_user == 'yes':
            try:
                self.questions_country.remove("Is your player sponsored by butterfly?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is your player Argentinian?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is your player known for his shots with two hands?")
            except ValueError:
                pass
    if self.app.root.ids.fourth.questions == "Is your player Argentinian?":
        if self.answer_user == "no" or self.answer_user == "dnk":
            try:
                self.questions_country.remove("Is your player Argentinian?")
            except ValueError:
                pass
        if self.answer_user == 'yes':
            try:
                self.questions_country.remove("Is your player Argentinian?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is your player ranked in the top 30 of the world?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is your player known for his shots with two hands?")
            except ValueError:
                pass
    if self.app.root.ids.fourth.questions == "Is your player ranked in the top 30 of the world?":
        if self.answer_user == "yes" or self.answer_user == "dnk":
            try:
                self.questions_country.remove("Is your player ranked in the top 30 of the world?")
            except ValueError:
                pass
        if self.answer_user == 'no':
            try:
                self.questions_country.remove("Is your player ranked in the top 30 of the world?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is your player known for his shots with two hands?")
            except ValueError:
                pass
    if self.app.root.ids.fourth.questions == "Is your player known for his shots with two hands?":
        try:
            self.questions_country.remove("Is your player known for his shots with two hands?")
        except ValueError:
            pass
