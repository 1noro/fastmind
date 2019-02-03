#graphic.goal
#by boot1110001

### IMPORTS ####################################################################
from .rectangle import Rectangle

### CLASSES ####################################################################
class Goal(Rectangle):
    def __init__(self, x, y, stdsize, color):
        self.x=x
        self.y=y
        self.width=stdsize
        self.height=stdsize
        self.color=color

    def set_stdsize(self,new_stdsize):
        self.width=new_stdsize
        self.height=new_stdsize

    def __eq__(self,other):
        out=False
        return out
