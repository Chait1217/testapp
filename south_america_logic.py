"""
A function that handles the logic of the questions.
"""


def south_america_logic(self):
    """
    Manages the logic of the questions according to the answers given by the user
    for the countries situated in South America.
    """
    YES = "yes"
    NO = "no"
    DNK = "dnk"
    Q1 = "Is Spanish an official language in your country?"
    Q2 = "Is the Amazon forest in your country?"
    Q3 = "Does your country touches the Atlantic Ocean?"
    Q4 = "Does your country touches the Pacific Ocean?"
    Q5 = "Does the flag of your country contains blue?"
    Q6 = "Does the flag of your country contains green?"
    Q7 = "Is the population of your country over 30 million?"
    Q8 = "Is the population of your country over 10 million?"
    Q9 = "Is the population of your country over 5 million?"
    Q10 = "Is there a star on the flag of your country?"
    Q11 = "Does the flag of your country contains red?"
    Q12 = "Is there a circled object or a sun on the flag of your country?"

    if self.app.root.ids.third.questions == Q1:
        if self.answer_user == DNK or self.answer_user == YES:
            self.questions_country.remove(Q1)
        else:
            self.questions_country.remove(Q1)
            self.questions_country.remove(Q2)
            self.questions_country.remove(Q3)
            self.questions_country.remove(Q4)
            self.questions_country.remove(Q5)
            self.questions_country.remove(Q6)

    if self.app.root.ids.third.questions == Q2:
        if self.answer_user == YES or self.answer_user == DNK:
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
                self.questions_country.remove(Q1)
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
    if self.app.root.ids.third.questions == Q7:
        if self.answer_user == NO or self.answer_user == DNK:
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
    if self.app.root.ids.third.questions == Q8:
        if self.answer_user == NO:
            try:
                self.questions_country.remove(Q8)
            except ValueError:
                pass
            try:
                self.questions_country.remove(Q7)
            except ValueError:
                pass
            try:
                self.questions_country.remove(Q4)
            except ValueError:
                pass
        if self.answer_user == YES:
            try:
                self.questions_country.remove(Q8)
            except ValueError:
                pass
            try:
                self.questions_country.remove(Q9)
            except ValueError:
                pass
        else:
            try:
                self.questions_country.remove(Q8)
            except ValueError:
                pass
    if self.app.root.ids.third.questions == Q9:
        if self.answer_user == YES or self.answer_user == DNK:
            try:
                self.questions_country.remove(Q9)
            except ValueError:
                pass
        else:
            try:
                self.questions_country.remove(Q9)
            except ValueError:
                pass
            try:
                self.questions_country.remove(Q8)
            except ValueError:
                pass
            try:
                self.questions_country.remove(Q7)
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

    if self.app.root.ids.third.questions == Q3:
        if self.answer_user == YES or self.answer_user == DNK:
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
                self.questions_country.remove(Q9)
            except ValueError:
                pass
            try:
                self.questions_country.remove(Q11)
            except ValueError:
                pass
            try:
                self.questions_country.remove(Q10)
            except ValueError:
                pass
    if self.app.root.ids.third.questions == Q4:
        if self.answer_user == NO or self.answer_user == DNK:
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
                self.questions_country.remove(Q8)
            except ValueError:
                pass
            try:
                self.questions_country.remove(Q9)
            except ValueError:
                pass
            try:
                self.questions_country.remove(Q11)
            except ValueError:
                pass
            try:
                self.questions_country.remove(Q6)
            except ValueError:
                pass
            try:
                self.questions_country.remove(Q12)
            except ValueError:
                pass

    if self.app.root.ids.third.questions == Q11:
        if self.answer_user == YES or self.answer_user == DNK:
            try:
                self.questions_country.remove(Q11)
            except ValueError:
                pass
        else:
            try:
                self.questions_country.remove(Q11)
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
                self.questions_country.remove(Q2)
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
    if self.app.root.ids.third.questions == Q6:
        if self.answer_user == NO or self.answer_user == DNK:
            try:
                self.questions_country.remove(Q6)
            except ValueError:
                pass
        else:
            try:
                self.questions_country.remove(Q6)
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
    if self.app.root.ids.third.questions == Q10:
        if self.answer_user == NO or self.answer_user == DNK:
            try:
                self.questions_country.remove(Q10)
            except ValueError:
                pass
        else:
            try:
                self.questions_country.remove(Q10)
            except ValueError:
                pass
            try:
                self.questions_country.remove(Q7)
            except ValueError:
                pass
            try:
                self.questions_country.remove(Q3)
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
    if self.app.root.ids.third.questions == Q12:
        if self.answer_user == NO or self.answer_user == DNK:
            try:
                self.questions_country.remove(Q12)
            except ValueError:
                pass
        else:
            try:
                self.questions_country.remove(Q12)
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
                self.questions_country.remove(Q10)
            except ValueError:
                pass

