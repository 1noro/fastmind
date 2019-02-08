#graphic.player
#by boot1110001

### IMPORTS ####################################################################
import pygame
from .square import Square

### CLASSES ####################################################################
class Player(Square):
    def __init__(self, x, y, xcell, ycell, stdsize, color1, color2):
        self.x=x
        self.y=y
        self.xcell=xcell
        self.ycell=ycell
        self.width=stdsize
        self.height=stdsize
        self.color1=color1
        self.color2=color2
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

    def draw(self, screen):
        pygame.draw.rect(screen, self.color1, [self.x, self.y, self.width, self.height])

        # p1 = ( self.x+(self.width/2), self.y+(self.height*0.25) )
        # p2 = ( self.x+(self.width*0.25), self.y+(self.height/2) )
        # p3 = ( self.x+(self.width/2), self.y+(self.height*0.75) )
        # p4 = ( self.x+(self.width*0.75), self.y+(self.height/2) )

        p1 = ( self.x+(self.width/2), self.y+(self.height*0.15) )
        p2 = ( self.x+(self.width*0.15), self.y+(self.height/2) )
        p3 = ( self.x+(self.width/2), self.y+(self.height*0.85) )
        p4 = ( self.x+(self.width*0.85), self.y+(self.height/2) )

        pygame.draw.polygon(screen, self.color2, [p1, p2, p3, p4], 0)

    def __eq__(self,other):
        out=False
        return out
