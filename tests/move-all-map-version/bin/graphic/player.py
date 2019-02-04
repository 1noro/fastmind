#graphic.player
#by boot1110001

### IMPORTS ####################################################################
from .square import Square

### CLASSES ####################################################################
class Player(Square):
    def __init__(self, x, y, stdsize, color):
        self.x=x
        self.y=y
        self.width=stdsize
        self.height=stdsize
        self.stdsize=stdsize
        self.color=color

    def move(self,x,y):
        self.x=x
        self.y=y

    def move_right(self):
        self.x+=self.stdsize

    def move_left(self):
        self.x-=self.stdsize

    def move_up(self):
        self.y-=self.stdsize

    def move_down(self):
        self.y+=self.stdsize

    def __eq__(self,other):
        out=False
        return out
