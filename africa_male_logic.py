"""
A function that handles the logic of the questions.
"""


def africa_male_check(self):
    """
    Manages the logic of the questions according to the answers given by the user
    for men table tennis players situated in Africa.
    """
    if self.app.root.ids.fourth.questions == "Is your player older than 30 years old?":
        if self.answer_user == 'no' or self.answer_user == "dnk" or self.answer_user == "yes":
            self.questions_country.remove("Is your player older than 30 years old?")
    if self.app.root.ids.fourth.questions == "Did your player participate in 2016 Olympics in singles or team event?":
        if self.answer_user == "dnk":
            try:
                self.questions_country.remove("Did your player participate in 2016 Olympics in singles or team event?")
            except ValueError:
                pass
        if self.answer_user == 'no':
            try:
                self.questions_country.remove("Did your player participate in 2016 Olympics in singles or team event?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is he known for his extremely powerful forehand?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Did he reach the quarter finals in 2021 olympics in singles?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is your player sponsored by butterfly?")
            except ValueError:
                pass
        if self.answer_user == "yes":
            try:
                self.questions_country.remove("Did your player participate in 2016 Olympics in singles or team event?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Did your player participate in 2021 Olympics in singles or team event?")
            except ValueError:
                pass
    if self.app.root.ids.fourth.questions == "Did your player participate in 2021 Olympics in singles or team event?":
        if self.answer_user == "dnk":
            try:
                self.questions_country.remove("Did your player participate in 2021 Olympics in singles or team event?")
            except ValueError:
                pass
        if self.answer_user == "yes":
            try:
                self.questions_country.remove("Did your player participate in 2021 Olympics in singles or team event?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is your player older than 40 years old?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is your player the 2nd best player of nigeria?")
            except ValueError:
                pass

        if self.answer_user == 'no':
            try:
                self.questions_country.remove("Did your player participate in 2021 Olympics in singles or team event?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is he known for his extremely powerful forehand?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Did he reach the quarter finals in 2021 olympics in singles?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Did he use to represent france when he was under 18?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is your player sponsored by butterfly?")
            except ValueError:
                pass
    if self.app.root.ids.fourth.questions == "Is your player sponsored by gewo?":
        if self.answer_user == "yes":
            try:
                self.questions_country.remove("Is your player sponsored by gewo?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Did he reach the quarter finals in 2021 olympics in singles?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is your player older than 40 years old?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Did he use to represent france when he was under 18?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is your player sponsored by butterfly?")
            except ValueError:
                pass
        if self.answer_user == 'no':
            try:
                self.questions_country.remove("Is your player sponsored by gewo?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is he known for his extremely powerful forehand?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is your player the 2nd best player of nigeria?")
            except ValueError:
                pass
        if self.answer_user == "dnk":
            try:
                self.questions_country.remove("Is your player sponsored by gewo?")
            except ValueError:
                pass

    if self.app.root.ids.fourth.questions == "Is he known for his extremely powerful forehand?":
        try:
            self.questions_country.remove("Is he known for his extremely powerful forehand?")
        except ValueError:
            pass

    if self.app.root.ids.fourth.questions == "Did he reach the quarter finals in 2021 olympics in singles?":
        try:
            self.questions_country.remove("Did he reach the quarter finals in 2021 olympics in singles?")
        except ValueError:
            pass

    if self.app.root.ids.fourth.questions == "Is your player older than 40 years old?":
        try:
            self.questions_country.remove("Is your player older than 40 years old?")
        except ValueError:
            pass

    if self.app.root.ids.fourth.questions == "Did he use to represent france when he was under 18?":
        try:
            self.questions_country.remove("Did he use to represent france when he was under 18?")
        except ValueError:
            pass

    if self.app.root.ids.fourth.questions == "Is your player the 2nd best player of nigeria?":
        try:
            self.questions_country.remove("Is your player the 2nd best player of nigeria?")
        except ValueError:
            pass

    if self.app.root.ids.fourth.questions == "Is your player sponsored by butterfly?":
        try:
            self.questions_country.remove("Is your player sponsored by butterfly?")
        except ValueError:
            pass
