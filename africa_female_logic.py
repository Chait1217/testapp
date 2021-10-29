"""
A function that handles the logic of the questions.
"""


def africa_female_logic(self):
    """
    Manages the logic of the questions according to the answers given by the user
    for the female table tennis players situated in Africa.
    """
    Q1 = "Is your player left handed?"
    Q2 = "Did your player participate in 2016 Olympics in singles or team event?"

    if self.app.root.ids.fourth.questions == Q1:
        self.questions_players.remove(Q1)

    if self.app.root.ids.fourth.questions == Q2:
        self.questions_players.remove(Q2)
