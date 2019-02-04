#graphic.rectangle
#by boot1110001

### IMPORTS ####################################################################
import pygame
from .rectangle import Rectangle

### CLASSES ####################################################################
class Square(Rectangle):
    def __init__(self, x, y, stdsize, color):
        self.x=x
        self.y=y
        self.width=stdsize
        self.height=stdsize
        self.color=color
        self.stdsize=stdsize

    def set_stdsize(self,new_stdsize):
        self.width=new_stdsize
        self.height=new_stdsize
        self.stdsize=new_stdsize

    def cell2px(self,xy,wh,stdsize):
        # 1 --> 10
        # 2 --> ?
        # (2*10)/1 = 20
        return int((xy*wh)/(wh/stdsize))-stdsize

    def draw(self, screen, mwidth, mheight):
        pygame.draw.rect(screen, self.color,
            [self.cell2px(self.x,mwidth,self.stdsize),
                self.cell2px(self.y,mheight,self.stdsize),
                self.width, self.height])

    def __eq__(self,other):
        out=False
        return out
