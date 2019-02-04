#graphic.wall
#by boot1110001

### IMPORTS ####################################################################
from .square import Square

### CLASSES ####################################################################
class Wall(Square):
    def __init__(self, x, y, stdsize, color):
        self.x=x
        self.y=y
        self.width=stdsize
        self.height=stdsize
        self.color=color
        self.stdsize=stdsize

    def move(self,x,y):
        self.x=x
        self.y=y

    def move_left(self):
        self.x-=1

    def move_right(self):
        self.x+=1

    def move_up(self):
        self.y-=1

    def move_down(self):
        self.y+=1

    def __eq__(self,other):
        out=False
        return out
