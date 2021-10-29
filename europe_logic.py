"""
A function that handles the logic of the questions.
"""


def europe_logic(self):
    """
    Manages the logic of the questions according to the answers given by the user
    for the countries situated in Europe.
    """
    YES = "yes"
    NO = "no"
    DNK = "dnk"
    Q1 = "Is Dutch an official language in your country?"
    Q2 = "Is the population of your country over 10 million?"
    Q3 = "Is the population of your country over 30 million?"
    Q4 = "Is the population of your country over 5 million?"
    Q5 = "Is English an official language in your country?"
    Q6 = "Is Italian an official language in your country?"
    Q7 = "Is German an official language in your country?"
    Q8 = "Is your country situated in the Nordic region?"
    Q9 = "Does your country touches The Mediterranean Sea?"
    Q10 = "Was your country part of Yougoslavia?"
    Q11 = "Does the flag of your country has 3 or more colors?"
    Q12 = "Does the flag of your country has a cross?"
    Q13 = "Does the flag of your country contains red?"
    Q14 = "Is your country part of the European Union?"
    Q15 = "Is Euro the official currency of your country?"
    Q16 = "Does the flag of your country has blue cross?"
    Q17 = "Is French an official language in your country?"

    if self.app.root.ids.third.questions == Q1:
        if self.answer_user == NO or self.answer_user == DNK:
            try:
                self.questions_country.remove(Q1)
            except ValueError:
                pass
        if self.answer_user == YES:
            try:
                self.questions_country.remove(Q2)
            except ValueError:
                pass
            try:
                self.questions_country.remove(Q3)
            except ValueError:
                pass
            try:
                self.questions_country.remove(Q4)
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
            try:
                self.questions_country.remove(Q7)
            except ValueError:
                pass
            try:
                self.questions_country.remove(Q8)
            except ValueError:
                pass
            try:
                self.questions_country.remove(Q9)
            except ValueError:
                pass
            try:
                self.questions_country.remove(Q10)
            except ValueError:
                pass
            try:
                self.questions_country.remove(Q11)
            except ValueError:
                pass
            try:
                self.questions_country.remove(Q12)
            except ValueError:
                pass
            try:
                self.questions_country.remove(Q13)
            except ValueError:
                pass
            try:
                self.questions_country.remove(Q14)
            except ValueError:
                pass
            try:
                self.questions_country.remove(Q15)
            except ValueError:
                pass
            try:
                self.questions_country.remove(Q16)
            except ValueError:
                pass
            try:
                self.questions_country.remove(Q1)
            except ValueError:
                pass

    if self.app.root.ids.third.questions == Q16:
        if self.answer_user == NO or self.answer_user == DNK:
            try:
                self.questions_country.remove(Q16)
            except ValueError:
                pass
        if self.answer_user == YES:
            try:
                self.questions_country.remove(Q6)
            except ValueError:
                pass
            try:
                self.questions_country.remove(Q5)
            except ValueError:
                pass
            try:
                self.questions_country.remove(Q7)
            except ValueError:
                pass
            try:
                self.questions_country.remove(Q8)
            except ValueError:
                pass
            try:
                self.questions_country.remove(Q10)
            except ValueError:
                pass
            try:
                self.questions_country.remove(Q16)
            except ValueError:
                pass
            try:
                self.questions_country.remove(Q1)
            except ValueError:
                pass
            try:
                self.questions_country.remove(Q17)
            except ValueError:
                pass
            try:
                self.questions_country.remove(Q2)
            except ValueError:
                pass
            try:
                self.questions_country.remove(Q3)
            except ValueError:
                pass
            try:
                self.questions_country.remove(Q4)
            except ValueError:
                pass
            try:
                self.questions_country.remove(Q9)
            except ValueError:
                pass
            try:
                self.questions_country.remove(Q8)
            except ValueError:
                pass
            try:
                self.questions_country.remove(Q12)
            except ValueError:
                pass

    if self.app.root.ids.third.questions == Q5:
        if self.answer_user == NO or self.answer_user == DNK:
            try:
                self.questions_country.remove(Q5)
            except ValueError:
                pass
        if self.answer_user == YES:
            try:
                self.questions_country.remove(Q6)
            except ValueError:
                pass
            try:
                self.questions_country.remove(Q5)
            except ValueError:
                pass
            try:
                self.questions_country.remove(Q7)
            except ValueError:
                pass
            try:
                self.questions_country.remove(Q8)
            except ValueError:
                pass
            try:
                self.questions_country.remove(Q10)
            except ValueError:
                pass
            try:
                self.questions_country.remove(Q16)
            except ValueError:
                pass
            try:
                self.questions_country.remove(Q1)
            except ValueError:
                pass
            try:
                self.questions_country.remove(Q17)
            except ValueError:
                pass

    if self.app.root.ids.third.questions == Q6:
        if self.answer_user == NO or self.answer_user == DNK:
            try:
                self.questions_country.remove(Q6)
            except ValueError:
                pass
        if self.answer_user == YES:
            try:
                self.questions_country.remove(Q5)
            except ValueError:
                pass
            try:
                self.questions_country.remove(Q6)
            except ValueError:
                pass
            try:
                self.questions_country.remove(Q8)
            except ValueError:
                pass
            try:
                self.questions_country.remove(Q10)
            except ValueError:
                pass
            try:
                self.questions_country.remove(Q16)
            except ValueError:
                pass
            try:
                self.questions_country.remove(Q1)
            except ValueError:
                pass

    if self.app.root.ids.third.questions == Q17:
        if self.answer_user == NO or self.answer_user == DNK:
            try:
                self.questions_country.remove(Q17)
            except ValueError:
                pass
        if self.answer_user == YES:
            try:
                self.questions_country.remove(Q5)
            except ValueError:
                pass
            try:
                self.questions_country.remove(Q17)
            except ValueError:
                pass
            try:
                self.questions_country.remove(Q8)
            except ValueError:
                pass
            try:
                self.questions_country.remove(Q10)
            except ValueError:
                pass
            try:
                self.questions_country.remove(Q16)
            except ValueError:
                pass

    if self.app.root.ids.third.questions == Q7:
        if self.answer_user == NO or self.answer_user == DNK:
            try:
                self.questions_country.remove(Q7)
            except ValueError:
                pass
        if self.answer_user == YES:
            try:
                self.questions_country.remove(Q5)
            except ValueError:
                pass
            try:
                self.questions_country.remove(Q7)
            except ValueError:
                pass
            try:
                self.questions_country.remove(Q8)
            except ValueError:
                pass
            try:
                self.questions_country.remove(Q9)
            except ValueError:
                pass
            try:
                self.questions_country.remove(Q10)
            except ValueError:
                pass
            try:
                self.questions_country.remove(Q13)
            except ValueError:
                pass
            try:
                self.questions_country.remove(Q16)
            except ValueError:
                pass

    if self.app.root.ids.third.questions == Q8:
        if self.answer_user == NO or self.answer_user == DNK:
            try:
                self.questions_country.remove(Q8)
            except ValueError:
                pass
        if self.answer_user == YES:
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
            try:
                self.questions_country.remove(Q7)
            except ValueError:
                pass
            try:
                self.questions_country.remove(Q8)
            except ValueError:
                pass
            try:
                self.questions_country.remove(Q9)
            except ValueError:
                pass
            try:
                self.questions_country.remove(Q10)
            except ValueError:
                pass
            try:
                self.questions_country.remove(Q12)
            except ValueError:
                pass
            try:
                self.questions_country.remove(Q17)
            except ValueError:
                pass

    if self.app.root.ids.third.questions == Q9:
        if self.answer_user == NO or self.answer_user == DNK:
            try:
                self.questions_country.remove(Q9)
            except ValueError:
                pass
        if self.answer_user == YES:
            try:
                self.questions_country.remove(Q7)
            except ValueError:
                pass
            try:
                self.questions_country.remove(Q8)
            except ValueError:
                pass
            try:
                self.questions_country.remove(Q9)
            except ValueError:
                pass
            try:
                self.questions_country.remove(Q16)
            except ValueError:
                pass

    if self.app.root.ids.third.questions == Q10:
        if self.answer_user == NO or self.answer_user == DNK:
            try:
                self.questions_country.remove(Q10)
            except ValueError:
                pass
        if self.answer_user == YES:
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
            try:
                self.questions_country.remove(Q7)
            except ValueError:
                pass
            try:
                self.questions_country.remove(Q8)
            except ValueError:
                pass
            try:
                self.questions_country.remove(Q10)
            except ValueError:
                pass
            try:
                self.questions_country.remove(Q12)
            except ValueError:
                pass
            try:
                self.questions_country.remove(Q16)
            except ValueError:
                pass
            try:
                self.questions_country.remove(Q1)
            except ValueError:
                pass
            try:
                self.questions_country.remove(Q17)
            except ValueError:
                pass

    if self.app.root.ids.third.questions == Q11:
        if self.answer_user == YES or self.answer_user == DNK:
            try:
                self.questions_country.remove(Q11)
            except ValueError:
                pass
        if self.answer_user == NO:
            try:
                self.questions_country.remove(Q11)
            except ValueError:
                pass
            try:
                self.questions_country.remove(Q1)
            except ValueError:
                pass

    if self.app.root.ids.third.questions == Q12:
        if self.answer_user == NO or self.answer_user == DNK:
            try:
                self.questions_country.remove(Q12)
            except ValueError:
                pass
        if self.answer_user == YES:
            try:
                self.questions_country.remove(Q10)
            except ValueError:
                pass
            try:
                self.questions_country.remove(Q12)
            except ValueError:
                pass
            try:
                self.questions_country.remove(Q1)
            except ValueError:
                pass

    if self.app.root.ids.third.questions == Q13:
        if self.answer_user == YES or self.answer_user == DNK:
            try:
                self.questions_country.remove(Q13)
            except ValueError:
                pass
        if self.answer_user == NO:
            try:
                self.questions_country.remove(Q7)
            except ValueError:
                pass
            try:
                self.questions_country.remove(Q13)
            except ValueError:
                pass
            try:
                self.questions_country.remove(Q1)
            except ValueError:
                pass
            try:
                self.questions_country.remove(Q17)
            except ValueError:
                pass

    if self.app.root.ids.third.questions == Q3:
        if self.answer_user == NO or self.answer_user == DNK:
            try:
                self.questions_country.remove(Q3)
            except ValueError:
                pass

        if self.answer_user == YES:
            try:
                self.questions_country.remove(Q2)
            except ValueError:
                pass
            try:
                self.questions_country.remove(Q3)
            except ValueError:
                pass
            try:
                self.questions_country.remove(Q4)
            except ValueError:
                pass
            try:
                self.questions_country.remove(Q1)
            except ValueError:
                pass
            try:
                self.questions_country.remove(Q16)
            except ValueError:
                pass
            try:
                self.questions_country.remove(Q8)
            except ValueError:
                pass
            try:
                self.questions_country.remove(Q10)
            except ValueError:
                pass

    if self.app.root.ids.third.questions == Q2:
        if self.answer_user == DNK:
            try:
                self.questions_country.remove(Q2)
            except ValueError:
                pass

        if self.answer_user == YES:
            try:
                self.questions_country.remove(Q4)
            except ValueError:
                pass
            try:
                self.questions_country.remove(Q10)
            except ValueError:
                pass
            try:
                self.questions_country.remove(Q16)
            except ValueError:
                pass
            try:
                self.questions_country.remove(Q2)
            except ValueError:
                pass
        if self.answer_user == NO:
            try:
                self.questions_country.remove(Q3)
            except ValueError:
                pass
            try:
                self.questions_country.remove(Q2)
            except ValueError:
                pass
            try:
                self.questions_country.remove(Q1)
            except ValueError:
                pass

    if self.app.root.ids.third.questions == Q4:
        if self.answer_user == YES or self.answer_user == DNK:
            try:
                self.questions_country.remove(Q4)
            except ValueError:
                pass

        if self.answer_user == NO:
            try:
                self.questions_country.remove(Q2)
            except ValueError:
                pass
            try:
                self.questions_country.remove(Q3)
            except ValueError:
                pass
            try:
                self.questions_country.remove(Q4)
            except ValueError:
                pass
    if self.app.root.ids.third.questions == Q14:
        try:
            self.questions_country.remove(Q14)
        except ValueError:
            pass

    if self.app.root.ids.third.questions == Q15:
        try:
            self.questions_country.remove(Q15)
        except ValueError:
            pass

