


def asia_logic(self):
    if self.app.root.ids.third.test1 == "pop over 100m?":
        if self.Q == 'no' or self.Q == "dnk":
            self.questions_country.remove("pop over 100m?")
        if self.Q == 'yes':
            self.questions_country.remove("pop over 100m?")
            self.questions_country.remove("pop over 30m?")
            self.questions_country.remove("pop over 10m?")
            self.questions_country.remove("pop over 5m?")
            self.questions_country.remove("middle east?")
            self.questions_country.remove("arabic?")

    if self.app.root.ids.third.test1 == "pop over 30m?":
        if self.Q == "dnk":
            try:
                self.questions_country.remove("pop over 30m?")
            except ValueError:
                pass
        if self.Q == 'no':
            try:
                self.questions_country.remove("pop over 100m?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("pop over 30m?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Folk religion?")
            except ValueError:
                pass
        if self.Q == 'yes':
            try:
                self.questions_country.remove("pop over 30m?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("pop over 10m?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("pop over 5m?")
            except ValueError:
                pass

    if self.app.root.ids.third.test1 == "pop over 10m?":
        if self.Q == "dnk":
            try:
                self.questions_country.remove("pop over 10m?")
            except ValueError:
                pass
        if self.Q == 'no':
            try:
                self.questions_country.remove("pop over 100m?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("pop over 30m?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("pop over 10m?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Folk religion?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Hindu?")
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

    if self.app.root.ids.third.test1 == "pop over 5m?":
        if self.Q == 'dnk':
            try:
                self.questions_country.remove("pop over 5m?")
            except ValueError:
                pass
        if self.Q == 'yes':
            try:
                self.questions_country.remove("pop over 5m?")
            except ValueError:
                pass
        if self.Q == 'no':
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
            try:
                self.questions_country.remove("pop over 100m?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Hindu?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Folk religion?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("circled object or sun on the flag?")
            except ValueError:
                pass

    if self.app.root.ids.third.test1 == "middle east?":
        if self.Q == 'dnk' or self.Q == "no":
            try:
                self.questions_country.remove("middle east?")
            except ValueError:
                pass

        if self.Q == "yes":
            try:
                self.questions_country.remove("middle east?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("pop over 100m?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Hindu?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Folk religion?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("christian?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Buddhist?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Island ?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("pacific ocean?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("flag contains yellow?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("moon on the flag?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("circled object or sun on the flag?")
            except ValueError:
                pass
    if self.app.root.ids.third.test1 == "arabic?":
        if self.Q == 'dnk' or self.Q == "no":
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
                self.questions_country.remove("pop over 100m?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Hindu?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Folk religion?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("christian?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Buddhist?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("muslim?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("island?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("pacific ocean?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("flag contains blue?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("flag contains yellow?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("moon on the flag?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("circled object or sun on the flag?")
            except ValueError:
                pass

    if self.app.root.ids.third.test1 == "Hindu?":
        if self.Q == 'dnk' or self.Q == "no":
            try:
                self.questions_country.remove("Hindu?")
            except ValueError:
                pass
        if self.Q == "yes":
            try:
                self.questions_country.remove("Hindu?")
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
                self.questions_country.remove("middle east?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("arabic?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Hindu?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Folk religion?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("christian?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Buddhist?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("muslim?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("island?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("pacific ocean?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("flag contains blue?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("flag contains yellow?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("moon on the flag?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("star on the flag?")
            except ValueError:
                pass
    if self.app.root.ids.third.test1 == "Folk religion?":
        if self.Q == 'dnk' or self.Q == "no":
            try:
                self.questions_country.remove("Folk religion?")
            except ValueError:
                pass
        if self.Q == "yes":
            try:
                self.questions_country.remove("Folk religion?")
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
                self.questions_country.remove("pop over 30m?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("middle east?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("arabic?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Hindu?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("christian?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Buddhist?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("muslim?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("island?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("touches indian ocean?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("pacific ocean?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("flag contains blue?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("flag contains yellow?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("flag contains red?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("flag contains green?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("star on the flag?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("moon on the flag?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("circled object or sun on the flag?")
            except ValueError:
                pass
    if self.app.root.ids.third.test1 == "christian?":
        if self.Q == 'dnk' or self.Q == "no":
            try:
                self.questions_country.remove("christian?")
            except ValueError:
                pass
        if self.Q == "yes":
            try:
                self.questions_country.remove("christian?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("middle east?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("arabic?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Buddhist?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("muslim?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Hindu?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Folk religion?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("flag contains red?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("flag contains green?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("moon on the flag?")
            except ValueError:
                pass
    if self.app.root.ids.third.test1 == "Buddhist?":
        if self.Q == 'dnk' or self.Q == "no":
            try:
                self.questions_country.remove("Buddhist?")
            except ValueError:
                pass
        if self.Q == "yes":
            try:
                self.questions_country.remove("Buddhist?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("christian?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("middle east?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("arabic?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("muslim?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Hindu?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Folk religion?")
            except ValueError:
                pass
    if self.app.root.ids.third.test1 == "muslim?":
        if self.Q == "dnk":
            try:
                self.questions_country.remove("muslim?")
            except ValueError:
                pass
        if self.Q == "no":
            try:
                self.questions_country.remove("muslim?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("arabic?")
            except ValueError:
                pass
        if self.Q == "yes":
            try:
                self.questions_country.remove("muslim?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Buddhist?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("christian?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Hindu?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Folk religion?")
            except ValueError:
                pass

    if self.app.root.ids.third.test1 == "island?":
        if self.Q == 'dnk' or self.Q == "no":
            try:
                self.questions_country.remove("island?")
            except ValueError:
                pass
        if self.Q == "yes":
            try:
                self.questions_country.remove("island?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("middle east?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("arabic?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Hindu?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Folk religion?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("flag contains red?")
            except ValueError:
                pass

    if self.app.root.ids.third.test1 == "touches indian ocean?":
        if self.Q == 'dnk' or self.Q == "no":
            try:
                self.questions_country.remove("touches indian ocean?")
            except ValueError:
                pass
        if self.Q == "yes":
            try:
                self.questions_country.remove("touches indian ocean?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Folk religion?")
            except ValueError:
                pass

    if self.app.root.ids.third.test1 == "pacific ocean?":
        if self.Q == 'dnk' or self.Q == "no":
            try:
                self.questions_country.remove("pacific ocean?")
            except ValueError:
                pass
        if self.Q == "yes":
            try:
                self.questions_country.remove("pacific ocean?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("middle east?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("arabic?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Hindu?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("flag contains red?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("flag contains green?")
            except ValueError:
                pass

    if self.app.root.ids.third.test1 == "flag contains red?":
        if self.Q == 'dnk' or self.Q == "yes":
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
                self.questions_country.remove("Folk religion?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("christian?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("island?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("pacific ocean?")
            except ValueError:
                pass

    if self.app.root.ids.third.test1 == "flag contains blue?":
        if self.Q == 'dnk' or self.Q == "no":
            try:
                self.questions_country.remove("flag contains blue?")
            except ValueError:
                pass
        if self.Q == "yes":
            try:
                self.questions_country.remove("flag contains blue?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("arabic?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Folk religion?")
            except ValueError:
                pass

    if self.app.root.ids.third.test1 == "flag contains green?":
        if self.Q == 'dnk' or self.Q == "no":
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
                self.questions_country.remove("Folk religion?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("christian?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("pacific ocean?")
            except ValueError:
                pass

    if self.app.root.ids.third.test1 == "flag contains yellow?":
        if self.Q == 'dnk' or self.Q == "no":
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
                self.questions_country.remove("middle east?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("arabic?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Hindu?")
            except ValueError:
                pass

    if self.app.root.ids.third.test1 == "star on the flag?":
        if self.Q == 'dnk':
            try:
                self.questions_country.remove("star on the flag?")
            except ValueError:
                pass
        if self.Q == "no":
            try:
                self.questions_country.remove("star on the flag?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Folk religion?")
            except ValueError:
                pass

        if self.Q == "yes":
            try:
                self.questions_country.remove("star on the flag?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Hindu?")
            except ValueError:
                pass

    if self.app.root.ids.third.test1 == "moon on the flag?":
        if self.Q == 'dnk' or self.Q == "no":
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
                self.questions_country.remove("Hindu?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("middle east?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("arabic?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Folk religion?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("christian?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("circled object or sun on the flag?")
            except ValueError:
                pass

    if self.app.root.ids.third.test1 == "circled object or sun on the flag?":
        if self.Q == 'dnk' or self.Q == "no":
            try:
                self.questions_country.remove("circled object or sun on the flag?")
            except ValueError:
                pass

        if self.Q == "yes":
            try:
                self.questions_country.remove("circled object or sun on the flag?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("pop over 5m?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("middle east?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("arabic?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("Folk religion?")
            except ValueError:
                pass
            try:
                self.questions_country.remove("moon on the flag?")
            except ValueError:
                pass