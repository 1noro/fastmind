#graphic.Player
#by boot1110001

### IMPORTS ####################################################################
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

from .Rectangle import Rectangle

### CLASES #####################################################################
class Wall(Rectangle):
    def __init__(self, x, y, stdsize):
        self.x=x
        self.y=y
        self.width=stdsize
        self.height=stdsize

    def set_stdsize(new_stdsize):
        self.width=new_stdsize
        self.height=new_stdsize

    def __eq__(self,other):
		out=False
		return out
