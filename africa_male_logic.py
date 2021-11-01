"""
A function that handles the logic of the questions.
"""


def africa_male_logic(self):
    """
    Manages the logic of the questions according to the answers given by the user
    for the male table tennis players situated in Africa.
    """
    YES = "yes"
    NO = "no"
    DNK = "dnk"
    Q1 = "Is your player older than 30 years old?"
    Q2 = "Did your player participate in 2016 Olympics in singles or team event?"
    Q3 = "Is he known for his extremely powerful forehand?"
    Q4 = "Did he reach the quarter finals in 2021 olympics in singles?"
    Q5 = "Is your player sponsored by butterfly?"
    Q6 = "Did your player participate in 2021 Olympics in singles or team event?"
    Q7 = "Is your player older than 40 years old?"
    Q8 = "Is your player the 2nd best player of nigeria?"
    Q9 = "Did he use to represent france when he was under 18?"
    Q10 = "Is your player sponsored by gewo?"

    if self.app.root.ids.fourth.questions == Q1:
        self.questions_players.remove(Q1)

    if self.app.root.ids.fourth.questions == Q2:
        if self.answer_user == DNK:
            try:
                self.questions_players.remove(Q2)
            except ValueError:
                pass
        if self.answer_user == NO:
            try:
                self.questions_players.remove(Q2)
            except ValueError:
                pass
            try:
                self.questions_players.remove(Q3)
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
        else:
            try:
                self.questions_players.remove(Q2)
            except ValueError:
                pass
            try:
                self.questions_players.remove(Q6)
            except ValueError:
                pass
    if self.app.root.ids.fourth.questions == Q6:
        if self.answer_user == DNK:
            try:
                self.questions_players.remove(Q6)
            except ValueError:
                pass
        if self.answer_user == YES:
            try:
                self.questions_players.remove(Q6)
            except ValueError:
                pass
            try:
                self.questions_players.remove(Q7)
            except ValueError:
                pass
            try:
                self.questions_players.remove(Q8)
            except ValueError:
                pass

        else:
            try:
                self.questions_players.remove(Q6)
            except ValueError:
                pass
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
            try:
                self.questions_players.remove(Q5)
            except ValueError:
                pass
    if self.app.root.ids.fourth.questions == Q10:
        if self.answer_user == YES:
            try:
                self.questions_players.remove(Q10)
            except ValueError:
                pass
            try:
                self.questions_players.remove(Q4)
            except ValueError:
                pass
            try:
                self.questions_players.remove(Q7)
            except ValueError:
                pass
            try:
                self.questions_players.remove(Q9)
            except ValueError:
                pass
            try:
                self.questions_players.remove(Q5)
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
                self.questions_players.remove(Q8)
            except ValueError:
                pass
        else:
            try:
                self.questions_players.remove(Q10)
            except ValueError:
                pass

    if self.app.root.ids.fourth.questions == Q3:
        try:
            self.questions_players.remove(Q3)
        except ValueError:
            pass

    if self.app.root.ids.fourth.questions == Q4:
        try:
            self.questions_players.remove(Q4)
        except ValueError:
            pass

    if self.app.root.ids.fourth.questions == Q7:
        try:
            self.questions_players.remove(Q7)
        except ValueError:
            pass

    if self.app.root.ids.fourth.questions == Q9:
        try:
            self.questions_players.remove(Q9)
        except ValueError:
            pass

    if self.app.root.ids.fourth.questions == Q8:
        try:
            self.questions_players.remove(Q8)
        except ValueError:
            pass

    if self.app.root.ids.fourth.questions == Q5:
        try:
            self.questions_players.remove(Q5)
        except ValueError:
            pass



