def south_america_logic(self):
    if self.app.root.ids.third.test1 == "Is Spanish an official language in your country?":
        if self.Q == "dnk" or self.Q == "yes":
            self.questions_country.remove("Is Spanish an official language in your country?")
        if self.Q == "no":
            self.questions_country.remove("Is Spanish an official language in your country?")
            self.questions_country.remove("Is the Amazon forest in your country?")
            self.questions_country.remove("Does your country touches the Atlantic Ocean?")
            self.questions_country.remove("Does your country touches the Pacific Ocean?")
            self.questions_country.remove("Does the flag of your country contains blue?")
            self.questions_country.remove("Does the flag of your country contains green?")

    if self.app.root.ids.third.test1 == "Is the Amazon forest in your country?":
        if self.Q == "yes" or self.Q == "dnk":
            try:
                self.questions_country.remove("Is the Amazon forest in your country?")
            except ValueError:
                pass
        if self.Q == "no":
            try:
                self.questions_country.remove("Is the Amazon forest in your country?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is Spanish an official language in your country?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Does the flag of your country contains blue?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Does the flag of your country contains green?")
            except ValueError:
                pass
    if self.app.root.ids.third.test1 == "Is the population of your country over 30 million?":
        if self.Q == "no" or self.Q == "dnk":
            try:
                self.questions_country.remove("Is the population of your country over 30 million?")
            except ValueError:
                pass
        if self.Q == "yes":
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
            try:
                self.questions_country.remove("Is there a star on the flag of your country?")
            except ValueError:
                pass
    if self.app.root.ids.third.test1 == "Is the population of your country over 10 million?":
        if self.Q == "no":
            try:
                self.questions_country.remove("Is the population of your country over 10 million?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is the population of your country over 30 million?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Does your country touches the Pacific Ocean?")
            except ValueError:
                pass
        if self.Q == "yes":
            try:
                self.questions_country.remove("Is the population of your country over 10 million?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is the population of your country over 5 million?")
            except ValueError:
                pass
        if self.Q == "dnk":
            try:
                self.questions_country.remove("Is the population of your country over 10 million?")
            except ValueError:
                pass
    if self.app.root.ids.third.test1 == "Is the population of your country over 5 million?":
        if self.Q == "yes" or self.Q == "dnk":
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
            try:
                self.questions_country.remove("Does your country touches the Atlantic Ocean?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Does your country touches the Pacific Ocean?")
            except ValueError:
                pass

    if self.app.root.ids.third.test1 == "Does your country touches the Atlantic Ocean?":
        if self.Q == "yes" or self.Q == "dnk":
            try:
                self.questions_country.remove("Does your country touches the Atlantic Ocean?")
            except ValueError:
                pass
        if self.Q == "no":
            try:
                self.questions_country.remove("Does your country touches the Atlantic Ocean?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is Spanish an official language in your country?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is the population of your country over 5 million?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Does the flag of your country contains red?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is there a star on the flag of your country?")
            except ValueError:
                pass
    if self.app.root.ids.third.test1 == "Does your country touches the Pacific Ocean?":
        if self.Q == "no" or self.Q == "dnk":
            try:
                self.questions_country.remove("Does your country touches the Pacific Ocean?")
            except ValueError:
                pass
        if self.Q == "yes":
            try:
                self.questions_country.remove("Does your country touches the Pacific Ocean?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is Spanish an official language in your country?")
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
            try:
                self.questions_country.remove("Does the flag of your country contains red?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Does the flag of your country contains green?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is there a circled object or a sun on the flag of your country?")
            except ValueError:
                pass

    if self.app.root.ids.third.test1 == "Does the flag of your country contains red?":
        if self.Q == "yes" or self.Q == "dnk":
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
                self.questions_country.remove("Is there a star on the flag of your country?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is there a circled object or a sun on the flag of your country?")
            except ValueError:
                pass

    if self.app.root.ids.third.test1 == "Does the flag of your country contains blue?":
        if self.Q == "yes" or self.Q == "dnk":
            try:
                self.questions_country.remove("Does the flag of your country contains blue?")
            except ValueError:
                pass
        if self.Q == "no":
            try:
                self.questions_country.remove("Does the flag of your country contains blue?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is the Amazon forest in your country?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Does the flag of your country contains red?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is there a circled object or a sun on the flag of your country?")
            except ValueError:
                pass
    if self.app.root.ids.third.test1 == "Does the flag of your country contains green?":
        if self.Q == "no" or self.Q == "dnk":
            try:
                self.questions_country.remove("Does the flag of your country contains green?")
            except ValueError:
                pass
        if self.Q == "yes":
            try:
                self.questions_country.remove("Does the flag of your country contains green?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is the Amazon forest in your country?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Does your country touches the Pacific Ocean?")
            except ValueError:
                pass
    if self.app.root.ids.third.test1 == "Is there a star on the flag of your country?":
        if self.Q == "no" or self.Q == "dnk":
            try:
                self.questions_country.remove("Is there a star on the flag of your country?")
            except ValueError:
                pass
        if self.Q == "yes":
            try:
                self.questions_country.remove("Is there a star on the flag of your country?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is the population of your country over 30 million?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Does your country touches the Atlantic Ocean?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Does the flag of your country contains red?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Is there a circled object or a sun on the flag of your country?")
            except ValueError:
                pass
    if self.app.root.ids.third.test1 == "Is there a circled object or a sun on the flag of your country?":
        if self.Q == "no" or self.Q == "dnk":
            try:
                self.questions_country.remove("Is there a circled object or a sun on the flag of your country?")
            except ValueError:
                pass
        if self.Q == "yes":
            try:
                self.questions_country.remove("Is there a circled object or a sun on the flag of your country?")
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
                self.questions_country.remove("Is there a star on the flag of your country?")
            except ValueError:
                pass