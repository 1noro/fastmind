#graphic.player
#by boot1110001

### IMPORTS ####################################################################
from .rectangle import Rectangle

### CLASES #####################################################################
class Player(Rectangle):
    def __init__(self, x, y, stdsize):
        self.x=x
        self.y=y
        self.width=stdsize
        self.height=stdsize
        self.stdsize=stdsize

    def set_stdsize(self,new_stdsize):
        self.width=new_stdsize
        self.height=new_stdsize
        self.stdsize=stdsize

    def move(self,x,y):
        self.x=x
        self.y=y

    def move_right(self):
        self.x+=self.stdsize

    def move_left(self):
        self.x-=self.stdsize

    def move_up(self):
        self.y+=self.stdsize

    def move_down(self):
        self.y-=self.stdsize

    def __eq__(self,other):
        out=False
        return out
