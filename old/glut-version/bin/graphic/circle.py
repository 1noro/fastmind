#NOT WORKING
#graphic.circle
#by boot1110001

### IMPORTS ####################################################################
import numpy

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

### CLASSES ####################################################################
class Circle:
    def __init__(self, x, y, width, height):
        self.x=x
        self.y=y
        self.width=width
        self.height=height

    def draw(self):
        if(edge_only):
            glBegin(GL_LINE_LOOP)
        else:
            glBegin(GL_POLYGON)

        for vertex in range(0, side_num):
            print vertex
            angle  = float(vertex) * 2.0 * numpy.pi / side_num
            glVertex3f(numpy.cos(angle)*radius, 0.0, numpy.sin(angle)*radius)

        glEnd();

    def __eq__(self,other):
        out=False
        return out
