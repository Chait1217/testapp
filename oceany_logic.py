


def oceany_logic(self):
    if self.app.root.ids.third.test1 == "pop over 10m?":
        if self.Q == 'no' or self.Q == "dnk":
            self.questions_country.remove("pop over 10m?")
        if self.Q == 'yes':
            self.questions_country.remove("pop over 10m?")
            self.questions_country.remove("pop over 1 million?")
            self.questions_country.remove("flag contains green?")
            self.questions_country.remove("flag contains blue?")
            self.questions_country.remove("flag contains stars?")
            self.questions_country.remove("flag contains red?")
            self.questions_country.remove("flag contains yellow?")
    if self.app.root.ids.third.test1 == "pop over 1 million?":
        if self.Q == 'no' or self.Q == "dnk":
            try:
                self.questions_country.remove("pop over 1 million?")
            except ValueError:
                pass
        if self.Q == 'yes':
            try:
                self.questions_country.remove("pop over 1 million?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("flag contains green?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("flag contains stars?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("flag contains red?")
            except ValueError:
                pass

    if self.app.root.ids.third.test1 == "flag contains green?":
        if self.Q == 'no' or self.Q == "dnk":
            try:
                self.questions_country.remove("flag contains green?")
            except ValueError:
                pass
        if self.Q == 'yes':
            try:
                self.questions_country.remove("flag contains green?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("pop over 10m?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("pop over 1 million?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("flag contains yellow?")
            except ValueError:
                pass
    if self.app.root.ids.third.test1 == "flag contains blue?":
        if self.Q == 'yes' or self.Q == "dnk":
            try:
                self.questions_country.remove("flag contains blue?")
            except ValueError:
                pass
        if self.Q == 'no':
            try:
                self.questions_country.remove("flag contains blue?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("pop over 10m?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("flag contains red?")
            except ValueError:
                pass
    if self.app.root.ids.third.test1 == "flag contains stars?":
        if self.Q == 'yes' or self.Q == "dnk":
            try:
                self.questions_country.remove("flag contains stars?")
            except ValueError:
                pass
        if self.Q == 'no':
            try:
                self.questions_country.remove("flag contains stars?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("pop over 10m?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("pop over 1 million?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("pop over 1 million?")
            except ValueError:
                pass
    if self.app.root.ids.third.test1 == "flag contains red?":
        if self.Q == 'yes' or self.Q == "dnk":
            try:
                self.questions_country.remove("flag contains red?")
            except ValueError:
                pass
        if self.Q == 'no':
            try:
                self.questions_country.remove("pop over 10m?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("pop over 1 million?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("flag contains blue?")
            except ValueError:
                pass

    if self.app.root.ids.third.test1 == "flag contains yellow?":
        if self.Q == "dnk":
            try:
                self.questions_country.remove("flag contains yellow?")
            except ValueError:
                pass
        if self.Q == 'no':
            try:
                self.questions_country.remove("flag contains green?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("flag contains yellow?")
            except ValueError:
                pass
        if self.Q == 'yes':
            try:
                self.questions_country.remove("flag contains yellow?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("pop over 10m?")
            except ValueError:
                pass