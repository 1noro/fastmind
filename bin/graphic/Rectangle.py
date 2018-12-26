#graphic.Rectangle
#by boot1110001

### IMPORTS ####################################################################
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

### CLASES #####################################################################
class Rectangle:
    def __init__(self, x, y, width, height):
        self.x=x
        self.y=y
        self.width=width
        self.height=height

    def draw(self):
        glBegin(GL_QUADS) # start drawing a rectangle
        glVertex2f(self.x, self.y) # bottom left point
        glVertex2f(self.x + self.width, self.y) # bottom right point
        glVertex2f(self.x + self.width, self.y + self.height) # top right point
        glVertex2f(self.x, self.y + self.height) # top left point
        glEnd() # done drawing a rectangle

    def __eq__(self,other):
		out=False
		return out
