#Eine Reihe des KniffelBlock.
class Row():
    def __init__(self,playerName,components,full):
        self.playerName = playerName
        self.components = components
        self.full = full

class Cube():
    def __init__(self,amount,state):
        self.amount = amount # Die Zahl die im Würfel gespeichert wird.
        self.state = state # State gibt an ob der Würfel gesperrt wurde. D.h. er wird bei den weiteren Würfen des Spielers nicht mehr verändert



