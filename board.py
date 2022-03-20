## board.py
## A class dedicated to anything associated with the board

from graphics import *

class Board():
    def __init__(self, numPlayers):
        self.num = numPlayers
        self.win = GraphWin("Checkers", 500, 500)
        self.point = Point(200, 200)
        self.point.draw(self.win)
    
    def theWindow(self):
        return self.win


