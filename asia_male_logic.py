

def asia_male_check(self):
    if self.app.root.ids.fourth.test1 == "Is your player left handed?":
        if self.Q == 'no' or self.Q == "dnk":
            self.questions_country.remove("Is your player left handed?")
        if self.Q == "yes":
            self.questions_country.remove("Is your player left handed?")
            self.questions_country.remove("Is your player Indian?")

    if self.app.root.ids.fourth.test1 == "Does your player play with the pen hold grip?":
        if self.Q == 'no' or self.Q == "dnk":
            try:
                self.questions_country.remove("Does your player play with the pen hold grip?")
            except ValueError:
                pass
        if self.Q == "yes":
            try:
                self.questions_country.remove("Does your player play with the pen hold grip?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is your player Indian?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is your player Korean?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Does your player serves the forehand reverse pendulum serve?")
            except ValueError:
                pass
    if self.app.root.ids.fourth.test1 == "Is your player older than 30 years old?":
        if self.Q == 'no' or self.Q == "dnk" or self.Q == "yes":
            try:
                self.questions_country.remove("Is your player older than 30 years old?")
            except ValueError:
                pass

    if self.app.root.ids.fourth.test1 == "Did your player participate in 2016 Olympics in singles or team event?":
        if self.Q == 'no' or self.Q == "dnk" or self.Q == "yes":
            try:
                self.questions_country.remove("Did your player participate in 2016 Olympics in singles or team event?")
            except ValueError:
                pass

    if self.app.root.ids.fourth.test1 == "Did your player participate in 2021 Olympics in singles or team event?":
        if self.Q == 'no' or self.Q == "dnk" or self.Q == "yes":
            try:
                self.questions_country.remove("Did your player participate in 2021 Olympics in singles or team event?")
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
                self.questions_country.remove("Is your player Indian?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is your player Korean?")
            except ValueError:
                pass
    if self.app.root.ids.fourth.test1 == "Is your player sponsored by butterfly?":
        if self.Q == 'no' or self.Q == "dnk" or self.Q == "yes":
            try:
                self.questions_country.remove("Is your player sponsored by butterfly?")
            except ValueError:
                pass
    if self.app.root.ids.fourth.test1 == "Is your player Chinese?":
        if self.Q == 'no' or self.Q == "dnk":
            try:
                self.questions_country.remove("Is your player Chinese?")
            except ValueError:
                pass
        if self.Q == "yes":
            try:
                self.questions_country.remove("Is your player Chinese?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is your player Indian?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is your player Korean?")
            except ValueError:
                pass
    if self.app.root.ids.fourth.test1 == "Is your player Korean?":
        if self.Q == 'no' or self.Q == "dnk":
            try:
                self.questions_country.remove("Is your player Korean?")
            except ValueError:
                pass
        if self.Q == "yes":
            try:
                self.questions_country.remove("Is your player Indian?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is your player Korean?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Does your player serves the forehand reverse pendulum serve?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Does your player serves the forehand hook serve?")
            except ValueError:
                pass
    if self.app.root.ids.fourth.test1 == "Is your player Indian?":
        if self.Q == 'no' or self.Q == "dnk":
            try:
                self.questions_country.remove("Is your player Indian?")
            except ValueError:
                pass
        if self.Q == "yes":
            try:
                self.questions_country.remove("Is your player Indian?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Does your player serves the forehand hook serve?")
            except ValueError:
                pass
    if self.app.root.ids.fourth.test1 == "Does your player serves the forehand reverse pendulum serve?":
        if self.Q == 'no' or self.Q == "dnk":
            try:
                self.questions_country.remove("Does your player serves the forehand reverse pendulum serve?")
            except ValueError:
                pass
        if self.Q == "yes":
            try:
                self.questions_country.remove("Does your player serves the forehand reverse pendulum serve?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Does your player serves the forehand hook serve?")
            except ValueError:
                pass
    if self.app.root.ids.fourth.test1 == "Does your player serves the forehand hook serve?":
        if self.Q == 'no' or self.Q == "dnk" or self.Q == "yes":
            try:
                self.questions_country.remove("Does your player serves the forehand hook serve?")
            except ValueError:
                pass





















