def south_america_logic(self):
    if self.app.root.ids.third.test1 == "Speaks Spanish ?":
        if self.Q == "dnk" or self.Q == "yes":
            self.questions_country.remove("Speaks Spanish ?")
        if self.Q == "no":
            self.questions_country.remove("Speaks Spanish ?")
            self.questions_country.remove("Amazon forest in your country ?")
            self.questions_country.remove("Touch atlantic ocean ?")
            self.questions_country.remove("Touch pacific ocean?")
            self.questions_country.remove("Flag contains blue?")
            self.questions_country.remove("Flag contains green?")

    if self.app.root.ids.third.test1 == "Amazon forest in your country ?":
        if self.Q == "yes" or self.Q == "dnk":
            try:
                self.questions_country.remove("Amazon forest in your country ?")
            except ValueError:
                pass
        if self.Q == "no":
            try:
                self.questions_country.remove("Amazon forest in your country ?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Speaks Spanish ?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Flag contains blue?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Flag contains green?")
            except ValueError:
                pass
    if self.app.root.ids.third.test1 == "Population over 30m?":
        if self.Q == "no" or self.Q == "dnk":
            try:
                self.questions_country.remove("Population over 30m?")
            except ValueError:
                pass
        if self.Q == "yes":
            try:
                self.questions_country.remove("Population over 30m?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Population over 10m?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Population over 5m?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("star on your flag?")
            except ValueError:
                pass
    if self.app.root.ids.third.test1 == "Population over 10m?":
        if self.Q == "no":
            try:
                self.questions_country.remove("Population over 10m?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Population over 30m?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Touch pacific ocean?")
            except ValueError:
                pass
        if self.Q == "yes":
            try:
                self.questions_country.remove("Population over 10m?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Population over 5m?")
            except ValueError:
                pass
        if self.Q == "dnk":
            try:
                self.questions_country.remove("Population over 10m?")
            except ValueError:
                pass
    if self.app.root.ids.third.test1 == "Population over 5m?":
        if self.Q == "yes" or self.Q == "dnk":
            try:
                self.questions_country.remove("Population over 5m?")
            except ValueError:
                pass
        if self.Q == "no":
            try:
                self.questions_country.remove("Population over 5m?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Population over 10m?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Population over 30m?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Touch atlantic ocean ?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Touch pacific ocean?")
            except ValueError:
                pass

    if self.app.root.ids.third.test1 == "Touch atlantic ocean ?":
        if self.Q == "yes" or self.Q == "dnk":
            try:
                self.questions_country.remove("Touch atlantic ocean ?")
            except ValueError:
                pass
        if self.Q == "no":
            try:
                self.questions_country.remove("Touch atlantic ocean ?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Speaks Spanish ?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Population over 5m?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Flag contains red?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("star on your flag?")
            except ValueError:
                pass
    if self.app.root.ids.third.test1 == "Touch pacific ocean?":
        if self.Q == "no" or self.Q == "dnk":
            try:
                self.questions_country.remove("Touch pacific ocean?")
            except ValueError:
                pass
        if self.Q == "yes":
            try:
                self.questions_country.remove("Touch pacific ocean?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Speaks Spanish ?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Population over 10m?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Population over 5m?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Flag contains red?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Flag contains green?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("cicrle or sun on your flag?")
            except ValueError:
                pass

    if self.app.root.ids.third.test1 == "Flag contains red?":
        if self.Q == "yes" or self.Q == "dnk":
            try:
                self.questions_country.remove("Flag contains red?")
            except ValueError:
                pass
        if self.Q == "no":
            try:
                self.questions_country.remove("Flag contains red?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("star on your flag?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("cicrle or sun on your flag?")
            except ValueError:
                pass

    if self.app.root.ids.third.test1 == "Flag contains blue?":
        if self.Q == "yes" or self.Q == "dnk":
            try:
                self.questions_country.remove("Flag contains blue?")
            except ValueError:
                pass
        if self.Q == "no":
            try:
                self.questions_country.remove("Flag contains blue?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Amazon forest in your country ?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Flag contains red?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("cicrle or sun on your flag?")
            except ValueError:
                pass
    if self.app.root.ids.third.test1 == "Flag contains green?":
        if self.Q == "no" or self.Q == "dnk":
            try:
                self.questions_country.remove("Flag contains green?")
            except ValueError:
                pass
        if self.Q == "yes":
            try:
                self.questions_country.remove("Flag contains green?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Amazon forest in your country ?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Touch pacific ocean?")
            except ValueError:
                pass
    if self.app.root.ids.third.test1 == "star on your flag?":
        if self.Q == "no" or self.Q == "dnk":
            try:
                self.questions_country.remove("star on your flag?")
            except ValueError:
                pass
        if self.Q == "yes":
            try:
                self.questions_country.remove("star on your flag?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Population over 30m?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Touch atlantic ocean ?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Flag contains red?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("cicrle or sun on your flag?")
            except ValueError:
                pass
    if self.app.root.ids.third.test1 == "cicrle or sun on your flag?":
        if self.Q == "no" or self.Q == "dnk":
            try:
                self.questions_country.remove("cicrle or sun on your flag?")
            except ValueError:
                pass
        if self.Q == "yes":
            try:
                self.questions_country.remove("cicrle or sun on your flag?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Touch pacific ocean?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Flag contains blue?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("star on your flag?")
            except ValueError:
                pass