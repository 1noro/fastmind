#bin.graphic.elements.goal
#by boot1110001

### IMPORTS ####################################################################
import pygame
from .square import Square

### CLASSES ####################################################################
class Goal(Square):
    def __init__(self, x, y, xcell, ycell, stdsize, color):
        self.x=x
        self.y=y
        self.xcell=xcell
        self.ycell=ycell
        self.width=stdsize
        self.height=stdsize
        self.color=color
        self.stdsize=stdsize

    def move(self,x,y):
        self.x=x
        self.y=y

    def move_left(self):
        self.x-=self.stdsize

    def move_right(self):
        self.x+=self.stdsize

    def move_up(self):
        self.y-=self.stdsize

    def move_down(self):
        self.y+=self.stdsize

    def draw(self, screen):
        p1 = ( self.x+(self.width/2), self.y+(self.height*0.15) )
        p2 = ( self.x+(self.width*0.15), self.y+(self.height/2) )
        p3 = ( self.x+(self.width/2), self.y+(self.height*0.85) )
        p4 = ( self.x+(self.width*0.85), self.y+(self.height/2) )

        pygame.draw.polygon(screen, self.color, [p1, p2, p3, p4], 0)

    def __eq__(self,other):
        out=False
        return out
