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

    def __eq__(self,other):
        out=False
        return out
