"""
A function that handles the logic of the questions.
"""


def europe_check(self):
    """
    Manages the logic of the questions according to the answers given by the user
    for the countries situated in Europe.
    """
    if self.app.root.ids.third.questions == "Is Dutch an official language in your country?":
        if self.answer_user == 'no' or self.answer_user == "dnk":
            try:
                self.questions_country.remove("Is Dutch an official language in your country?")
            except ValueError:
                pass
        if self.answer_user == 'yes':
            try:
                self.questions_country.remove("Is the population of your country over 10 million?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is the population of your country over 30 million?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is the population of your country over 5 million?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is English an official language in your country?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is Italian an official language in your country?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is German an official language in your country?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is your country situated in the Nordic region?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Does your country touches The Mediterranean Sea?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Was your country part of Yougoslavia?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Does the flag of your country has 3 or more colors?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Does the flag of your country has a cross?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Does the flag of your country contains red?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is your country part of the European Union?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is Euro the official currency of your country?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Does the flag of your country has blue cross?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is Dutch an official language in your country?")
            except ValueError:
                pass

    if self.app.root.ids.third.questions == "Does the flag of your country has blue cross?":
        if self.answer_user == 'no' or self.answer_user == "dnk":
            try:
                self.questions_country.remove("Does the flag of your country has blue cross?")
            except ValueError:
                pass
        if self.answer_user == "yes":
            try:
                self.questions_country.remove("Is Italian an official language in your country?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is English an official language in your country?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is German an official language in your country?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is your country situated in the Nordic region?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Was your country part of Yougoslavia?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Does the flag of your country has blue cross?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is Dutch an official language in your country?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is French an official language in your country?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is the population of your country over 10 million?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is the population of your country over 30 million?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is the population of your country over 5 million?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Does your country touches The Mediterranean Sea?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is your country situated in the Nordic region?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Does the flag of your country has a cross?")
            except ValueError:
                pass

    if self.app.root.ids.third.questions == "Is English an official language in your country?":
        if self.answer_user == 'no' or self.answer_user == "dnk":
            try:
                self.questions_country.remove("Is English an official language in your country?")
            except ValueError:
                pass
        if self.answer_user == "yes":
            try:
                self.questions_country.remove("Is Italian an official language in your country?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is English an official language in your country?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is German an official language in your country?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is your country situated in the Nordic region?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Was your country part of Yougoslavia?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Does the flag of your country has blue cross?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is Dutch an official language in your country?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is French an official language in your country?")
            except ValueError:
                pass

    if self.app.root.ids.third.questions == "Is Italian an official language in your country?":
        if self.answer_user == 'no' or self.answer_user == "dnk":
            try:
                self.questions_country.remove("Is Italian an official language in your country?")
            except ValueError:
                pass
        if self.answer_user == "yes":
            try:
                self.questions_country.remove("Is English an official language in your country?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is Italian an official language in your country?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is your country situated in the Nordic region?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Was your country part of Yougoslavia?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Does the flag of your country has blue cross?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is Dutch an official language in your country?")
            except ValueError:
                pass

    if self.app.root.ids.third.questions == "Is French an official language in your country?":
        if self.answer_user == 'no' or self.answer_user == "dnk":
            try:
                self.questions_country.remove("Is French an official language in your country?")
            except ValueError:
                pass
        if self.answer_user == "yes":
            try:
                self.questions_country.remove("Is English an official language in your country?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is French an official language in your country?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is your country situated in the Nordic region?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Was your country part of Yougoslavia?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Does the flag of your country has blue cross?")
            except ValueError:
                pass

    if self.app.root.ids.third.questions == "Is German an official language in your country?":
        if self.answer_user == 'no' or self.answer_user == "dnk":
            try:
                self.questions_country.remove("Is German an official language in your country?")
            except ValueError:
                pass
        if self.answer_user == "yes":
            try:
                self.questions_country.remove("Is English an official language in your country?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is German an official language in your country?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is your country situated in the Nordic region?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Does your country touches The Mediterranean Sea?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Was your country part of Yougoslavia?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Does the flag of your country contains red?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Does the flag of your country has blue cross?")
            except ValueError:
                pass

    if self.app.root.ids.third.questions == "Is your country situated in the Nordic region?":
        if self.answer_user == 'no' or self.answer_user == "dnk":
            try:
                self.questions_country.remove("Is your country situated in the Nordic region?")
            except ValueError:
                pass
        if self.answer_user == "yes":
            try:
                self.questions_country.remove("Is the population of your country over 30 million?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is English an official language in your country?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is Italian an official language in your country?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is German an official language in your country?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is your country situated in the Nordic region?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Does your country touches The Mediterranean Sea?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Was your country part of Yougoslavia?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Does the flag of your country has a cross?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is French an official language in your country?")
            except ValueError:
                pass

    if self.app.root.ids.third.questions == "Does your country touches The Mediterranean Sea?":
        if self.answer_user == 'no' or self.answer_user == "dnk":
            try:
                self.questions_country.remove("Does your country touches The Mediterranean Sea?")
            except ValueError:
                pass
        if self.answer_user == "yes":
            try:
                self.questions_country.remove("Is German an official language in your country?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is your country situated in the Nordic region?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Does your country touches The Mediterranean Sea?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Does the flag of your country has blue cross?")
            except ValueError:
                pass

    if self.app.root.ids.third.questions == "Was your country part of Yougoslavia?":
        if self.answer_user == 'no' or self.answer_user == "dnk":
            try:
                self.questions_country.remove("Was your country part of Yougoslavia?")
            except ValueError:
                pass
        if self.answer_user == "yes":
            try:
                self.questions_country.remove("Is the population of your country over 10 million?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is the population of your country over 30 million?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is English an official language in your country?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is Italian an official language in your country?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is German an official language in your country?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is your country situated in the Nordic region?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Was your country part of Yougoslavia?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Does the flag of your country has a cross?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Does the flag of your country has blue cross?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is Dutch an official language in your country?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is French an official language in your country?")
            except ValueError:
                pass

    if self.app.root.ids.third.questions == "Does the flag of your country has 3 or more colors?":
        if self.answer_user == 'yes' or self.answer_user == "dnk":
            try:
                self.questions_country.remove("Does the flag of your country has 3 or more colors?")
            except ValueError:
                pass
        if self.answer_user == "no":
            try:
                self.questions_country.remove("Does the flag of your country has 3 or more colors?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is Dutch an official language in your country?")
            except ValueError:
                pass

    if self.app.root.ids.third.questions == "Does the flag of your country has a cross?":
        if self.answer_user == 'no' or self.answer_user == "dnk":
            try:
                self.questions_country.remove("Does the flag of your country has a cross?")
            except ValueError:
                pass
        if self.answer_user == "yes":
            try:
                self.questions_country.remove("Was your country part of Yougoslavia?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Does the flag of your country has a cross?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is Dutch an official language in your country?")
            except ValueError:
                pass

    if self.app.root.ids.third.questions == "Does the flag of your country contains red?":
        if self.answer_user == 'yes' or self.answer_user == "dnk":
            try:
                self.questions_country.remove("Does the flag of your country contains red?")
            except ValueError:
                pass
        if self.answer_user == "no":
            try:
                self.questions_country.remove("Is German an official language in your country?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Does the flag of your country contains red?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is Dutch an official language in your country?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is French an official language in your country?")
            except ValueError:
                pass

    if self.app.root.ids.third.questions == "Is the population of your country over 30 million?":
        if self.answer_user == 'no' or self.answer_user == "dnk":
            try:
                self.questions_country.remove("Is the population of your country over 30 million?")
            except ValueError:
                pass

        if self.answer_user == "yes":
            try:
                self.questions_country.remove("Is the population of your country over 10 million?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is the population of your country over 30 million?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is the population of your country over 5 million?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is Dutch an official language in your country?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Does the flag of your country has blue cross?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is your country situated in the Nordic region?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Was your country part of Yougoslavia?")
            except ValueError:
                pass

    if self.app.root.ids.third.questions == "Is the population of your country over 10 million?":
        if self.answer_user == "dnk":
            try:
                self.questions_country.remove("Is the population of your country over 10 million?")
            except ValueError:
                pass

        if self.answer_user == "yes":
            try:
                self.questions_country.remove("Is the population of your country over 5 million?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Was your country part of Yougoslavia?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Does the flag of your country has blue cross?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is the population of your country over 10 million?")
            except ValueError:
                pass
        if self.answer_user == "no":
            try:
                self.questions_country.remove("Is the population of your country over 30 million?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is the population of your country over 10 million?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is Dutch an official language in your country?")
            except ValueError:
                pass

    if self.app.root.ids.third.questions == "Is the population of your country over 5 million?":
        if self.answer_user == 'yes' or self.answer_user == "dnk":
            try:
                self.questions_country.remove("Is the population of your country over 5 million?")
            except ValueError:
                pass

        if self.answer_user == "no":
            try:
                self.questions_country.remove("Is the population of your country over 10 million?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is the population of your country over 30 million?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is the population of your country over 5 million?")
            except ValueError:
                pass
    if self.app.root.ids.third.questions == "Is your country part of the European Union?":
        try:
            self.questions_country.remove("Is your country part of the European Union?")
        except ValueError:
            pass

    if self.app.root.ids.third.questions == "Is Euro the official currency of your country?":
        try:
            self.questions_country.remove('Is Euro the official currency of your country?')
        except ValueError:
            pass
