
def americas_male_check(self):
    if self.app.root.ids.fourth.test1 == "Is your player left handed?":
        if self.Q == 'no' or self.Q == "dnk":
            self.questions_country.remove("Is your player left handed?")
        if self.Q == "yes":
            self.questions_country.remove("Is your player left handed?")
            self.questions_country.remove("Did your player participate in 2016 Olympics in singles or team event?")
            self.questions_country.remove("Is your player sponsored by butterfly?")
            self.questions_country.remove("Is your player Argentinian?")
            self.questions_country.remove("Is your player ranked in the top 30 of the world?")
            self.questions_country.remove("Is your player known for his shots with two hands?")

    if self.app.root.ids.fourth.test1 == "Is your player older than 30 years old?":
        if self.Q == 'no' or self.Q == "dnk":
            try:
                self.questions_country.remove("Is your player older than 30 years old?")
            except ValueError:
                pass
        if self.Q == "yes":
            try:
                self.questions_country.remove("Is your player older than 30 years old?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is your player ranked in the top 30 of the world?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is your player known for his shots with two hands?")
            except ValueError:
                pass
    if self.app.root.ids.fourth.test1 == "Did your player participate in 2016 Olympics in singles or team event?":
        if self.Q == "dnk":
            try:
                self.questions_country.remove("Did your player participate in 2016 Olympics in singles or team event?")
            except ValueError:
                pass
        if self.Q == "yes":
            try:
                self.questions_country.remove("Did your player participate in 2016 Olympics in singles or team event?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is your player Argentinian?")
            except ValueError:
                pass

        if self.Q == 'no':
            try:
                self.questions_country.remove("Did your player participate in 2016 Olympics in singles or team event?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is your player ranked in the top 30 of the world?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is your player known for his shots with two hands?")
            except ValueError:
                pass

    if self.app.root.ids.fourth.test1 == "Did your player participate in 2021 Olympics in singles or team event?":
        if self.Q == 'yes' or self.Q == "dnk":
            try:
                self.questions_country.remove("Did your player participate in 2021 Olympics in singles or team event?")
            except ValueError:
                pass

        if self.Q == "no":
            try:
                self.questions_country.remove("Did your player participate in 2021 Olympics in singles or team event?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is your player Argentinian?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is your player ranked in the top 30 of the world?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is your player known for his shots with two hands?")
            except ValueError:
                pass
    if self.app.root.ids.fourth.test1 == "Is your player sponsored by butterfly?":
        if self.Q == "no" or self.Q == "dnk":
            try:
                self.questions_country.remove("Is your player sponsored by butterfly?")
            except ValueError:
                pass
        if self.Q == 'yes':
            try:
                self.questions_country.remove("Is your player sponsored by butterfly?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is your player Argentinian?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is your player known for his shots with two hands?")
            except ValueError:
                pass
    if self.app.root.ids.fourth.test1 == "Is your player Argentinian?":
        if self.Q == "no" or self.Q == "dnk":
            try:
                self.questions_country.remove("Is your player Argentinian?")
            except ValueError:
                pass
        if self.Q == 'yes':
            try:
                self.questions_country.remove("Is your player Argentinian?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is your player ranked in the top 30 of the world?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is your player known for his shots with two hands?")
            except ValueError:
                pass
    if self.app.root.ids.fourth.test1 == "Is your player ranked in the top 30 of the world?":
        if self.Q == "yes" or self.Q == "dnk":
            try:
                self.questions_country.remove("Is your player ranked in the top 30 of the world?")
            except ValueError:
                pass
        if self.Q == 'no':
            try:
                self.questions_country.remove("Is your player ranked in the top 30 of the world?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is your player known for his shots with two hands?")
            except ValueError:
                pass
    if self.app.root.ids.fourth.test1 == "Is your player known for his shots with two hands?":
        if self.Q == "yes" or self.Q == "dnk" or self.Q == "no":
            try:
                self.questions_country.remove("Is your player known for his shots with two hands?")
            except ValueError:
                pass
