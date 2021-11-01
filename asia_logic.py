"""
A function that handles the logic of the questions.
"""


def asia_logic(self):
    """
    Manages the logic of the questions according to the answers given by the user
    for the countries situated in Asia.
    """
    YES = "yes"
    NO = "no"
    DNK = "dnk"
    Q1 = "Is the population of your country over 100 million?"
    Q2 = "Is the population of your country over 30 million?"
    Q3 = "Is the population of your country over 10 million?"
    Q4 = "Is the population of your country over 5 million?"
    Q5 = "Is your country situated in Middle East region?"
    Q6 = "Is Arabic an official language in your country?"
    Q7 = "Is Folk religion the most practiced religion in your country?"
    Q8 = "Is Hinduism the most practiced religion in your country?"
    Q9 = "Is there a circled object or a sun on the flag of your country?"
    Q10 = "Is Christianity the most practiced religion in your country?"
    Q11 = "Is Buddhism the most practiced religion in your country?"
    Q12 = "Is your country an island?"
    Q13 = "Does your country touches the Pacific Ocean?"
    Q14 = "Does the flag of your country contains yellow?"
    Q15 = "Is there a moon on the flag your country?"
    Q16 = "Is Islam the most practiced religion in your religion?"
    Q17 = "Does the flag of your country contains blue?"
    Q18 = "Is there a star on the flag of your country?"
    Q19 = "Does your country touches the Indian Ocean?"
    Q20 = "Does the flag of your country contains red?"
    Q21 = "Does the flag of your country contains green?"

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

    if self.app.root.ids.third.questions == Q2:
        if self.answer_user == DNK:
            try:
                self.questions_country.remove(Q2)
            except ValueError:
                pass
        if self.answer_user == NO:
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
                self.questions_country.remove(Q4)
            except ValueError:
                pass

    if self.app.root.ids.third.questions == Q3:
        if self.answer_user == DNK:
            try:
                self.questions_country.remove(Q3)
            except ValueError:
                pass
        if self.answer_user == NO:
            try:
                self.questions_country.remove(Q1)
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
                self.questions_country.remove(Q7)
            except ValueError:
                pass
            try:
                self.questions_country.remove(Q8)
            except ValueError:
                pass
        else:
            try:
                self.questions_country.remove(Q3)
            except ValueError:
                pass
            try:
                self.questions_country.remove(Q4)
            except ValueError:
                pass

    if self.app.root.ids.third.questions == Q4:
        if self.answer_user == DNK:
            try:
                self.questions_country.remove(Q4)
            except ValueError:
                pass
        if self.answer_user == YES:
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
            try:
                self.questions_country.remove(Q8)
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

    if self.app.root.ids.third.questions == Q5:
        if self.answer_user == DNK or self.answer_user == NO:
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
                self.questions_country.remove(Q8)
            except ValueError:
                pass
            try:
                self.questions_country.remove(Q7)
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
                self.questions_country.remove(Q9)
            except ValueError:
                pass
    if self.app.root.ids.third.questions == Q6:
        if self.answer_user == DNK or self.answer_user == NO:
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
                self.questions_country.remove(Q1)
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
                self.questions_country.remove(Q10)
            except ValueError:
                pass
            try:
                self.questions_country.remove(Q11)
            except ValueError:
                pass
            try:
                self.questions_country.remove(Q16)
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
                self.questions_country.remove(Q17)
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
                self.questions_country.remove(Q9)
            except ValueError:
                pass

    if self.app.root.ids.third.questions == Q8:
        if self.answer_user == DNK or self.answer_user == NO:
            try:
                self.questions_country.remove(Q8)
            except ValueError:
                pass
        else:
            try:
                self.questions_country.remove(Q8)
            except ValueError:
                pass
            try:
                self.questions_country.remove(Q4)
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
                self.questions_country.remove(Q8)
            except ValueError:
                pass
            try:
                self.questions_country.remove(Q7)
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
                self.questions_country.remove(Q16)
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
                self.questions_country.remove(Q17)
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
                self.questions_country.remove(Q18)
            except ValueError:
                pass
    if self.app.root.ids.third.questions == Q7:
        if self.answer_user == DNK or self.answer_user == NO:
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
                self.questions_country.remove(Q4)
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
                self.questions_country.remove(Q11)
            except ValueError:
                pass
            try:
                self.questions_country.remove(Q16)
            except ValueError:
                pass
            try:
                self.questions_country.remove(Q12)
            except ValueError:
                pass
            try:
                self.questions_country.remove(Q19)
            except ValueError:
                pass
            try:
                self.questions_country.remove(Q13)
            except ValueError:
                pass
            try:
                self.questions_country.remove(Q17)
            except ValueError:
                pass
            try:
                self.questions_country.remove(Q14)
            except ValueError:
                pass
            try:
                self.questions_country.remove(Q20)
            except ValueError:
                pass
            try:
                self.questions_country.remove(Q21)
            except ValueError:
                pass
            try:
                self.questions_country.remove(Q18)
            except ValueError:
                pass
            try:
                self.questions_country.remove(Q15)
            except ValueError:
                pass
            try:
                self.questions_country.remove(Q9)
            except ValueError:
                pass
    if self.app.root.ids.third.questions == Q10:
        if self.answer_user == DNK or self.answer_user == NO:
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
                self.questions_country.remove(Q5)
            except ValueError:
                pass
            try:
                self.questions_country.remove(Q6)
            except ValueError:
                pass
            try:
                self.questions_country.remove(Q11)
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
                self.questions_country.remove(Q7)
            except ValueError:
                pass
            try:
                self.questions_country.remove(Q20)
            except ValueError:
                pass
            try:
                self.questions_country.remove(Q21)
            except ValueError:
                pass
            try:
                self.questions_country.remove(Q15)
            except ValueError:
                pass
    if self.app.root.ids.third.questions == Q11:
        if self.answer_user == DNK or self.answer_user == NO:
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
                self.questions_country.remove(Q5)
            except ValueError:
                pass
            try:
                self.questions_country.remove(Q6)
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
                self.questions_country.remove(Q7)
            except ValueError:
                pass
    if self.app.root.ids.third.questions == Q16:
        if self.answer_user == DNK:
            try:
                self.questions_country.remove(Q16)
            except ValueError:
                pass
        if self.answer_user == NO:
            try:
                self.questions_country.remove(Q16)
            except ValueError:
                pass
            try:
                self.questions_country.remove(Q6)
            except ValueError:
                pass
        else:
            try:
                self.questions_country.remove(Q16)
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
            try:
                self.questions_country.remove(Q8)
            except ValueError:
                pass
            try:
                self.questions_country.remove(Q7)
            except ValueError:
                pass

    if self.app.root.ids.third.questions == Q12:
        if self.answer_user == DNK or self.answer_user == NO:
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
                self.questions_country.remove(Q7)
            except ValueError:
                pass
            try:
                self.questions_country.remove(Q20)
            except ValueError:
                pass

    if self.app.root.ids.third.questions == Q19:
        if self.answer_user == DNK or self.answer_user == NO:
            try:
                self.questions_country.remove(Q19)
            except ValueError:
                pass
        else:
            try:
                self.questions_country.remove(Q19)
            except ValueError:
                pass
            try:
                self.questions_country.remove(Q7)
            except ValueError:
                pass

    if self.app.root.ids.third.questions == Q13:
        if self.answer_user == DNK or self.answer_user == NO:
            try:
                self.questions_country.remove(Q13)
            except ValueError:
                pass
        else:
            try:
                self.questions_country.remove(Q13)
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
                self.questions_country.remove(Q8)
            except ValueError:
                pass
            try:
                self.questions_country.remove(Q20)
            except ValueError:
                pass
            try:
                self.questions_country.remove(Q21)
            except ValueError:
                pass

    if self.app.root.ids.third.questions == Q20:
        if self.answer_user == DNK or self.answer_user == YES:
            try:
                self.questions_country.remove(Q20)
            except ValueError:
                pass
        else:
            try:
                self.questions_country.remove(Q20)
            except ValueError:
                pass
            try:
                self.questions_country.remove(Q7)
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
                self.questions_country.remove(Q13)
            except ValueError:
                pass

    if self.app.root.ids.third.questions == Q17:
        if self.answer_user == DNK or self.answer_user == NO:
            try:
                self.questions_country.remove(Q17)
            except ValueError:
                pass
        else:
            try:
                self.questions_country.remove(Q17)
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

    if self.app.root.ids.third.questions == Q21:
        if self.answer_user == DNK or self.answer_user == NO:
            try:
                self.questions_country.remove(Q21)
            except ValueError:
                pass
        else:
            try:
                self.questions_country.remove(Q21)
            except ValueError:
                pass
            try:
                self.questions_country.remove(Q7)
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

    if self.app.root.ids.third.questions == Q14:
        if self.answer_user == DNK or self.answer_user == NO:
            try:
                self.questions_country.remove(Q14)
            except ValueError:
                pass
        else:
            try:
                self.questions_country.remove(Q14)
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
                self.questions_country.remove(Q8)
            except ValueError:
                pass

    if self.app.root.ids.third.questions == Q18:
        if self.answer_user == DNK:
            try:
                self.questions_country.remove(Q18)
            except ValueError:
                pass
        if self.answer_user == NO:
            try:
                self.questions_country.remove(Q18)
            except ValueError:
                pass
            try:
                self.questions_country.remove(Q7)
            except ValueError:
                pass

        else:
            try:
                self.questions_country.remove(Q18)
            except ValueError:
                pass
            try:
                self.questions_country.remove(Q8)
            except ValueError:
                pass

    if self.app.root.ids.third.questions == Q15:
        if self.answer_user == DNK or self.answer_user == NO:
            try:
                self.questions_country.remove(Q15)
            except ValueError:
                pass
        else:
            try:
                self.questions_country.remove(Q15)
            except ValueError:
                pass
            try:
                self.questions_country.remove(Q8)
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
                self.questions_country.remove(Q10)
            except ValueError:
                pass
            try:
                self.questions_country.remove(Q9)
            except ValueError:
                pass

    if self.app.root.ids.third.questions == Q9:
        if self.answer_user == DNK or self.answer_user == NO:
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
                self.questions_country.remove(Q15)
            except ValueError:
                pass
