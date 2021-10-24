

def europe_male_check(self):
    if self.app.root.ids.fourth.test1 == "Does your player play with pimples?":
        if self.Q == 'no' or self.Q == "dnk":
            self.questions_country.remove("Does your player play with pimples?")
        if self.Q == "yes":
            self.questions_country.remove("Does your player play with pimples?")
            self.questions_country.remove("Is your player left handed?")
            self.questions_country.remove("Has your player ever won an olympic medal in singles or in team event?")
            self.questions_country.remove("Is your player from England?")
            self.questions_country.remove("Is your player Austrian?")
            self.questions_country.remove("Is your player Croatian?")

    if self.app.root.ids.fourth.test1 == "Is your player left handed?":
        if self.Q == 'no' or self.Q == "dnk":
            try:
                self.questions_country.remove("Is your player left handed?")
            except ValueError:
                pass
        if self.Q == "yes":
            try:
                self.questions_country.remove("Is your player left handed?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Does your player serves with the backhand?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is your player from England?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is your player Austrian?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is your player Croatian?")
            except ValueError:
                pass

    if self.app.root.ids.fourth.test1 == "Is your player older than 30 years old?":
        if self.Q == 'yes' or self.Q == "dnk":
            try:
                self.questions_country.remove("Is your player older than 30 years old?")
            except ValueError:
                pass
        if self.Q == "no":
            try:
                self.questions_country.remove("Is your player older than 30 years old?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is your player Austrian?")
            except ValueError:
                pass
    if self.app.root.ids.fourth.test1 == "Did your player participate in 2016 Olympics in singles or team event?":
        if self.Q == "no":
            try:
                self.questions_country.remove("Did your player participate in 2016 Olympics in singles or team event?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is your player Austrian?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is your player from England?")
            except ValueError:
                pass
        if self.Q == 'yes' or self.Q == "dnk":
            try:
                self.questions_country.remove("Did your player participate in 2016 Olympics in singles or team event?")
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
                self.questions_country.remove("Has your player ever won an olympic medal in singles or in team event?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is your player Croatian?")
            except ValueError:
                pass
    if self.app.root.ids.fourth.test1 == "Has your player ever won an olympic medal in singles or in team event?":
        if self.Q == 'no' or self.Q == "dnk":
            try:
                self.questions_country.remove("Has your player ever won an olympic medal in singles or in team event?")
            except ValueError:
                pass
        if self.Q == "yes":
            try:
                self.questions_country.remove("Has your player ever won an olympic medal in singles or in team event?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is your player sponsored by butterfly?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Does your player serves the forehand hook serve?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is your player from England?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is your player Austrian?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is your player Croatian?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is your player Swedish?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is your player German?")
            except ValueError:
                pass
    if self.app.root.ids.fourth.test1 == "Is your player sponsored by butterfly?":
        if self.Q == 'no' or self.Q == "dnk":
            try:
                self.questions_country.remove("Is your player sponsored by butterfly?")
            except ValueError:
                pass
        if self.Q == "yes":
            try:
                self.questions_country.remove("Is your player sponsored by butterfly?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is your player from England?")
            except ValueError:
                pass

    if self.app.root.ids.fourth.test1 == "Does your player serves with the backhand?":
        if self.Q == 'no' or self.Q == "dnk":
            try:
                self.questions_country.remove("Does your player serves with the backhand?")
            except ValueError:
                pass
        if self.Q == "yes":
            try:
                self.questions_country.remove("Does your player serves with the backhand?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is your player from England?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is your player Austrian?")
            except ValueError:
                pass

    if self.app.root.ids.fourth.test1 == "Does your player serves the forehand reverse pendulum serve?":
        if self.Q == 'no' or self.Q == "dnk" or self.Q == "yes":
            try:
                self.questions_country.remove("Does your player serves the forehand reverse pendulum serve?")
            except ValueError:
                pass

    if self.app.root.ids.fourth.test1 == "Does your player serves the forehand hook serve?":
        if self.Q == 'no' or self.Q == "dnk":
            try:
                self.questions_country.remove("Does your player serves the forehand hook serve?")
            except ValueError:
                pass
        if self.Q == "yes":
            try:
                self.questions_country.remove("Does your player serves the forehand hook serve?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is your player Austrian?")
            except ValueError:
                pass

    if self.app.root.ids.fourth.test1 == "Is your player Swedish?":
        if self.Q == 'no' or self.Q == "dnk":
            try:
                self.questions_country.remove("Is your player Swedish?")
            except ValueError:
                pass
        if self.Q == "yes":
            try:
                self.questions_country.remove("Is your player Swedish?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is your player from England?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is your player Austrian?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is your player Croatian?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is your player German?")
            except ValueError:
                pass
    if self.app.root.ids.fourth.test1 == "Is your player German?":
        if self.Q == 'no' or self.Q == "dnk":
            try:
                self.questions_country.remove("Is your player German?")
            except ValueError:
                pass
        if self.Q == "yes":
            try:
                self.questions_country.remove("Is your player German?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is your player from England?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is your player Austrian?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is your player Croatian?")
            except ValueError:
                pass
    if self.app.root.ids.fourth.test1 == "Is your player from England?":
        if self.Q == 'no' or self.Q == "dnk":
            try:
                self.questions_country.remove("Is your player from England?")
            except ValueError:
                pass
        if self.Q == "yes":
            try:
                self.questions_country.remove("Is your player from England?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is your player Austrian?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is your player Croatian?")
            except ValueError:
                pass
    if self.app.root.ids.fourth.test1 == "Is your player Austrian?":
        if self.Q == 'no' or self.Q == "dnk":
            try:
                self.questions_country.remove("Is your player Austrian?")
            except ValueError:
                pass
        if self.Q == "yes":
            try:
                self.questions_country.remove("Is your player Austrian?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is your player Croatian?")
            except ValueError:
                pass
    if self.app.root.ids.fourth.test1 == "Is your player Croatian?":
        if self.Q == 'no' or self.Q == "dnk" or self.Q == "yes":
            try:
                self.questions_country.remove("Is your player Croatian?")
            except ValueError:
                pass
































