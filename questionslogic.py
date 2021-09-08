import json
from kivy.app import App
import main2


class Before:
    Contient = [["Albania", "Andorra", "Austria", "Belarus", "Belgium", "Bosnia and Herzegovina", "Bulgaria", "Croatia",
                 "Czech Republic", "Cyprus", "Denmark", "Estonia", "Finland", "France", "Georgia", "Germany", "Greece",
                 "Hungary", "Iceland", "Ireland", "Italy", "Latvia", "Liechtenstein", "Lithuania", "Luxembourg",
                 "Malta",
                 "Moldova", "Monaco", "Montenegro", "Netherlands", "North Macedonia", "Norway", "Poland", "Portugal",
                 "Romania", "Russia", "San Marino", "Serbia", "Slovakia", "Slovenia", "Spain", "Sweden", "Switzerland",
                 "Turkey", "Ukraine", "United Kingdom"], ["Afghanistan", "Armenia", "Azerbaijan", "Bahrain",
                                                          "Bangladesh", "Bhutan", "Brunei", "Cambodia", "China",
                                                          "India", "Indonesia", "Iran", "Iraq", "Israel",
                                                          "Japan", "Jordan", "Kazakhstan", "Kuwait", "Kyrgyzstan",
                                                          "Laos", "Lebanon", "Malaysia", "Maldives",
                                                          "Mongolia", "Myanmar", "Nepal", "North Korea", "Oman",
                                                          "Pakistan", "Philippines", "Qatar", "Saudi Arabia",
                                                          "Singapore", "South Korea", "Sri Lanka", "Palestine", "Syria",
                                                          "Tajikistan", "Thailand", "Timor-Leste",
                                                          "Turkmenistan", "United Arab Emirates", "Uzbekistan",
                                                          "Vietnam", "Yemen"],
                ["Algeria", "Angola", "Benin", "Botswana", "Burkina Faso", "Burundi", "Cabo Verde", "Cameroon",
                 "Central African Republic", "Chad", "Comoros", "Congo", "Côte d'Ivoire", "Djibouti", "DR Congo",
                 "Egypt",
                 "Equatorial Guinea", "Eritrea", "Eswatini", "Ethiopia", "Gabon", "Gambia", "Ghana", "Guinea",
                 "Guinea-Bissau",
                 "Kenya", "Lesotho", "Liberia", "Libya", "Madagascar", "Malawi", "Mali", "Mauritania", "Mauritius",
                 "Morocco",
                 "Mozambique", "Namibia", "Niger", "Nigeria", "Rwanda", "Sao Tome and Principe", "Senegal",
                 "Seychelles",
                 "Sierra Leone", "Somalia", "South Africa", "South Sudan", "Sudan", "Tanzania", "Togo", "Tunisia",
                 "Uganda",
                 "Zambia", "Zimbabwe"],
                ["Argentina", "Bolivia", "Brazil", "Chile", "Colombia", "Ecuador", "Guyana", "Paraguay",
                 "Peru", "Suriname", "Uruguay", "Venezuela"],
                ["Antigua and Barbuda", "Bahamas", "Barbados", "Belize", "Canada", "Costa Rica", "Cuba",
                 "Dominica", "Dominican Republic", "El Salvador", "Grenada", "Guatemala", "Haiti",
                 "Honduras", "Jamaica", "Mexico", "Nicaragua", "Panama", "Saint Kitts and Nevis",
                 "Saint Lucia", "St. Vincent and Grenadines", "Trinidad and Tobago",
                 "United States of America"],
                ["Australia", "Fiji", "Kiribati", "Marshall Islands", "Micronesia", "Nauru", "New Zealand", "Palau",
                 "Papua New Guinea", "Samoa", "Solomon Islands", "Tonga", "Tuvalu", "Vanuatu"]]

    Continent_q = [["In Europe Union ?", "Touches sea mediterean ?", "Population over 5m",
                    "Population over 10m", "Population over 30m", "Speaks German ?", "Speaks French ?",
                    "Part of Yougoslavia ?", "Flag contains red?", "Flag with a cross?", "Flag with Blue cross?",
                    "Speaks Dutch", "Speaks English", "Flag has 3 or more colors ?", "Speaks Italien",
                    "Situated in the Nordic region?", "Euro in your country?"],
                   ["pop over 5m?", "pop over 10m?", "pop over 30m?", "pop over 100m?",
                    "middle east?", "arabic?", "muslim?", "christian?", "Buddhist?", "Folk religion?",
                    "Hindu?", "touches indian ocean?", "pacific ocean?", "flag contains red?",
                    "flag contains blue?", "flag contains green?", "flag contains yellow?", "island?",
                    "star on the flag?", "moon on the flag?", "circled object or sun on the flag?"],
                   ["pop over 5m?", "pop over 10m?", "pop over 30m?", "Island ?",
                    "french ?", "english?", "arabic?", "portuguese", "flag contains 3 or more color",
                    "flag contains red?", "flag contains blue?", "flag contains green?",
                    "flag contains yellow?", "Dominant Religion Muslim?", "Dominant Religion Christian?",
                    "touches atlantic ocean?(including mediterranen sea)",
                    "countries touching indian ocean?(including the red sea,arabian sea)",
                    "star on the flag?", "moon on the flag?"],
                   ["Speaks Spanish ?", "Amazon forest in your country ?", "Population over 5m?",
                    "Population over 10m?", "Population over 30m?", "Touch atlantic ocean ?",
                    "Touch pacific ocean?", "Flag contains red?", "Flag contains blue?",
                    "Flag contains green?", "star on your flag?", "cicrle or sun on your flag?"],
                   ["pop over 5m", "pop over 10m", "pop over 30m", "spanish?", "english?",
                    "flag contains red?", "flag contains blue?", "flag contains yellow?",
                    "flag contains green?", "flag contains star?", "flag contains black?",
                    "country touches atlantic ocean?", "country touching pacific ocean?"],
                   ["Population over 1m? ", "flag contains red?", "flag contains blue?",
                    "flag contains yellow?", "star on your flag?", "flag contains green?",
                    "pop over 10m?"]]

    Questions_First = ["Situated in Europe?", "Situated in Asia?", "Situated in Africa?",
                       "Situated in South?", "Situated in North?", "Situated in Oceany?"]

    def __init__(self):
        self.app = App.get_running_app()
        self.indexchange = 0
        self.index1 = 0
        self.index = 1

    def questionmanager(self):
        ask = self.app.root.ids.third.answer
        if ask == "yes":
            continent_countries = self.Contient[self.indexchange]
            questions_ask = self.Continent_q[self.indexchange]
            if self.indexchange == 5:
                self.results = continent_countries
                main2.create_json_oceany("answers.json", questions_ask, continent_countries)
                with open("answers.json", "r", encoding='utf-8') as f:
                    self.transition(json.loads(f.read()), continent_countries, questions_ask)
            if self.indexchange == 4:
                self.results = continent_countries
                main2.create_json_north("answers.json", questions_ask, continent_countries)
                with open("answers.json", "r", encoding='utf-8') as f:
                    self.transition(json.loads(f.read()), continent_countries, questions_ask)
            if self.indexchange == 3:
                self.results = continent_countries
                main2.create_json_south("answers.json", questions_ask, continent_countries)
                with open("answers.json", "r", encoding='utf-8') as f:
                    self.transition(json.loads(f.read()), continent_countries, questions_ask)
            if self.indexchange == 0:
                self.results = continent_countries
                main2.create_json_europe("answers.json", questions_ask, continent_countries)
                with open("answers.json", "r", encoding='utf-8') as f:
                    self.transition(json.loads(f.read()), continent_countries, questions_ask)
            if self.indexchange == 1:
                self.results = continent_countries
                main2.create_json_asia("answers.json", questions_ask, continent_countries)
                with open("answers.json", "r", encoding='utf-8') as f:
                    self.transition(json.loads(f.read()), continent_countries, questions_ask)
            if self.indexchange == 2:
                self.results = continent_countries
                main2.create_json_africa("answers.json", questions_ask, continent_countries)
                with open("answers.json", "r", encoding='utf-8') as f:
                    self.transition(json.loads(f.read()), continent_countries, questions_ask)

        if ask == "no" or ask == "dnk":
            self.indexchange += 1
            try:
                self.app.root.ids.third.set_question(self.Questions_First[self.indexchange])
            except IndexError:
                self.app.root.ids.third.set_question("Sorry,coudn't guess your country?")
            print(self.app.root.ids.third.index)

    def bienvenu(self):
        self.app.root.ids.third.set_question("Situated in Europe?")

    def transition(self, answers_recieved, continent, questions):
        # print(answers_recieved)
        self.answers = answers_recieved
        self.continent_country = continent
        self.questions_country = questions
        self.app.root.ids.third.set_question(self.questions_country[0])
        self.app.root.ids.third.index += 10
        self.results = self.continent_country

    def get_answeer(self):
        answers = self.answers
        self.Q = self.app.root.ids.third.answer
        set_answer = []
        if self.Q == 'yes' or self.Q == 'no' or self.Q == 'dnk':
            if self.Q == 'dnk':
                set_answer = self.results
            else:
                for country in self.continent_country:
                    if answers[country][self.questions_country[self.index1]] == self.Q:
                        set_answer.append(country)
            if len(self.continent_country) == 46:
                self.europe_check()
            if len(self.continent_country) == 45:
                self.asia_check()

        self.results = set(self.results) & set(set_answer)
        return self.results
    def europe_check(self):
        if self.index == 3:
            if self.Q == 'no':
                self.questions_country.remove("Population over 10m")
                self.questions_country.remove("Population over 30m")

    def asia_check(self):
        if self.index == 1:
            if self.Q == 'no':
                self.questions_country.remove("pop over 5m?")
                self.questions_country.remove("pop over 10m?")
                self.questions_country.remove("pop over 100m?")




    def game_manager(self):
        self.results = self.get_answeer()
        print(self.results)

        if len(self.results) == 1:
            self.displays = list(self.results)
            self.app.root.ids.third.set_question(self.displays[0])
        elif len(self.results) == 0:
            self.app.root.ids.third.set_question("Sorry,coudn't guess your country?")
        else:
            self.app.root.ids.third.set_question(self.questions_country[self.index])
        self.index += 1
        self.index1 += 1


if __name__ == '__main__':
    Before()
