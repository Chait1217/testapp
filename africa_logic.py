def africa_logic(self):
    if self.app.root.ids.third.test1 == "pop over 30m?":
        if self.Q == 'no' or self.Q == "dnk":
            self.questions_country.remove("pop over 30m?")
        if self.Q == "yes":
            self.questions_country.remove("pop over 30m?")
            self.questions_country.remove("pop over 10m?")
            self.questions_country.remove("pop over 5m?")
            self.questions_country.remove("Island ?")

    if self.app.root.ids.third.test1 == "pop over 10m?":
        if self.Q == "dnk":
            try:
                self.questions_country.remove("pop over 10m?")
            except ValueError:
                pass
        if self.Q == 'yes':
            try:
                self.questions_country.remove("pop over 10m?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("pop over 5m?")
            except ValueError:
                pass
        if self.Q == "no":
            try:
                self.questions_country.remove("pop over 10m?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("pop over 30m?")
            except ValueError:
                pass

    if self.app.root.ids.third.test1 == "pop over 5m?":
        if self.Q == "dnk":
            try:
                self.questions_country.remove("pop over 5m?")
            except ValueError:
                pass
        if self.Q == 'yes':
            try:
                self.questions_country.remove("pop over 5m?")
            except ValueError:
                pass
        if self.Q == "no":
            try:
                self.questions_country.remove("pop over 5m?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("pop over 10m?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("pop over 30m?")
            except ValueError:
                pass
    if self.app.root.ids.third.test1 == "Island ?":
        if self.Q == 'no' or self.Q == "dnk":
            try:
                self.questions_country.remove("Island ?")
            except ValueError:
                pass
        if self.Q == "yes":
            try:
                self.questions_country.remove("Island ?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("pop over 30m?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("flag contains 3 or more color")
            except ValueError:
                pass
            try:
                self.questions_country.remove("flag contains red?")
            except ValueError:
                pass
    if self.app.root.ids.third.test1 == "french ?":
        if self.Q == 'no' or self.Q == "dnk":
            try:
                self.questions_country.remove("french ?")
            except ValueError:
                pass
        if self.Q == "yes":
            try:
                self.questions_country.remove("french ?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("flag contains 3 or more color")
            except ValueError:
                pass
    if self.app.root.ids.third.test1 == "english?":
        if self.Q == 'no' or self.Q == "dnk":
            try:
                self.questions_country.remove("english?")
            except ValueError:
                pass
        if self.Q == "yes":
            try:
                self.questions_country.remove("english?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("portuguese")
            except ValueError:
                pass
            try:
                self.questions_country.remove("moon on the flag?")
            except ValueError:
                pass
    if self.app.root.ids.third.test1 == "arabic?":
        if self.Q == 'no' or self.Q == "dnk":
            try:
                self.questions_country.remove("arabic?")
            except ValueError:
                pass
        if self.Q == "yes":
            try:
                self.questions_country.remove("arabic?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("portuguese")
            except ValueError:
                pass
    if self.app.root.ids.third.test1 == "portuguese":
        if self.Q == 'no' or self.Q == "dnk":
            try:
                self.questions_country.remove("portuguese")
            except ValueError:
                pass
        if self.Q == "yes":
            try:
                self.questions_country.remove("portuguese")
            except ValueError:
                pass
            try:
                self.questions_country.remove("english?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("arabic?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("flag contains 3 or more color")
            except ValueError:
                pass
            try:
                self.questions_country.remove("flag contains red?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("moon on the flag?")
            except ValueError:
                pass

    if self.app.root.ids.third.test1 == "flag contains 3 or more color":
        if self.Q == 'yes' or self.Q == "dnk":
            try:
                self.questions_country.remove("portuguese")
            except ValueError:
                pass
            try:
                self.questions_country.remove("flag contains 3 or more color")
            except ValueError:
                pass
        if self.Q == "no":
            try:
                self.questions_country.remove("flag contains 3 or more color")
            except ValueError:
                pass
            try:
                self.questions_country.remove("portuguese")
            except ValueError:
                pass
            try:
                self.questions_country.remove("pop over 5m?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("pop over 10m?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Island ?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("french ?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("flag contains yellow?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Dominant Religion Muslim?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Dominant Religion Christian?")
            except ValueError:
                pass
    if self.app.root.ids.third.test1 == "flag contains red?":
        if self.Q == 'yes' or self.Q == "dnk":
            try:
                self.questions_country.remove("flag contains red?")
            except ValueError:
                pass
        if self.Q == "no":
            try:
                self.questions_country.remove("flag contains red?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Island ?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("portuguese")
            except ValueError:
                pass
            try:
                self.questions_country.remove("moon on the flag?")
            except ValueError:
                pass

    if self.app.root.ids.third.test1 == "flag contains blue?":
        if self.Q == 'no' or self.Q == "dnk" or self.Q == "yes":
            try:
                self.questions_country.remove("flag contains blue?")
            except ValueError:
                pass
    if self.app.root.ids.third.test1 == "flag contains green?":
        if self.Q == "dnk" or self.Q == "yes" or self.Q == "no":
            try:
                self.questions_country.remove("flag contains green?")
            except ValueError:
                pass
    if self.app.root.ids.third.test1 == "flag contains yellow?":
        if self.Q == "dnk" or self.Q == "no" or self.Q == "yes":
            try:
                self.questions_country.remove("flag contains yellow?")
            except ValueError:
                pass
    if self.app.root.ids.third.test1 == "Dominant Religion Muslim?":
        if self.Q == "no" or self.Q == "yes":
            try:
                self.questions_country.remove("Dominant Religion Muslim?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Dominant Religion Christian?")
            except ValueError:
                pass
        if self.Q == "dnk":
            try:
                self.questions_country.remove("Dominant Religion Muslim?")
            except ValueError:
                pass
    if self.app.root.ids.third.test1 == "Dominant Religion Christian?":
        if self.Q == "no" or self.Q == "yes":
            try:
                self.questions_country.remove("Dominant Religion Muslim?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Dominant Religion Christian?")
            except ValueError:
                pass
        if self.Q == "dnk":
            try:
                self.questions_country.remove("Dominant Religion Christian?")
            except ValueError:
                pass
    if self.app.root.ids.third.test1 == "touches atlantic ocean?(including mediterranen sea)":
        if self.Q == "dnk" or self.Q == "no" or self.Q == "yes":
            try:
                self.questions_country.remove("touches atlantic ocean?(including mediterranen sea)")
            except ValueError:
                pass
    if self.app.root.ids.third.test1 == "countries touching indian ocean?(including the red sea,arabian sea)":
        if self.Q == "dnk" or self.Q == "no" or self.Q == "yes":
            try:
                self.questions_country.remove("countries touching indian ocean?(including the red sea,arabian sea)")
            except ValueError:
                pass
    if self.app.root.ids.third.test1 == "star on the flag?":
        if self.Q == "dnk" or self.Q == "no" or self.Q == "yes":
            try:
                self.questions_country.remove("star on the flag?")
            except ValueError:
                pass
    if self.app.root.ids.third.test1 == "moon on the flag?":
        if self.Q == "dnk" or self.Q == "no":
            try:
                self.questions_country.remove("moon on the flag?")
            except ValueError:
                pass
        if self.Q == "yes":
            try:
                self.questions_country.remove("moon on the flag?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("english?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("arabic?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("portuguese")
            except ValueError:
                pass
            try:
                self.questions_country.remove("flag contains red?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Dominant Religion Muslim?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Dominant Religion Christian?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("star on the flag?")
            except ValueError:
                pass