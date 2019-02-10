#bin.graphic.elements.square
#by boot1110001

### IMPORTS ####################################################################
import pygame
from .rectangle import Rectangle

### CLASSES ####################################################################
class Square(Rectangle):
    def __init__(self, x, y, xcell, ycell, stdsize, color):
        self.x=x
        self.y=y
        self.xcell=xcell
        self.ycell=ycell
        self.width=stdsize
        self.height=stdsize
        self.color=color
        self.stdsize=stdsize

    def set_stdsize(self,new_stdsize):
        self.width=new_stdsize
        self.height=new_stdsize
        self.stdsize=new_stdsize

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, [self.x, self.y, self.width, self.height])

    def __eq__(self,other):
        out=False
        return out
