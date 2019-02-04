#graphic.player
#by boot1110001

### IMPORTS ####################################################################
import pygame
from .square import Square

### CLASSES ####################################################################
class Player(Square):
    def __init__(self, x, y, xcell, ycell, stdsize, color,):
        self.x=x
        self.y=y
        self.xcell=xcell
        self.ycell=ycell
        self.width=stdsize
        self.height=stdsize
        self.color=color
        self.stdsize=stdsize

    def move(self,x,y):
        self.xcell=x
        self.ycell=y

    def move_left(self):
        self.xcell-=1

    def move_right(self):
        self.xcell+=1

    def move_up(self):
        self.ycell-=1

    def move_down(self):
        self.ycell+=1

    def draw(self, screen, xpx, ypx):
        pygame.draw.rect(screen, self.color,[xpx, ypx, self.width, self.height])

    def __eq__(self,other):
        out=False
        return out
