def africa_logic(self):
    if self.app.root.ids.third.test1 == "Is the population of your country over 30 million?":
        if self.Q == 'no' or self.Q == "dnk":
            self.questions_country.remove("Is the population of your country over 30 million?")
        if self.Q == "yes":
            self.questions_country.remove("Is the population of your country over 30 million?")
            self.questions_country.remove("Is the population of your country over 10 million?")
            self.questions_country.remove("Is the population of your country over 5 million?")
            self.questions_country.remove("Is your country an island?")

    if self.app.root.ids.third.test1 == "Is the population of your country over 10 million?":
        if self.Q == "dnk":
            try:
                self.questions_country.remove("Is the population of your country over 10 million?")
            except ValueError:
                pass
        if self.Q == 'yes':
            try:
                self.questions_country.remove("Is the population of your country over 10 million?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is the population of your country over 5 million?")
            except ValueError:
                pass
        if self.Q == "no":
            try:
                self.questions_country.remove("Is the population of your country over 10 million?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is the population of your country over 30 million?")
            except ValueError:
                pass

    if self.app.root.ids.third.test1 == "Is the population of your country over 5 million?":
        if self.Q == "dnk":
            try:
                self.questions_country.remove("Is the population of your country over 5 million?")
            except ValueError:
                pass
        if self.Q == 'yes':
            try:
                self.questions_country.remove("Is the population of your country over 5 million?")
            except ValueError:
                pass
        if self.Q == "no":
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
    if self.app.root.ids.third.test1 == "Is your country an island?":
        if self.Q == 'no' or self.Q == "dnk":
            try:
                self.questions_country.remove("Is your country an island?")
            except ValueError:
                pass
        if self.Q == "yes":
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
    if self.app.root.ids.third.test1 == "Is French an official language in your country?":
        if self.Q == 'no' or self.Q == "dnk":
            try:
                self.questions_country.remove("Is French an official language in your country?")
            except ValueError:
                pass
        if self.Q == "yes":
            try:
                self.questions_country.remove("Is French an official language in your country?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Does the flag of your country contains at least 3 or more colors?")
            except ValueError:
                pass
    if self.app.root.ids.third.test1 == "Is English an official language in your country?":
        if self.Q == 'no' or self.Q == "dnk":
            try:
                self.questions_country.remove("Is English an official language in your country?")
            except ValueError:
                pass
        if self.Q == "yes":
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
    if self.app.root.ids.third.test1 == "Is Arabic an official language in your country?":
        if self.Q == 'no' or self.Q == "dnk":
            try:
                self.questions_country.remove("Is Arabic an official language in your country?")
            except ValueError:
                pass
        if self.Q == "yes":
            try:
                self.questions_country.remove("Is Arabic an official language in your country?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is Portuguese an official language in your country?")
            except ValueError:
                pass
    if self.app.root.ids.third.test1 == "Is Portuguese an official language in your country?":
        if self.Q == 'no' or self.Q == "dnk":
            try:
                self.questions_country.remove("Is Portuguese an official language in your country?")
            except ValueError:
                pass
        if self.Q == "yes":
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

    if self.app.root.ids.third.test1 == "Does the flag of your country contains at least 3 or more colors?":
        if self.Q == 'yes' or self.Q == "dnk":
            try:
                self.questions_country.remove("Is Portuguese an official language in your country?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Does the flag of your country contains at least 3 or more colors?")
            except ValueError:
                pass
        if self.Q == "no":
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
    if self.app.root.ids.third.test1 == "Does the flag of your country contains red?":
        if self.Q == 'yes' or self.Q == "dnk":
            try:
                self.questions_country.remove("Does the flag of your country contains red?")
            except ValueError:
                pass
        if self.Q == "no":
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

    if self.app.root.ids.third.test1 == "Does the flag of your country contains blue?":
        if self.Q == 'no' or self.Q == "dnk" or self.Q == "yes":
            try:
                self.questions_country.remove("Does the flag of your country contains blue?")
            except ValueError:
                pass
    if self.app.root.ids.third.test1 == "Does the flag of your country contains green?":
        if self.Q == "dnk" or self.Q == "yes" or self.Q == "no":
            try:
                self.questions_country.remove("Does the flag of your country contains green?")
            except ValueError:
                pass
    if self.app.root.ids.third.test1 == "Does the flag of your country contains yellow?":
        if self.Q == "dnk" or self.Q == "no" or self.Q == "yes":
            try:
                self.questions_country.remove("Does the flag of your country contains yellow?")
            except ValueError:
                pass
    if self.app.root.ids.third.test1 == "Is Islam the most practiced religion in your religion?":
        if self.Q == "no" or self.Q == "yes":
            try:
                self.questions_country.remove("Is Islam the most practiced religion in your religion?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is Christianity the most practiced religion in your country?")
            except ValueError:
                pass
        if self.Q == "dnk":
            try:
                self.questions_country.remove("Is Islam the most practiced religion in your religion?")
            except ValueError:
                pass
    if self.app.root.ids.third.test1 == "Is Christianity the most practiced religion in your country?":
        if self.Q == "no" or self.Q == "yes":
            try:
                self.questions_country.remove("Is Islam the most practiced religion in your religion?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is Christianity the most practiced religion in your country?")
            except ValueError:
                pass
        if self.Q == "dnk":
            try:
                self.questions_country.remove("Is Christianity the most practiced religion in your country?")
            except ValueError:
                pass
    if self.app.root.ids.third.test1 == "Does your country touches the Atlantic Ocean?(including The Mediterranean Sea)":
        if self.Q == "dnk" or self.Q == "no" or self.Q == "yes":
            try:
                self.questions_country.remove("Does your country touches the Atlantic Ocean?(including The Mediterranean Sea)")
            except ValueError:
                pass
    if self.app.root.ids.third.test1 == "Does your country touches the Indian Ocean?(including The Red Sea and The Arabian Sea)":
        if self.Q == "dnk" or self.Q == "no" or self.Q == "yes":
            try:
                self.questions_country.remove("Does your country touches the Indian Ocean?(including The Red Sea and The Arabian Sea)")
            except ValueError:
                pass
    if self.app.root.ids.third.test1 == "Is there a star on the flag of your country?":
        if self.Q == "dnk" or self.Q == "no" or self.Q == "yes":
            try:
                self.questions_country.remove("Is there a star on the flag of your country?")
            except ValueError:
                pass
    if self.app.root.ids.third.test1 == "Is there a moon on the flag your country?":
        if self.Q == "dnk" or self.Q == "no":
            try:
                self.questions_country.remove("Is there a moon on the flag your country?")
            except ValueError:
                pass
        if self.Q == "yes":
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