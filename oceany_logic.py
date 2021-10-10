


def oceany_logic(self):
    if self.app.root.ids.third.test1 == "Is the population of your country over 10 million?":
        if self.Q == 'no' or self.Q == "dnk":
            self.questions_country.remove("Is the population of your country over 10 million?")
        if self.Q == 'yes':
            self.questions_country.remove("Is the population of your country over 10 million?")
            self.questions_country.remove("Is the population of your country over 1 million?")
            self.questions_country.remove("Does the flag of your country contains green?")
            self.questions_country.remove("Does the flag of your country contains blue?")
            self.questions_country.remove("Is there a star on the flag of your country?")
            self.questions_country.remove("Does the flag of your country contains red?")
            self.questions_country.remove("Does the flag of your country contains yellow?")
    if self.app.root.ids.third.test1 == "Is the population of your country over 1 million?":
        if self.Q == 'no' or self.Q == "dnk":
            try:
                self.questions_country.remove("Is the population of your country over 1 million?")
            except ValueError:
                pass
        if self.Q == 'yes':
            try:
                self.questions_country.remove("Is the population of your country over 1 million?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Does the flag of your country contains green?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is there a star on the flag of your country?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Does the flag of your country contains red?")
            except ValueError:
                pass

    if self.app.root.ids.third.test1 == "Does the flag of your country contains green?":
        if self.Q == 'no' or self.Q == "dnk":
            try:
                self.questions_country.remove("Does the flag of your country contains green?")
            except ValueError:
                pass
        if self.Q == 'yes':
            try:
                self.questions_country.remove("Does the flag of your country contains green?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is the population of your country over 10 million?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is the population of your country over 1 million?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Does the flag of your country contains yellow?")
            except ValueError:
                pass
    if self.app.root.ids.third.test1 == "Does the flag of your country contains blue?":
        if self.Q == 'yes' or self.Q == "dnk":
            try:
                self.questions_country.remove("Does the flag of your country contains blue?")
            except ValueError:
                pass
        if self.Q == 'no':
            try:
                self.questions_country.remove("Does the flag of your country contains blue?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is the population of your country over 10 million?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Does the flag of your country contains red?")
            except ValueError:
                pass
    if self.app.root.ids.third.test1 == "Is there a star on the flag of your country?":
        if self.Q == 'yes' or self.Q == "dnk":
            try:
                self.questions_country.remove("Is there a star on the flag of your country?")
            except ValueError:
                pass
        if self.Q == 'no':
            try:
                self.questions_country.remove("Is there a star on the flag of your country?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is the population of your country over 10 million?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is the population of your country over 1 million?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is the population of your country over 1 million?")
            except ValueError:
                pass
    if self.app.root.ids.third.test1 == "Does the flag of your country contains red?":
        if self.Q == 'yes' or self.Q == "dnk":
            try:
                self.questions_country.remove("Does the flag of your country contains red?")
            except ValueError:
                pass
        if self.Q == 'no':
            try:
                self.questions_country.remove("Is the population of your country over 10 million?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is the population of your country over 1 million?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Does the flag of your country contains blue?")
            except ValueError:
                pass

    if self.app.root.ids.third.test1 == "Does the flag of your country contains yellow?":
        if self.Q == "dnk":
            try:
                self.questions_country.remove("Does the flag of your country contains yellow?")
            except ValueError:
                pass
        if self.Q == 'no':
            try:
                self.questions_country.remove("Does the flag of your country contains green?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Does the flag of your country contains yellow?")
            except ValueError:
                pass
        if self.Q == 'yes':
            try:
                self.questions_country.remove("Does the flag of your country contains yellow?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is the population of your country over 10 million?")
            except ValueError:
                pass