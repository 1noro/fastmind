#graphic.rectangle
#by boot1110001

### IMPORTS ####################################################################
#~from OpenGL.GL import *
#~from OpenGL.GLUT import *
#~from OpenGL.GLU import *

import pygame

### CLASSES ####################################################################
class Rectangle:
    def __init__(self, x, y, width, height, color):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.color=color

    def draw(self, screen):
        #~glBegin(GL_QUADS) # start drawing a rectangle
        #~glVertex2f(self.x, self.y) # bottom left point
        #~glVertex2f(self.x + self.width, self.y) # bottom right point
        #~glVertex2f(self.x + self.width, self.y + self.height) # top right point
        #~glVertex2f(self.x, self.y + self.height) # top left point
        #~glEnd() # done drawing a rectangle

        pygame.draw.rect(screen, (255, 255, 255), [self.x, self.y, self.width, self.height])

    def __eq__(self,other):
        out=False
        return out
