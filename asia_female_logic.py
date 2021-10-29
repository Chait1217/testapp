"""
A function that handles the logic of the questions.
"""


def asia_female_logic(self):
    """
    Manages the logic of the questions according to the answers given by the user
    for the female table tennis players situated in Asia.
    """
    YES = "yes"
    NO = "no"
    DNK = "dnk"
    Q1 = "Is your player left handed?"
    Q2 = "Is your player a defender?"
    Q3 = "Is your player older than 30 years old?"
    Q4 = "Is your player older than 25 years old?"
    Q5 = "Has your player ever won an olympic medal in singles or in team event?"
    Q6 = "Did your player participate in 2021 Olympics in singles or team event?"
    Q7 = "Did your player participate in 2016 Olympics in singles or team event?"
    Q8 = "Does your player serves with the backhand?"
    Q9 = "Does your player serves the forehand reverse pendulum serve?"
    Q10 = "Does your player serves the forehand hook serve?"
    Q11 = "Is your player Chinese?"
    Q12 = "Is your player Japanese?"

    if self.app.root.ids.fourth.questions == Q1:
        if self.answer_user == NO or self.answer_user == DNK:
            self.questions_players.remove(Q1)
        if self.answer_user == YES:
            self.questions_players.remove(Q1)
            self.questions_players.remove(Q2)

    if self.app.root.ids.fourth.questions == Q3:
        if self.answer_user == NO or self.answer_user == DNK:
            try:
                self.questions_players.remove(Q3)
            except ValueError:
                pass
        if self.answer_user == YES:
            try:
                self.questions_players.remove(Q3)
            except ValueError:
                pass
            try:
                self.questions_players.remove(Q4)
            except ValueError:
                pass
            try:
                self.questions_players.remove(Q9)
            except ValueError:
                pass

    if self.app.root.ids.fourth.questions == Q4:
        try:
            self.questions_players.remove(Q4)
        except ValueError:
            pass

    if self.app.root.ids.fourth.questions == Q2:
        if self.answer_user == NO or self.answer_user == DNK:
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
                self.questions_players.remove(Q5)
            except ValueError:
                pass
            try:
                self.questions_players.remove(Q6)
            except ValueError:
                pass
            try:
                self.questions_players.remove(Q8)
            except ValueError:
                pass
            try:
                self.questions_players.remove(Q9)
            except ValueError:
                pass

    if self.app.root.ids.fourth.questions == Q5:
        if self.answer_user == NO or self.answer_user == DNK:
            try:
                self.questions_players.remove(Q5)
            except ValueError:
                pass
        if self.answer_user == YES:
            try:
                self.questions_players.remove(Q5)
            except ValueError:
                pass
            try:
                self.questions_players.remove(Q8)
            except ValueError:
                pass

    if self.app.root.ids.fourth.questions == Q7:
        try:
            self.questions_players.remove(Q7)
        except ValueError:
            pass

    if self.app.root.ids.fourth.questions == Q6:
        try:
            self.questions_players.remove(Q6)
        except ValueError:
            pass

    if self.app.root.ids.fourth.questions == Q10:
        if self.answer_user == NO or self.answer_user == DNK:
            try:
                self.questions_players.remove(Q10)
            except ValueError:
                pass
        if self.answer_user == YES:
            try:
                self.questions_players.remove(Q10)
            except ValueError:
                pass
            try:
                self.questions_players.remove(Q9)
            except ValueError:
                pass

    if self.app.root.ids.fourth.questions == Q8:
        if self.answer_user == NO or self.answer_user == DNK:
            try:
                self.questions_players.remove(Q8)
            except ValueError:
                pass
        if self.answer_user == YES:
            try:
                self.questions_players.remove(Q8)
            except ValueError:
                pass
            try:
                self.questions_players.remove(Q9)
            except ValueError:
                pass

    if self.app.root.ids.fourth.questions == Q9:
        try:
            self.questions_players.remove(Q9)
        except ValueError:
            pass

    if self.app.root.ids.fourth.questions == Q11:
        try:
            self.questions_players.remove(Q11)
        except ValueError:
            pass

    if self.app.root.ids.fourth.questions == Q12:
        try:
            self.questions_players.remove(Q12)
        except ValueError:
            pass
