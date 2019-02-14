#graphic.elements.rectangle
#by boot1110001

### IMPORTS ####################################################################
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
        pygame.draw.rect(screen, self.color, [self.x, self.y, self.width, self.height])

    def __eq__(self,other):
        out=False
        return out
