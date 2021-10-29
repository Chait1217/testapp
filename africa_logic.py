"""
A function that handles the logic of the questions.
"""


def africa_logic(self):
    """
    Manages the logic of the questions according to the answers given by the user
    for the countries situated in Africa.
    """
    YES = "yes"
    NO = "no"
    DNK = "dnk"
    Q1 = "Is the population of your country over 30 million?"
    Q2 = "Is the population of your country over 10 million?"
    Q3 = "Is the population of your country over 5 million?"
    Q4 = "Is your country an island?"
    Q5 = "Is French an official language in your country?"
    Q6 = "Is English an official language in your country?"
    Q7 = "Is Arabic an official language in your country?"
    Q8 = "Is Portuguese an official language in your country?"
    Q9 = "Does the flag of your country contains at least 3 or more colors?"
    Q10 = "Does the flag of your country contains red?"
    Q11 = "Does the flag of your country contains blue?"
    Q12 = "Is Islam the most practiced religion in your religion?"
    Q13 = "Does the flag of your country contains green?"
    Q14 = "Does the flag of your country contains yellow?"
    Q15 = "Is Christianity the most practiced religion in your country?"
    Q16 = "Does your country touches the Atlantic Ocean?(including The Mediterranean Sea)"
    Q17 = "Does your country touches the Indian Ocean?(including The Red Sea and The Arabian Sea)"
    Q18 = "Is there a star on the flag of your country?"
    Q19 = "Is there a moon on the flag your country?"

    if self.app.root.ids.third.questions == Q1:
        if self.answer_user == NO or self.answer_user == DNK:
            self.questions_country.remove(Q1)
        if self.answer_user == YES:
            self.questions_country.remove(Q1)
            self.questions_country.remove(Q2)
            self.questions_country.remove(Q3)
            self.questions_country.remove(Q4)

    if self.app.root.ids.third.questions == Q2:
        if self.answer_user == DNK:
            try:
                self.questions_country.remove(Q2)
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
        if self.answer_user == NO:
            try:
                self.questions_country.remove(Q2)
            except ValueError:
                pass
            try:
                self.questions_country.remove(Q1)
            except ValueError:
                pass

    if self.app.root.ids.third.questions == Q3:
        if self.answer_user == DNK:
            try:
                self.questions_country.remove(Q3)
            except ValueError:
                pass
        if self.answer_user == YES:
            try:
                self.questions_country.remove(Q3)
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
        if self.answer_user == NO or self.answer_user == DNK:
            try:
                self.questions_country.remove(Q4)
            except ValueError:
                pass
        if self.answer_user == YES:
            try:
                self.questions_country.remove(Q4)
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
                self.questions_country.remove(Q10)
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
                self.questions_country.remove(Q5)
            except ValueError:
                pass
            try:
                self.questions_country.remove(Q9)
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
                self.questions_country.remove(Q6)
            except ValueError:
                pass
            try:
                self.questions_country.remove(Q8)
            except ValueError:
                pass
            try:
                self.questions_country.remove(Q19)
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
                self.questions_country.remove(Q7)
            except ValueError:
                pass
            try:
                self.questions_country.remove(Q8)
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
                self.questions_country.remove(Q8)
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
                self.questions_country.remove(Q9)
            except ValueError:
                pass
            try:
                self.questions_country.remove(Q10)
            except ValueError:
                pass
            try:
                self.questions_country.remove(Q19)
            except ValueError:
                pass

    if self.app.root.ids.third.questions == Q9:
        if self.answer_user == YES or self.answer_user == DNK:
            try:
                self.questions_country.remove(Q8)
            except ValueError:
                pass
            try:
                self.questions_country.remove(Q9)
            except ValueError:
                pass
        if self.answer_user == NO:
            try:
                self.questions_country.remove(Q9)
            except ValueError:
                pass
            try:
                self.questions_country.remove(Q8)
            except ValueError:
                pass
            try:
                self.questions_country.remove(Q3)
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
            try:
                self.questions_country.remove(Q5)
            except ValueError:
                pass
            try:
                self.questions_country.remove(Q14)
            except ValueError:
                pass
            try:
                self.questions_country.remove(Q12)
            except ValueError:
                pass
            try:
                self.questions_country.remove(Q15)
            except ValueError:
                pass
    if self.app.root.ids.third.questions == Q10:
        if self.answer_user == YES or self.answer_user == DNK:
            try:
                self.questions_country.remove(Q10)
            except ValueError:
                pass
        if self.answer_user == NO:
            try:
                self.questions_country.remove(Q10)
            except ValueError:
                pass
            try:
                self.questions_country.remove(Q4)
            except ValueError:
                pass
            try:
                self.questions_country.remove(Q8)
            except ValueError:
                pass
            try:
                self.questions_country.remove(Q19)
            except ValueError:
                pass

    if self.app.root.ids.third.questions == Q11:
        try:
            self.questions_country.remove(Q11)
        except ValueError:
            pass

    if self.app.root.ids.third.questions == Q13:
        try:
            self.questions_country.remove(Q13)
        except ValueError:
            pass

    if self.app.root.ids.third.questions == Q14:
        try:
            self.questions_country.remove(Q14)
        except ValueError:
            pass

    if self.app.root.ids.third.questions == Q12:
        if self.answer_user == NO or self.answer_user == YES:
            try:
                self.questions_country.remove(Q12)
            except ValueError:
                pass
            try:
                self.questions_country.remove(Q15)
            except ValueError:
                pass
        if self.answer_user == DNK:
            try:
                self.questions_country.remove(Q12)
            except ValueError:
                pass
    if self.app.root.ids.third.questions == Q15:
        if self.answer_user == NO or self.answer_user == YES:
            try:
                self.questions_country.remove(Q12)
            except ValueError:
                pass
            try:
                self.questions_country.remove(Q15)
            except ValueError:
                pass
        if self.answer_user == DNK:
            try:
                self.questions_country.remove(Q15)
            except ValueError:
                pass
    if self.app.root.ids.third.questions == Q16:
        try:
            self.questions_country.remove(Q16)
        except ValueError:
            pass
    if self.app.root.ids.third.questions == Q17:
        try:
            self.questions_country.remove(Q17)
        except ValueError:
            pass

    if self.app.root.ids.third.questions == Q18:
        try:
            self.questions_country.remove(Q18)
        except ValueError:
            pass
    if self.app.root.ids.third.questions == Q19:
        if self.answer_user == DNK or self.answer_user == NO:
            try:
                self.questions_country.remove(Q19)
            except ValueError:
                pass
        if self.answer_user == YES:
            try:
                self.questions_country.remove(Q19)
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
                self.questions_country.remove(Q15)
            except ValueError:
                pass
            try:
                self.questions_country.remove(Q18)
            except ValueError:
                pass

