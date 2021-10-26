"""
A function that handles the logic of the questions.
"""


def oceania_logic(self):
    """
    Manages the logic of the questions according to the answers given by the user
    for the countries situated in Oceania.
    """
    if self.app.root.ids.third.questions == "Is the population of your country over 10 million?":
        if self.answer_user == 'no' or self.answer_user == "dnk":
            self.questions_country.remove("Is the population of your country over 10 million?")
        if self.answer_user == 'yes':
            self.questions_country.remove("Is the population of your country over 10 million?")
            self.questions_country.remove("Is the population of your country over 1 million?")
            self.questions_country.remove("Does the flag of your country contains green?")
            self.questions_country.remove("Does the flag of your country contains blue?")
            self.questions_country.remove("Is there a star on the flag of your country?")
            self.questions_country.remove("Does the flag of your country contains red?")
            self.questions_country.remove("Does the flag of your country contains yellow?")
    if self.app.root.ids.third.questions == "Is the population of your country over 1 million?":
        if self.answer_user == 'no' or self.answer_user == "dnk":
            try:
                self.questions_country.remove("Is the population of your country over 1 million?")
            except ValueError:
                pass
        if self.answer_user == 'yes':
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

    if self.app.root.ids.third.questions == "Does the flag of your country contains green?":
        if self.answer_user == 'no' or self.answer_user == "dnk":
            try:
                self.questions_country.remove("Does the flag of your country contains green?")
            except ValueError:
                pass
        if self.answer_user == 'yes':
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
    if self.app.root.ids.third.questions == "Does the flag of your country contains blue?":
        if self.answer_user == 'yes' or self.answer_user == "dnk":
            try:
                self.questions_country.remove("Does the flag of your country contains blue?")
            except ValueError:
                pass
        if self.answer_user == 'no':
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
    if self.app.root.ids.third.questions == "Is there a star on the flag of your country?":
        if self.answer_user == 'yes' or self.answer_user == "dnk":
            try:
                self.questions_country.remove("Is there a star on the flag of your country?")
            except ValueError:
                pass
        if self.answer_user == 'no':
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
    if self.app.root.ids.third.questions == "Does the flag of your country contains red?":
        if self.answer_user == 'yes' or self.answer_user == "dnk":
            try:
                self.questions_country.remove("Does the flag of your country contains red?")
            except ValueError:
                pass
        if self.answer_user == 'no':
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

    if self.app.root.ids.third.questions == "Does the flag of your country contains yellow?":
        if self.answer_user == "dnk":
            try:
                self.questions_country.remove("Does the flag of your country contains yellow?")
            except ValueError:
                pass
        if self.answer_user == 'no':
            try:
                self.questions_country.remove("Does the flag of your country contains green?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Does the flag of your country contains yellow?")
            except ValueError:
                pass
        if self.answer_user == 'yes':
            try:
                self.questions_country.remove("Does the flag of your country contains yellow?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is the population of your country over 10 million?")
            except ValueError:
                pass
