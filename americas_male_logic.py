"""
A function that handles the logic of the questions.
"""


def americas_male_logic(self):
    """
    Manages the logic of the questions according to the answers given by the user
    for the male table tennis players situated in the Americas.
    """
    YES = "yes"
    NO = "no"
    DNK = "dnk"
    Q1 = "Is your player left handed?"
    Q2 = "Did your player participate in 2016 Olympics in singles or team event?"
    Q3 = "Is your player sponsored by butterfly?"
    Q4 = "Is your player Argentinian?"
    Q5 = "Is your player ranked in the top 30 of the world?"
    Q6 = "Is your player known for his shots with two hands?"
    Q7 = "Is your player older than 30 years old?"
    Q8 = "Did your player participate in 2021 Olympics in singles or team event?"

    if self.app.root.ids.fourth.questions == Q1:
        if self.answer_user == NO or self.answer_user == DNK:
            self.questions_players.remove(Q1)
        else:
            self.questions_players.remove(Q1)
            self.questions_players.remove(Q2)
            self.questions_players.remove(Q3)
            self.questions_players.remove(Q4)
            self.questions_players.remove(Q5)
            self.questions_players.remove(Q6)

    if self.app.root.ids.fourth.questions == Q7:
        if self.answer_user == NO or self.answer_user == DNK:
            try:
                self.questions_players.remove(Q7)
            except ValueError:
                pass
        else:
            try:
                self.questions_players.remove(Q7)
            except ValueError:
                pass
            try:
                self.questions_players.remove(Q5)
            except ValueError:
                pass
            try:
                self.questions_players.remove(Q6)
            except ValueError:
                pass
    if self.app.root.ids.fourth.questions == Q2:
        if self.answer_user == DNK:
            try:
                self.questions_players.remove(Q2)
            except ValueError:
                pass
        if self.answer_user == YES:
            try:
                self.questions_players.remove(Q2)
            except ValueError:
                pass
            try:
                self.questions_players.remove(Q4)
            except ValueError:
                pass

        else:
            try:
                self.questions_players.remove(Q2)
            except ValueError:
                pass
            try:
                self.questions_players.remove(Q5)
            except ValueError:
                pass
            try:
                self.questions_players.remove(Q6)
            except ValueError:
                pass

    if self.app.root.ids.fourth.questions == Q8:
        if self.answer_user == YES or self.answer_user == DNK:
            try:
                self.questions_players.remove(Q8)
            except ValueError:
                pass

        else:
            try:
                self.questions_players.remove(Q8)
            except ValueError:
                pass
            try:
                self.questions_players.remove(Q4)
            except ValueError:
                pass
            try:
                self.questions_players.remove(Q5)
            except ValueError:
                pass
            try:
                self.questions_players.remove(Q6)
            except ValueError:
                pass
    if self.app.root.ids.fourth.questions == Q3:
        if self.answer_user == NO or self.answer_user == DNK:
            try:
                self.questions_players.remove(Q3)
            except ValueError:
                pass
        else:
            try:
                self.questions_players.remove(Q3)
            except ValueError:
                pass
            try:
                self.questions_players.remove(Q4)
            except ValueError:
                pass
            try:
                self.questions_players.remove(Q6)
            except ValueError:
                pass
    if self.app.root.ids.fourth.questions == Q4:
        if self.answer_user == NO or self.answer_user == DNK:
            try:
                self.questions_players.remove(Q4)
            except ValueError:
                pass
        else:
            try:
                self.questions_players.remove(Q4)
            except ValueError:
                pass
            try:
                self.questions_players.remove(Q5)
            except ValueError:
                pass
            try:
                self.questions_players.remove(Q6)
            except ValueError:
                pass
    if self.app.root.ids.fourth.questions == Q5:
        if self.answer_user == YES or self.answer_user == DNK:
            try:
                self.questions_players.remove(Q5)
            except ValueError:
                pass
        else:
            try:
                self.questions_players.remove(Q5)
            except ValueError:
                pass
            try:
                self.questions_players.remove(Q6)
            except ValueError:
                pass
    if self.app.root.ids.fourth.questions == Q6:
        try:
            self.questions_players.remove(Q6)
        except ValueError:
            pass

