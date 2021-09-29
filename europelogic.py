

def europe_check(self):
    if self.app.root.ids.third.test1 == "Speaks Dutch":
        if self.Q == 'no' or self.Q == "dnk":
            self.questions_country.remove("Speaks Dutch")
        if self.Q == 'yes':
            try:
                print("worked")
                self.questions_country.remove("Pop over 10m ?")
                self.questions_country.remove("Pop over 30m ?")
                self.questions_country.remove("Population over 5m")
                self.questions_country.remove("Speaks English")
                self.questions_country.remove("Speaks Italien")
                self.questions_country.remove("Speaks German ?")
                self.questions_country.remove("Situated in the Nordic region?")
                self.questions_country.remove("Touches sea mediterean ?")
                self.questions_country.remove("Part of Yougoslavia ?")
                self.questions_country.remove("Flag has 3 or more colors ?")
                self.questions_country.remove("Flag with a cross?")
                self.questions_country.remove("Flag contains red?")
                self.questions_country.remove("In Europe Union ?")
                self.questions_country.remove("euro in your country?")
                self.questions_country.remove("Flag with Blue cross?")
                self.questions_country.remove("Speaks Dutch")
            except ValueError:
                pass

    if self.app.root.ids.third.test1 == "Flag with Blue cross?":
        if self.Q == 'no' or self.Q == "dnk":
            try:
                self.questions_country.remove("Flag with Blue cross?")
            except ValueError:
                pass
        if self.Q == "yes":
            try:
                self.questions_country.remove("Speaks Italien")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Speaks English")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Speaks German ?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Situated in the Nordic region?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Part of Yougoslavia ?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Flag with Blue cross?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Speaks Dutch")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Speaks French ?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Pop over 10m ?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Pop over 30m ?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Population over 5m")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Touches sea mediterean ?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Situated in the Nordic region?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Flag with a cross?")
            except ValueError:
                pass

    if self.app.root.ids.third.test1 == "Speaks English":
        if self.Q == 'no' or self.Q == "dnk":
            try:
                self.questions_country.remove("Speaks English")
            except ValueError:
                pass
        if self.Q == "yes":
            try:
                self.questions_country.remove("Speaks Italien")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Speaks English")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Speaks German ?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Situated in the Nordic region?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Part of Yougoslavia ?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Flag with Blue cross?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Speaks Dutch")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Speaks French ?")
            except ValueError:
                pass

    if self.app.root.ids.third.test1 == "Speaks Italien":
        if self.Q == 'no' or self.Q == "dnk":
            try:
                self.questions_country.remove("Speaks Italien")
            except ValueError:
                pass
        if self.Q == "yes":
            try:
                self.questions_country.remove("Speaks English")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Speaks Italien")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Situated in the Nordic region?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Part of Yougoslavia ?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Flag with Blue cross?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Speaks Dutch")
            except ValueError:
                pass

    if self.app.root.ids.third.test1 == "Speaks French ?":
        if self.Q == 'no' or self.Q == "dnk":
            try:
                self.questions_country.remove("Speaks French ?")
            except ValueError:
                pass
        if self.Q == "yes":
            try:
                self.questions_country.remove("Speaks English")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Speaks French ?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Situated in the Nordic region?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Part of Yougoslavia ?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Flag with Blue cross?")
            except ValueError:
                pass

    if self.app.root.ids.third.test1 == "Speaks German ?":
        if self.Q == 'no' or self.Q == "dnk":
            try:
                self.questions_country.remove("Speaks German ?")
            except ValueError:
                pass
        if self.Q == "yes":
            try:
                self.questions_country.remove("Speaks English")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Speaks German ?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Situated in the Nordic region?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Touches sea mediterean ?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Part of Yougoslavia ?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Flag contains red?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Flag with Blue cross?")
            except ValueError:
                pass

    if self.app.root.ids.third.test1 == "Situated in the Nordic region?":
        if self.Q == 'no' or self.Q == "dnk":
            try:
                self.questions_country.remove("Situated in the Nordic region?")
            except ValueError:
                pass
        if self.Q == "yes":
            try:
                self.questions_country.remove("Pop over 30m ?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Speaks English")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Speaks Italien")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Speaks German ?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Situated in the Nordic region?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Touches sea mediterean ?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Part of Yougoslavia ?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Flag with a cross?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Speaks French ?")
            except ValueError:
                pass

    if self.app.root.ids.third.test1 == "Touches sea mediterean ?":
        if self.Q == 'no' or self.Q == "dnk":
            try:
                self.questions_country.remove("Touches sea mediterean ?")
            except ValueError:
                pass
        if self.Q == "yes":
            try:
                self.questions_country.remove("Speaks German ?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Situated in the Nordic region?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Touches sea mediterean ?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Flag with Blue cross?")
            except ValueError:
                pass

    if self.app.root.ids.third.test1 == "Part of Yougoslavia ?":
        if self.Q == 'no' or self.Q == "dnk":
            try:
                self.questions_country.remove("Part of Yougoslavia ?")
            except ValueError:
                pass
        if self.Q == "yes":
            try:
                self.questions_country.remove("Pop over 10m ?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Pop over 30m ?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Speaks English")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Speaks Italien")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Speaks German ?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Situated in the Nordic region?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Part of Yougoslavia ?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Flag with a cross?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Flag with Blue cross?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Speaks Dutch")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Speaks French ?")
            except ValueError:
                pass

    if self.app.root.ids.third.test1 == "Flag has 3 or more colors ?":
        if self.Q == 'yes' or self.Q == "dnk":
            try:
                self.questions_country.remove("Flag has 3 or more colors ?")
            except ValueError:
                pass
        if self.Q == "no":
            try:
                self.questions_country.remove("Flag has 3 or more colors ?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Speaks Dutch")
            except ValueError:
                pass

    if self.app.root.ids.third.test1 == "Flag with a cross?":
        if self.Q == 'no' or self.Q == "dnk":
            try:
                self.questions_country.remove("Flag with a cross?")
            except ValueError:
                pass
        if self.Q == "yes":
            try:
                self.questions_country.remove("Part of Yougoslavia ?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Flag with a cross?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Speaks Dutch")
            except ValueError:
                pass

    if self.app.root.ids.third.test1 == "Flag contains red?":
        if self.Q == 'yes' or self.Q == "dnk":
            try:
                self.questions_country.remove("Flag contains red?")
            except ValueError:
                pass
        if self.Q == "no":
            try:
                self.questions_country.remove("Speaks German ?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Flag contains red?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Speaks Dutch")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Speaks French ?")
            except ValueError:
                pass

    if self.app.root.ids.third.test1 == "Pop over 30m ?":
        if self.Q == 'no' or self.Q == "dnk":
            try:
                self.questions_country.remove("Pop over 30m ?")
            except ValueError:
                pass

        if self.Q == "yes":
            try:
                self.questions_country.remove("Pop over 10m ?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Pop over 30m ?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Population over 5m")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Speaks Dutch")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Flag with Blue cross?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Situated in the Nordic region?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Part of Yougoslavia ?")
            except ValueError:
                pass

    if self.app.root.ids.third.test1 == "Pop over 10m ?":
        if self.Q == "dnk":
            try:
                self.questions_country.remove("Pop over 10m ?")
            except ValueError:
                pass

        if self.Q == "yes":
            try:
                self.questions_country.remove("Population over 5m")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Part of Yougoslavia ?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Flag with Blue cross?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Pop over 10m ?")
            except ValueError:
                pass
        if self.Q == "no":
            try:
                self.questions_country.remove("Pop over 30m ?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Pop over 10m ?")
            except ValueError:
                pass

    if self.app.root.ids.third.test1 == "Population over 5m":
        if self.Q == 'yes' or self.Q == "dnk":
            try:
                self.questions_country.remove("Population over 5m")
            except ValueError:
                pass

        if self.Q == "no":
            try:
                self.questions_country.remove("Pop over 10m ?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Pop over 30m ?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Population over 5m")
            except ValueError:
                pass
    if self.app.root.ids.third.test1 == "In Europe Union ?":
        if self.Q == 'yes' or self.Q == "dnk" or self.Q == "yes":
            try:
                self.questions_country.remove("In Europe Union ?")
            except ValueError:
                pass

    if self.app.root.ids.third.test1 == 'euro in your country?':
        if self.Q == 'yes' or self.Q == "dnk" or self.Q == "yes":
            try:
                self.questions_country.remove('euro in your country?')
            except ValueError:
                pass