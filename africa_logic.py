"""
A function that handles the logic of the questions.
"""

def africa_logic(self):
    """
    Manages the logic of the questions according to the answers given by the user
    for the countries situated in Africa.
    """
    if self.app.root.ids.third.questions == "Is the population of your country over 30 million?":
        if self.answer_user == 'no' or self.answer_user == "dnk":
            self.questions_country.remove("Is the population of your country over 30 million?")
        if self.answer_user == "yes":
            self.questions_country.remove("Is the population of your country over 30 million?")
            self.questions_country.remove("Is the population of your country over 10 million?")
            self.questions_country.remove("Is the population of your country over 5 million?")
            self.questions_country.remove("Is your country an island?")

    if self.app.root.ids.third.questions == "Is the population of your country over 10 million?":
        if self.answer_user == "dnk":
            try:
                self.questions_country.remove("Is the population of your country over 10 million?")
            except ValueError:
                pass
        if self.answer_user == 'yes':
            try:
                self.questions_country.remove("Is the population of your country over 10 million?")
            except ValueError:
                pass
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

    if self.app.root.ids.third.questions == "Is the population of your country over 5 million?":
        if self.answer_user == "dnk":
            try:
                self.questions_country.remove("Is the population of your country over 5 million?")
            except ValueError:
                pass
        if self.answer_user == 'yes':
            try:
                self.questions_country.remove("Is the population of your country over 5 million?")
            except ValueError:
                pass
        if self.answer_user == "no":
            try:
                self.questions_country.remove("Is the population of your country over 5 million?")
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
    if self.app.root.ids.third.questions == "Is your country an island?":
        if self.answer_user == 'no' or self.answer_user == "dnk":
            try:
                self.questions_country.remove("Is your country an island?")
            except ValueError:
                pass
        if self.answer_user == "yes":
            try:
                self.questions_country.remove("Is your country an island?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is the population of your country over 30 million?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Does the flag of your country contains at least 3 or more colors?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Does the flag of your country contains red?")
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
                self.questions_country.remove("Is French an official language in your country?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Does the flag of your country contains at least 3 or more colors?")
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
                self.questions_country.remove("Is English an official language in your country?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is Portuguese an official language in your country?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is there a moon on the flag your country?")
            except ValueError:
                pass
    if self.app.root.ids.third.questions == "Is Arabic an official language in your country?":
        if self.answer_user == 'no' or self.answer_user == "dnk":
            try:
                self.questions_country.remove("Is Arabic an official language in your country?")
            except ValueError:
                pass
        if self.answer_user == "yes":
            try:
                self.questions_country.remove("Is Arabic an official language in your country?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is Portuguese an official language in your country?")
            except ValueError:
                pass
    if self.app.root.ids.third.questions == "Is Portuguese an official language in your country?":
        if self.answer_user == 'no' or self.answer_user == "dnk":
            try:
                self.questions_country.remove("Is Portuguese an official language in your country?")
            except ValueError:
                pass
        if self.answer_user == "yes":
            try:
                self.questions_country.remove("Is Portuguese an official language in your country?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is English an official language in your country?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is Arabic an official language in your country?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Does the flag of your country contains at least 3 or more colors?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Does the flag of your country contains red?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is there a moon on the flag your country?")
            except ValueError:
                pass

    if self.app.root.ids.third.questions == "Does the flag of your country contains at least 3 or more colors?":
        if self.answer_user == 'yes' or self.answer_user == "dnk":
            try:
                self.questions_country.remove("Is Portuguese an official language in your country?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Does the flag of your country contains at least 3 or more colors?")
            except ValueError:
                pass
        if self.answer_user == "no":
            try:
                self.questions_country.remove("Does the flag of your country contains at least 3 or more colors?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is Portuguese an official language in your country?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is the population of your country over 5 million?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is the population of your country over 10 million?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is your country an island?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is French an official language in your country?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Does the flag of your country contains yellow?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is Islam the most practiced religion in your religion?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is Christianity the most practiced religion in your country?")
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
                self.questions_country.remove("Does the flag of your country contains red?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is your country an island?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is Portuguese an official language in your country?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is there a moon on the flag your country?")
            except ValueError:
                pass

    if self.app.root.ids.third.questions == "Does the flag of your country contains blue?":
        try:
            self.questions_country.remove("Does the flag of your country contains blue?")
        except ValueError:
            pass
    if self.app.root.ids.third.questions == "Does the flag of your country contains green?":
        try:
            self.questions_country.remove("Does the flag of your country contains green?")
        except ValueError:
            pass
    if self.app.root.ids.third.questions == "Does the flag of your country contains yellow?":
        try:
            self.questions_country.remove("Does the flag of your country contains yellow?")
        except ValueError:
            pass
    if self.app.root.ids.third.questions == "Is Islam the most practiced religion in your religion?":
        if self.answer_user == "no" or self.answer_user == "yes":
            try:
                self.questions_country.remove("Is Islam the most practiced religion in your religion?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is Christianity the most practiced religion in your country?")
            except ValueError:
                pass
        if self.answer_user == "dnk":
            try:
                self.questions_country.remove("Is Islam the most practiced religion in your religion?")
            except ValueError:
                pass
    if self.app.root.ids.third.questions == "Is Christianity the most practiced religion in your country?":
        if self.answer_user == "no" or self.answer_user == "yes":
            try:
                self.questions_country.remove("Is Islam the most practiced religion in your religion?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is Christianity the most practiced religion in your country?")
            except ValueError:
                pass
        if self.answer_user == "dnk":
            try:
                self.questions_country.remove("Is Christianity the most practiced religion in your country?")
            except ValueError:
                pass
    if self.app.root.ids.third.questions == "Does your country touches the Atlantic Ocean?" \
                                            "(including The Mediterranean Sea)":
        try:
            self.questions_country.remove(
                "Does your country touches the Atlantic Ocean?(including The Mediterranean Sea)")
        except ValueError:
            pass
    if self.app.root.ids.third.questions == "Does your country touches the Indian Ocean?" \
                                            "(including The Red Sea and The Arabian Sea)":
        try:
            self.questions_country.remove(
                "Does your country touches the Indian Ocean?(including The Red Sea and The Arabian Sea)")
        except ValueError:
            pass
    if self.app.root.ids.third.questions == "Is there a star on the flag of your country?":
        try:
            self.questions_country.remove("Is there a star on the flag of your country?")
        except ValueError:
            pass
    if self.app.root.ids.third.questions == "Is there a moon on the flag your country?":
        if self.answer_user == "dnk" or self.answer_user == "no":
            try:
                self.questions_country.remove("Is there a moon on the flag your country?")
            except ValueError:
                pass
        if self.answer_user == "yes":
            try:
                self.questions_country.remove("Is there a moon on the flag your country?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is English an official language in your country?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is Arabic an official language in your country?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is Portuguese an official language in your country?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Does the flag of your country contains red?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is Islam the most practiced religion in your religion?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is Christianity the most practiced religion in your country?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is there a star on the flag of your country?")
            except ValueError:
                pass
