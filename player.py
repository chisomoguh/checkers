## player.py
## Class of a human and computer player

class Player():
    def __init__(self, name, color):
        self.name = name
        self.color = color
    
    def getName(self):
        return self.name

    def getColor(self):
        return self.color
    