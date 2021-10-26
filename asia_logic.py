"""
A function that handles the logic of the questions.
"""


def asia_logic(self):
    """
    Manages the logic of the questions according to the answers given by the user
    for the countries situated in Asia.
    """
    if self.app.root.ids.third.questions == "Is the population of your country over 100 million?":
        if self.answer_user == 'no' or self.answer_user == "dnk":
            self.questions_country.remove("Is the population of your country over 100 million?")
        if self.answer_user == 'yes':
            self.questions_country.remove("Is the population of your country over 100 million?")
            self.questions_country.remove("Is the population of your country over 30 million?")
            self.questions_country.remove("Is the population of your country over 10 million?")
            self.questions_country.remove("Is the population of your country over 5 million?")
            self.questions_country.remove("Is your country situated in Middle East region?")
            self.questions_country.remove("Is Arabic an official language in your country?")

    if self.app.root.ids.third.questions == "Is the population of your country over 30 million?":
        if self.answer_user == "dnk":
            try:
                self.questions_country.remove("Is the population of your country over 30 million?")
            except ValueError:
                pass
        if self.answer_user == 'no':
            try:
                self.questions_country.remove("Is the population of your country over 100 million?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is the population of your country over 30 million?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is Folk religion the most practiced religion in your country?")
            except ValueError:
                pass
        if self.answer_user == 'yes':
            try:
                self.questions_country.remove("Is the population of your country over 30 million?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is the population of your country over 10 million?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is the population of your country over 5 million?")
            except ValueError:
                pass

    if self.app.root.ids.third.questions == "Is the population of your country over 10 million?":
        if self.answer_user == "dnk":
            try:
                self.questions_country.remove("Is the population of your country over 10 million?")
            except ValueError:
                pass
        if self.answer_user == 'no':
            try:
                self.questions_country.remove("Is the population of your country over 100 million?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is the population of your country over 30 million?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is the population of your country over 10 million?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is Folk religion the most practiced religion in your country?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is Hinduism the most practiced religion in your country?")
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

    if self.app.root.ids.third.questions == "Is the population of your country over 5 million?":
        if self.answer_user == 'dnk':
            try:
                self.questions_country.remove("Is the population of your country over 5 million?")
            except ValueError:
                pass
        if self.answer_user == 'yes':
            try:
                self.questions_country.remove("Is the population of your country over 5 million?")
            except ValueError:
                pass
        if self.answer_user == 'no':
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
            try:
                self.questions_country.remove("Is the population of your country over 100 million?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is Hinduism the most practiced religion in your country?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is Folk religion the most practiced religion in your country?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is there a circled object or a sun on the flag of your country?")
            except ValueError:
                pass

    if self.app.root.ids.third.questions == "Is your country situated in Middle East region?":
        if self.answer_user == 'dnk' or self.answer_user == "no":
            try:
                self.questions_country.remove("Is your country situated in Middle East region?")
            except ValueError:
                pass

        if self.answer_user == "yes":
            try:
                self.questions_country.remove("Is your country situated in Middle East region?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is the population of your country over 100 million?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is Hinduism the most practiced religion in your country?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is Folk religion the most practiced religion in your country?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is Christianity the most practiced religion in your country?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is Buddhism the most practiced religion in your country?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Island ?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Does your country touches the Pacific Ocean?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Does the flag of your country contains yellow?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is there a moon on the flag your country?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is there a circled object or a sun on the flag of your country?")
            except ValueError:
                pass
    if self.app.root.ids.third.questions == "Is Arabic an official language in your country?":
        if self.answer_user == 'dnk' or self.answer_user == "no":
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
                self.questions_country.remove("Is the population of your country over 100 million?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is Hinduism the most practiced religion in your country?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is Folk religion the most practiced religion in your country?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is Christianity the most practiced religion in your country?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is Buddhism the most practiced religion in your country?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is Islam the most practiced religion in your religion?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is your country an island?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Does your country touches the Pacific Ocean?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Does the flag of your country contains blue?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Does the flag of your country contains yellow?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is there a moon on the flag your country?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is there a circled object or a sun on the flag of your country?")
            except ValueError:
                pass

    if self.app.root.ids.third.questions == "Is Hinduism the most practiced religion in your country?":
        if self.answer_user == 'dnk' or self.answer_user == "no":
            try:
                self.questions_country.remove("Is Hinduism the most practiced religion in your country?")
            except ValueError:
                pass
        if self.answer_user == "yes":
            try:
                self.questions_country.remove("Is Hinduism the most practiced religion in your country?")
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
                self.questions_country.remove("Is your country situated in Middle East region?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is Arabic an official language in your country?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is Hinduism the most practiced religion in your country?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is Folk religion the most practiced religion in your country?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is Christianity the most practiced religion in your country?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is Buddhism the most practiced religion in your country?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is Islam the most practiced religion in your religion?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is your country an island?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Does your country touches the Pacific Ocean?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Does the flag of your country contains blue?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Does the flag of your country contains yellow?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is there a moon on the flag your country?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is there a star on the flag of your country?")
            except ValueError:
                pass
    if self.app.root.ids.third.questions == "Is Folk religion the most practiced religion in your country?":
        if self.answer_user == 'dnk' or self.answer_user == "no":
            try:
                self.questions_country.remove("Is Folk religion the most practiced religion in your country?")
            except ValueError:
                pass
        if self.answer_user == "yes":
            try:
                self.questions_country.remove("Is Folk religion the most practiced religion in your country?")
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
                self.questions_country.remove("Is the population of your country over 30 million?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is your country situated in Middle East region?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is Arabic an official language in your country?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is Hinduism the most practiced religion in your country?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is Christianity the most practiced religion in your country?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is Buddhism the most practiced religion in your country?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is Islam the most practiced religion in your religion?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is your country an island?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Does your country touches the Indian Ocean?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Does your country touches the Pacific Ocean?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Does the flag of your country contains blue?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Does the flag of your country contains yellow?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Does the flag of your country contains red?")
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
                self.questions_country.remove("Is there a moon on the flag your country?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is there a circled object or a sun on the flag of your country?")
            except ValueError:
                pass
    if self.app.root.ids.third.questions == "Is Christianity the most practiced religion in your country?":
        if self.answer_user == 'dnk' or self.answer_user == "no":
            try:
                self.questions_country.remove("Is Christianity the most practiced religion in your country?")
            except ValueError:
                pass
        if self.answer_user == "yes":
            try:
                self.questions_country.remove("Is Christianity the most practiced religion in your country?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is your country situated in Middle East region?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is Arabic an official language in your country?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is Buddhism the most practiced religion in your country?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is Islam the most practiced religion in your religion?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is Hinduism the most practiced religion in your country?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is Folk religion the most practiced religion in your country?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Does the flag of your country contains red?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Does the flag of your country contains green?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is there a moon on the flag your country?")
            except ValueError:
                pass
    if self.app.root.ids.third.questions == "Is Buddhism the most practiced religion in your country?":
        if self.answer_user == 'dnk' or self.answer_user == "no":
            try:
                self.questions_country.remove("Is Buddhism the most practiced religion in your country?")
            except ValueError:
                pass
        if self.answer_user == "yes":
            try:
                self.questions_country.remove("Is Buddhism the most practiced religion in your country?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is Christianity the most practiced religion in your country?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is your country situated in Middle East region?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is Arabic an official language in your country?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is Islam the most practiced religion in your religion?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is Hinduism the most practiced religion in your country?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is Folk religion the most practiced religion in your country?")
            except ValueError:
                pass
    if self.app.root.ids.third.questions == "Is Islam the most practiced religion in your religion?":
        if self.answer_user == "dnk":
            try:
                self.questions_country.remove("Is Islam the most practiced religion in your religion?")
            except ValueError:
                pass
        if self.answer_user == "no":
            try:
                self.questions_country.remove("Is Islam the most practiced religion in your religion?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is Arabic an official language in your country?")
            except ValueError:
                pass
        if self.answer_user == "yes":
            try:
                self.questions_country.remove("Is Islam the most practiced religion in your religion?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is Buddhism the most practiced religion in your country?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is Christianity the most practiced religion in your country?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is Hinduism the most practiced religion in your country?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is Folk religion the most practiced religion in your country?")
            except ValueError:
                pass

    if self.app.root.ids.third.questions == "Is your country an island?":
        if self.answer_user == 'dnk' or self.answer_user == "no":
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
                self.questions_country.remove("Is your country situated in Middle East region?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is Arabic an official language in your country?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is Hinduism the most practiced religion in your country?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is Folk religion the most practiced religion in your country?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Does the flag of your country contains red?")
            except ValueError:
                pass

    if self.app.root.ids.third.questions == "Does your country touches the Indian Ocean?":
        if self.answer_user == 'dnk' or self.answer_user == "no":
            try:
                self.questions_country.remove("Does your country touches the Indian Ocean?")
            except ValueError:
                pass
        if self.answer_user == "yes":
            try:
                self.questions_country.remove("Does your country touches the Indian Ocean?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is Folk religion the most practiced religion in your country?")
            except ValueError:
                pass

    if self.app.root.ids.third.questions == "Does your country touches the Pacific Ocean?":
        if self.answer_user == 'dnk' or self.answer_user == "no":
            try:
                self.questions_country.remove("Does your country touches the Pacific Ocean?")
            except ValueError:
                pass
        if self.answer_user == "yes":
            try:
                self.questions_country.remove("Does your country touches the Pacific Ocean?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is your country situated in Middle East region?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is Arabic an official language in your country?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is Hinduism the most practiced religion in your country?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Does the flag of your country contains red?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Does the flag of your country contains green?")
            except ValueError:
                pass

    if self.app.root.ids.third.questions == "Does the flag of your country contains red?":
        if self.answer_user == 'dnk' or self.answer_user == "yes":
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
                self.questions_country.remove("Is Folk religion the most practiced religion in your country?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is Christianity the most practiced religion in your country?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is your country an island?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Does your country touches the Pacific Ocean?")
            except ValueError:
                pass

    if self.app.root.ids.third.questions == "Does the flag of your country contains blue?":
        if self.answer_user == 'dnk' or self.answer_user == "no":
            try:
                self.questions_country.remove("Does the flag of your country contains blue?")
            except ValueError:
                pass
        if self.answer_user == "yes":
            try:
                self.questions_country.remove("Does the flag of your country contains blue?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is Arabic an official language in your country?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is Folk religion the most practiced religion in your country?")
            except ValueError:
                pass

    if self.app.root.ids.third.questions == "Does the flag of your country contains green?":
        if self.answer_user == 'dnk' or self.answer_user == "no":
            try:
                self.questions_country.remove("Does the flag of your country contains green?")
            except ValueError:
                pass
        if self.answer_user == "yes":
            try:
                self.questions_country.remove("Does the flag of your country contains green?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is Folk religion the most practiced religion in your country?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is Christianity the most practiced religion in your country?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Does your country touches the Pacific Ocean?")
            except ValueError:
                pass

    if self.app.root.ids.third.questions == "Does the flag of your country contains yellow?":
        if self.answer_user == 'dnk' or self.answer_user == "no":
            try:
                self.questions_country.remove("Does the flag of your country contains yellow?")
            except ValueError:
                pass
        if self.answer_user == "yes":
            try:
                self.questions_country.remove("Does the flag of your country contains yellow?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is your country situated in Middle East region?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is Arabic an official language in your country?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is Hinduism the most practiced religion in your country?")
            except ValueError:
                pass

    if self.app.root.ids.third.questions == "Is there a star on the flag of your country?":
        if self.answer_user == 'dnk':
            try:
                self.questions_country.remove("Is there a star on the flag of your country?")
            except ValueError:
                pass
        if self.answer_user == "no":
            try:
                self.questions_country.remove("Is there a star on the flag of your country?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is Folk religion the most practiced religion in your country?")
            except ValueError:
                pass

        if self.answer_user == "yes":
            try:
                self.questions_country.remove("Is there a star on the flag of your country?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is Hinduism the most practiced religion in your country?")
            except ValueError:
                pass

    if self.app.root.ids.third.questions == "Is there a moon on the flag your country?":
        if self.answer_user == 'dnk' or self.answer_user == "no":
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
                self.questions_country.remove("Is Hinduism the most practiced religion in your country?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is your country situated in Middle East region?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is Arabic an official language in your country?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is Folk religion the most practiced religion in your country?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is Christianity the most practiced religion in your country?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is there a circled object or a sun on the flag of your country?")
            except ValueError:
                pass

    if self.app.root.ids.third.questions == "Is there a circled object or a sun on the flag of your country?":
        if self.answer_user == 'dnk' or self.answer_user == "no":
            try:
                self.questions_country.remove("Is there a circled object or a sun on the flag of your country?")
            except ValueError:
                pass

        if self.answer_user == "yes":
            try:
                self.questions_country.remove("Is there a circled object or a sun on the flag of your country?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is the population of your country over 5 million?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is your country situated in Middle East region?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is Arabic an official language in your country?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is Folk religion the most practiced religion in your country?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is there a moon on the flag your country?")
            except ValueError:
                pass
