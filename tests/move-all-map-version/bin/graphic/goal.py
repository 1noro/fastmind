#graphic.goal
#by boot1110001

### IMPORTS ####################################################################
from .square import Square

### CLASSES ####################################################################
class Goal(Square):
    def __init__(self, x, y, xcell, ycell, stdsize, color):
        self.x=x
        self.y=y
        self.xcell=xcell
        self.ycell=ycell
        self.width=stdsize
        self.height=stdsize
        self.color=color
        self.stdsize=stdsize

    def move(self,x,y):
        self.x=x
        self.y=y

    def move_left(self):
        self.x-=self.stdsize

    def move_right(self):
        self.x+=self.stdsize

    def move_up(self):
        self.y-=self.stdsize

    def move_down(self):
        self.y+=self.stdsize

    def __eq__(self,other):
        out=False
        return out
