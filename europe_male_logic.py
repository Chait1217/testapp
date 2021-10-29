"""
A function that handles the logic of the questions.
"""


def europe_male_logic(self):
    """
    Manages the logic of the questions according to the answers given by the user
    for the male table tennis players situated in Europe.
    """
    YES = "yes"
    NO = "no"
    DNK = "dnk"
    Q1 = "Does your player play with pimples?"
    Q2 = "Is your player left handed?"
    Q3 = "Has your player ever won an olympic medal in singles or in team event?"
    Q4 = "Is your player from England?"
    Q5 = "Is your player Austrian?"
    Q6 = "Is your player Croatian?"
    Q7 = "Does your player serves with the backhand?"
    Q8 = "Is your player older than 30 years old?"
    Q9 = "Did your player participate in 2016 Olympics in singles or team event?"
    Q10 = "Did your player participate in 2021 Olympics in singles or team event?"
    Q11 = "Is your player sponsored by butterfly?"
    Q12 = "Does your player serves the forehand hook serve?"
    Q13 = "Is your player Swedish?"
    Q14 = "Is your player German?"
    Q15 = "Does your player serves the forehand reverse pendulum serve?"

    if self.app.root.ids.fourth.questions == Q1:
        if self.answer_user == NO or self.answer_user == DNK:
            self.questions_players.remove(Q1)
        if self.answer_user == YES:
            self.questions_players.remove(Q1)
            self.questions_players.remove(Q2)
            self.questions_players.remove(Q3)
            self.questions_players.remove(Q4)
            self.questions_players.remove(Q5)
            self.questions_players.remove(Q6)

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
                self.questions_players.remove(Q7)
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

    if self.app.root.ids.fourth.questions == Q8:
        if self.answer_user == YES or self.answer_user == DNK:
            try:
                self.questions_players.remove(Q8)
            except ValueError:
                pass
        if self.answer_user == NO:
            try:
                self.questions_players.remove(Q8)
            except ValueError:
                pass
            try:
                self.questions_players.remove(Q5)
            except ValueError:
                pass
    if self.app.root.ids.fourth.questions == Q9:
        if self.answer_user == NO:
            try:
                self.questions_players.remove(Q9)
            except ValueError:
                pass
            try:
                self.questions_players.remove(Q5)
            except ValueError:
                pass
            try:
                self.questions_players.remove(Q4)
            except ValueError:
                pass
        if self.answer_user == YES or self.answer_user == DNK:
            try:
                self.questions_players.remove(Q9)
            except ValueError:
                pass
    if self.app.root.ids.fourth.questions == Q10:
        if self.answer_user == YES or self.answer_user == DNK:
            try:
                self.questions_players.remove(Q10)
            except ValueError:
                pass
        if self.answer_user == NO:
            try:
                self.questions_players.remove(Q10)
            except ValueError:
                pass
            try:
                self.questions_players.remove(Q3)
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
        if self.answer_user == YES:
            try:
                self.questions_players.remove(Q3)
            except ValueError:
                pass
            try:
                self.questions_players.remove(Q11)
            except ValueError:
                pass
            try:
                self.questions_players.remove(Q12)
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
            try:
                self.questions_players.remove(Q13)
            except ValueError:
                pass
            try:
                self.questions_players.remove(Q14)
            except ValueError:
                pass
    if self.app.root.ids.fourth.questions == Q11:
        if self.answer_user == NO or self.answer_user == DNK:
            try:
                self.questions_players.remove(Q11)
            except ValueError:
                pass
        if self.answer_user == YES:
            try:
                self.questions_players.remove(Q11)
            except ValueError:
                pass
            try:
                self.questions_players.remove(Q4)
            except ValueError:
                pass

    if self.app.root.ids.fourth.questions == Q7:
        if self.answer_user == NO or self.answer_user == DNK:
            try:
                self.questions_players.remove(Q7)
            except ValueError:
                pass
        if self.answer_user == YES:
            try:
                self.questions_players.remove(Q7)
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

    if self.app.root.ids.fourth.questions == Q15:
        try:
            self.questions_players.remove(Q15)
        except ValueError:
            pass

    if self.app.root.ids.fourth.questions == Q12:
        if self.answer_user == NO or self.answer_user == DNK:
            try:
                self.questions_players.remove(Q12)
            except ValueError:
                pass
        if self.answer_user == YES:
            try:
                self.questions_players.remove(Q12)
            except ValueError:
                pass
            try:
                self.questions_players.remove(Q5)
            except ValueError:
                pass

    if self.app.root.ids.fourth.questions == Q13:
        if self.answer_user == NO or self.answer_user == DNK:
            try:
                self.questions_players.remove(Q13)
            except ValueError:
                pass
        if self.answer_user == YES:
            try:
                self.questions_players.remove(Q13)
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
            try:
                self.questions_players.remove(Q14)
            except ValueError:
                pass
    if self.app.root.ids.fourth.questions == Q14:
        if self.answer_user == NO or self.answer_user == DNK:
            try:
                self.questions_players.remove(Q14)
            except ValueError:
                pass
        if self.answer_user == YES:
            try:
                self.questions_players.remove(Q14)
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
    if self.app.root.ids.fourth.questions == Q4:
        if self.answer_user == NO or self.answer_user == DNK:
            try:
                self.questions_players.remove(Q4)
            except ValueError:
                pass
        if self.answer_user == YES:
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
                self.questions_players.remove(Q6)
            except ValueError:
                pass
    if self.app.root.ids.fourth.questions == Q6:
        try:
            self.questions_players.remove(Q6)
        except ValueError:
            pass

