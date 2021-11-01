"""
A function that handles the logic of the questions.
"""


def oceania_logic(self):
    """
    Manages the logic of the questions according to the answers given by the user
    for the countries situated in Oceania.
    """
    YES = "yes"
    NO = "no"
    DNK = "dnk"
    Q1 = "Is the population of your country over 10 million?"
    Q2 = "Is the population of your country over 1 million?"
    Q3 = "Does the flag of your country contains green?"
    Q4 = "Does the flag of your country contains blue?"
    Q5 = "Is there a star on the flag of your country?"
    Q6 = "Does the flag of your country contains red?"
    Q7 = "Does the flag of your country contains yellow?"

    if self.app.root.ids.third.questions == Q1:
        if self.answer_user == NO or self.answer_user == DNK:
            self.questions_country.remove(Q1)
        else:
            self.questions_country.remove(Q1)
            self.questions_country.remove(Q2)
            self.questions_country.remove(Q3)
            self.questions_country.remove(Q4)
            self.questions_country.remove(Q5)
            self.questions_country.remove(Q6)
            self.questions_country.remove(Q7)
    if self.app.root.ids.third.questions == Q2:
        if self.answer_user == NO or self.answer_user == DNK:
            try:
                self.questions_country.remove(Q2)
            except ValueError:
                pass
        else:
            try:
                self.questions_country.remove(Q2)
            except ValueError:
                pass
            try:
                self.questions_country.remove(Q3)
            except ValueError:
                pass
            try:
                self.questions_country.remove(Q5)
            except ValueError:
                pass
            try:
                self.questions_country.remove(Q6)
            except ValueError:
                pass

    if self.app.root.ids.third.questions == Q3:
        if self.answer_user == NO or self.answer_user == DNK:
            try:
                self.questions_country.remove(Q3)
            except ValueError:
                pass
        else:
            try:
                self.questions_country.remove(Q3)
            except ValueError:
                pass
            try:
                self.questions_country.remove(Q1)
            except ValueError:
                pass
            try:
                self.questions_country.remove(Q2)
            except ValueError:
                pass
            try:
                self.questions_country.remove(Q7)
            except ValueError:
                pass
    if self.app.root.ids.third.questions == Q4:
        if self.answer_user == YES or self.answer_user == DNK:
            try:
                self.questions_country.remove(Q4)
            except ValueError:
                pass
        else:
            try:
                self.questions_country.remove(Q4)
            except ValueError:
                pass
            try:
                self.questions_country.remove(Q1)
            except ValueError:
                pass
            try:
                self.questions_country.remove(Q6)
            except ValueError:
                pass
    if self.app.root.ids.third.questions == Q5:
        if self.answer_user == YES or self.answer_user == DNK:
            try:
                self.questions_country.remove(Q5)
            except ValueError:
                pass
        else:
            try:
                self.questions_country.remove(Q5)
            except ValueError:
                pass
            try:
                self.questions_country.remove(Q1)
            except ValueError:
                pass
            try:
                self.questions_country.remove(Q2)
            except ValueError:
                pass
            try:
                self.questions_country.remove(Q2)
            except ValueError:
                pass
    if self.app.root.ids.third.questions == Q6:
        if self.answer_user == YES or self.answer_user == DNK:
            try:
                self.questions_country.remove(Q6)
            except ValueError:
                pass
        else:
            try:
                self.questions_country.remove(Q1)
            except ValueError:
                pass
            try:
                self.questions_country.remove(Q2)
            except ValueError:
                pass
            try:
                self.questions_country.remove(Q4)
            except ValueError:
                pass

    if self.app.root.ids.third.questions == Q7:
        if self.answer_user == DNK:
            try:
                self.questions_country.remove(Q7)
            except ValueError:
                pass
        if self.answer_user == NO:
            try:
                self.questions_country.remove(Q3)
            except ValueError:
                pass
            try:
                self.questions_country.remove(Q7)
            except ValueError:
                pass
        else:
            try:
                self.questions_country.remove(Q7)
            except ValueError:
                pass
            try:
                self.questions_country.remove(Q1)
            except ValueError:
                pass

