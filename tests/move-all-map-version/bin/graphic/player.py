#graphic.player
#by boot1110001

### IMPORTS ####################################################################
import pygame
from .square import Square

### CLASSES ####################################################################
class Player(Square):
    def __init__(self, x, y, stdsize, color):
        self.x=x
        self.y=y
        self.width=stdsize
        self.height=stdsize
        self.stdsize=stdsize
        self.color=color

    def move(self,x,y):
        self.x=x
        self.y=y

    def move_left(self):
        self.x-=1

    def move_right(self):
        self.x+=1

    def move_up(self):
        self.y-=1

    def move_down(self):
        self.y+=1

    def draw(self, screen, xpx, ypx):
        pygame.draw.rect(screen, self.color,[xpx, ypx, self.width, self.height])

    def __eq__(self,other):
        out=False
        return out
