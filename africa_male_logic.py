
def africa_male_check(self):
    if self.app.root.ids.fourth.test1 == "Is your player older than 30 years?":
        if self.Q == 'no' or self.Q == "dnk" or self.Q == "yes":
            self.questions_country.remove("Is your player older than 30 years?")
    if self.app.root.ids.fourth.test1 == "Did your player participate in 2016 Olympics in singles or team event?":
        if self.Q == "dnk":
            try:
                self.questions_country.remove("Did your player participate in 2016 Olympics in singles or team event?")
            except ValueError:
                pass
        if self.Q == 'no':
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
        if self.Q == "yes":
            try:
                self.questions_country.remove("Did your player participate in 2016 Olympics in singles or team event?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Did your player participate in 2021 Olympics in singles or team event?")
            except ValueError:
                pass
    if self.app.root.ids.fourth.test1 == "Did your player participate in 2021 Olympics in singles or team event?":
        if self.Q == "dnk":
            try:
                self.questions_country.remove("Did your player participate in 2021 Olympics in singles or team event?")
            except ValueError:
                pass
        if self.Q == "yes":
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

        if self.Q == 'no':
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
    if self.app.root.ids.fourth.test1 == "Is your player sponsored by gewo?":
        if self.Q == "yes":
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
        if self.Q == 'no':
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
        if self.Q == "dnk":
            try:
                self.questions_country.remove("Is your player sponsored by gewo?")
            except ValueError:
                pass

    if self.app.root.ids.fourth.test1 == "Is he known for his extremely powerful forehand?":
        if self.Q == 'yes' or self.Q == "dnk" or self.Q == "no":
            try:
                self.questions_country.remove("Is he known for his extremely powerful forehand?")
            except ValueError:
                pass

    if self.app.root.ids.fourth.test1 == "Did he reach the quarter finals in 2021 olympics in singles?":
        if self.Q == 'yes' or self.Q == "dnk" or self.Q == "no":
            try:
                self.questions_country.remove("Did he reach the quarter finals in 2021 olympics in singles?")
            except ValueError:
                pass

    if self.app.root.ids.fourth.test1 == "Is your player older than 40 years old?":
        if self.Q == 'yes' or self.Q == "dnk" or self.Q == "no":
            try:
                self.questions_country.remove("Is your player older than 40 years old?")
            except ValueError:
                pass

    if self.app.root.ids.fourth.test1 == "Did he use to represent france when he was under 18?":
        if self.Q == 'yes' or self.Q == "dnk" or self.Q == "no":
            try:
                self.questions_country.remove("Did he use to represent france when he was under 18?")
            except ValueError:
                pass

    if self.app.root.ids.fourth.test1 == "Is your player the 2nd best player of nigeria?":
        if self.Q == 'yes' or self.Q == "dnk" or self.Q == "no":
            try:
                self.questions_country.remove("Is your player the 2nd best player of nigeria?")
            except ValueError:
                pass

    if self.app.root.ids.fourth.test1 == "Is your player sponsored by butterfly?":
        if self.Q == 'yes' or self.Q == "dnk" or self.Q == "no":
            try:
                self.questions_country.remove("Is your player sponsored by butterfly?")
            except ValueError:
                pass




