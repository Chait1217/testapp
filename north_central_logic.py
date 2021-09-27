def north_central_america_logic(self):
    if self.app.root.ids.third.test1 == "pop over 30m":
        if self.Q == "yes":
            self.questions_country.remove("pop over 30m")
            self.questions_country.remove("spanish?")
            self.questions_country.remove("pop over 10m")
            self.questions_country.remove("pop over 5m")
            self.questions_country.remove("flag contains red?")
            self.questions_country.remove("flag contains yellow?")
            self.questions_country.remove("flag contains black?")
            self.questions_country.remove("country touches atlantic ocean?")
            self.questions_country.remove("country touching pacific ocean?")
        if self.Q == "no" or self.Q == "dnk":
            self.questions_country.remove("pop over 30m")
    if self.app.root.ids.third.test1 == "pop over 10m":
        if self.Q == "dnk":
            try:
                self.questions_country.remove("pop over 10m")
            except ValueError:
                pass
        if self.Q == "no":
            try:
                self.questions_country.remove("pop over 10m")
            except ValueError:
                pass
            try:
                self.questions_country.remove("pop over 30m")
            except ValueError:
                pass
        if self.Q == "yes":
            try:
                self.questions_country.remove("pop over 5m")
            except ValueError:
                pass
            try:
                self.questions_country.remove("pop over 10m")
            except ValueError:
                pass
            try:
                self.questions_country.remove("flag contains yellow?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("flag contains black?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("country touches atlantic ocean?")
            except ValueError:
                pass
    if self.app.root.ids.third.test1 == "pop over 5m":
        if self.Q == "dnk":
            try:
                self.questions_country.remove("pop over 5m")
            except ValueError:
                pass
        if self.Q == "yes":
            try:
                self.questions_country.remove("pop over 5m")
            except ValueError:
                pass
            try:
                self.questions_country.remove("flag contains yellow?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("flag contains black?")
            except ValueError:
                pass
        if self.Q == "no":
            try:
                self.questions_country.remove("pop over 5m")
            except ValueError:
                pass
            try:
                self.questions_country.remove("pop over 10m")
            except ValueError:
                pass
            try:
                self.questions_country.remove("pop over 30m")
            except ValueError:
                pass
            try:
                self.questions_country.remove("country touches atlantic ocean?")
            except ValueError:
                pass
    if self.app.root.ids.third.test1 == "spanish?":
        if self.Q == "dnk":
            try:
                self.questions_country.remove("spanish?")
            except ValueError:
                pass
        if self.Q == "no":
            try:
                self.questions_country.remove("spanish?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("country touches atlantic ocean?")
            except ValueError:
                pass
        if self.Q == "yes":
            try:
                self.questions_country.remove("spanish?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("english?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("flag contains yellow?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("flag contains black?")
            except ValueError:
                pass
    if self.app.root.ids.third.test1 == "english?":
        if self.Q == "dnk":
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
                self.questions_country.remove("spanish?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("country touches atlantic ocean?")
            except ValueError:
                pass
        if self.Q == "no":
            try:
                self.questions_country.remove("english?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("flag contains yellow?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("flag contains black?")
            except ValueError:
                pass
    if self.app.root.ids.third.test1 == "flag contains red?":
        if self.Q == "dnk" or self.Q == "no":
            try:
                self.questions_country.remove("flag contains red?")
            except ValueError:
                pass
        if self.Q == "yes":
            try:
                self.questions_country.remove("flag contains red?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("country touches atlantic ocean?")
            except ValueError:
                pass
    if self.app.root.ids.third.test1 == "flag contains blue?":
        if self.Q == "dnk" or self.Q == "yes":
            try:
                self.questions_country.remove("flag contains blue?")
            except ValueError:
                pass
        if self.Q == "no":
            try:
                self.questions_country.remove("flag contains blue?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("country touches atlantic ocean?")
            except ValueError:
                pass
    if self.app.root.ids.third.test1 == "flag contains yellow?":
        if self.Q == "dnk" or self.Q == "no":
            try:
                self.questions_country.remove("flag contains yellow?")
            except ValueError:
                pass
        if self.Q == "yes":
            try:
                self.questions_country.remove("flag contains yellow?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("country touches atlantic ocean?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("country touching pacific ocean?")
            except ValueError:
                pass
    if self.app.root.ids.third.test1 == "flag contains green?":
        if self.Q == "dnk" or self.Q == "no":
            try:
                self.questions_country.remove("flag contains green?")
            except ValueError:
                pass
        if self.Q == "yes":
            try:
                self.questions_country.remove("flag contains green?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("country touches atlantic ocean?")
            except ValueError:
                pass
    if self.app.root.ids.third.test1 == "flag contains star?":
        if self.Q == "dnk" or self.Q == "no":
            try:
                self.questions_country.remove("flag contains star?")
            except ValueError:
                pass
        if self.Q == "yes":
            try:
                self.questions_country.remove("flag contains star?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("country touches atlantic ocean?")
            except ValueError:
                pass
    if self.app.root.ids.third.test1 == "flag contains black?":
        if self.Q == "dnk" or self.Q == "no":
            try:
                self.questions_country.remove("flag contains black?")
            except ValueError:
                pass
        if self.Q == "yes":
            try:
                self.questions_country.remove("flag contains black?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("country touches atlantic ocean?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("country touching pacific ocean?")
            except ValueError:
                pass
    if self.app.root.ids.third.test1 == "country touches atlantic ocean?":
        if self.Q == "dnk" or self.Q == "no" or self.Q == "yes":
            try:
                self.questions_country.remove("country touches atlantic ocean?")
            except ValueError:
                pass
    if self.app.root.ids.third.test1 == "country touching pacific ocean?":
        if self.Q == "dnk" or self.Q == "no" or self.Q == "yes":
            try:
                self.questions_country.remove("country touching pacific ocean?")
            except ValueError:
                pass