#graphic.displays
#by boot1110001

### IMPORTS ####################################################################
import pygame
from . import gfunc as gf

### FUNCTIONS ##################################################################
def displaymenu(screen, width, stdsize, pxcenter, mselect, color1, color2, colorbg):
    # --- PREVIOUS CHECKS ------------------------------------------------------
    # --- DRAWING --------------------------------------------------------------
    # Set the screen background
    screen.fill(colorbg)

    # --- Logo background
    pygame.draw.rect(screen, color1, [0, 0, width, 6*stdsize])
    # --- F
    pygame.draw.rect(screen, color2, [pxcenter-(4*stdsize), 1*stdsize, 3*stdsize, stdsize])
    pygame.draw.rect(screen, color2, [pxcenter-(4*stdsize), 2*stdsize, stdsize, 3*stdsize])
    pygame.draw.rect(screen, color2, [pxcenter-(3*stdsize), 3*stdsize, stdsize, stdsize])
    # --- M
    pygame.draw.rect(screen, color2, [pxcenter+(0*stdsize), 1*stdsize, 5*stdsize, stdsize])
    pygame.draw.rect(screen, color2, [pxcenter+(0*stdsize), 2*stdsize, stdsize, 3*stdsize])
    pygame.draw.rect(screen, color2, [pxcenter+(2*stdsize), 2*stdsize, stdsize, 2*stdsize])
    pygame.draw.rect(screen, color2, [pxcenter+(4*stdsize), 2*stdsize, stdsize, 3*stdsize])

    # basicfont = pygame.font.SysFont('Monospace', stdsize)
    basicfont = pygame.font.Font("media/font/ttf/node.ttf", stdsize)

    # --- Play
    if (mselect==0):
        text = basicfont.render('  PLAY  ', True, color2, color1)
    else:
        text = basicfont.render('  PLAY  ', True, color1, color2)
    textrect = text.get_rect()
    textrect.centerx = screen.get_rect().centerx
    textrect.centery = screen.get_rect().centery+(stdsize*0)
    screen.blit(text, textrect)
    # --- Levels
    if (mselect==1):
        text = basicfont.render(' LEVELS ', True, color2, color1)
    else:
        text = basicfont.render(' LEVELS ', True, color1, color2)
    textrect = text.get_rect()
    textrect.centerx = screen.get_rect().centerx
    textrect.centery = screen.get_rect().centery+(stdsize*1.5)
    screen.blit(text, textrect)
    # --- Credits
    if (mselect==2):
        text = basicfont.render('  CRED  ', True, color2, color1)
    else:
        text = basicfont.render('  CRED  ', True, color1, color2)
    textrect = text.get_rect()
    textrect.centerx = screen.get_rect().centerx
    textrect.centery = screen.get_rect().centery+(stdsize*3)
    screen.blit(text, textrect)
    # --- Exit
    if (mselect==3):
        text = basicfont.render('  EXIT  ', True, color2, color1)
    else:
        text = basicfont.render('  EXIT  ', True, color1, color2)
    textrect = text.get_rect()
    textrect.centerx = screen.get_rect().centerx
    textrect.centery = screen.get_rect().centery+(stdsize*4.5)
    screen.blit(text, textrect)

def displaylevel(screen, lvlist, lselect, stdsize, cellscope, color1, color2, colorbg):
    # Set the screen background
    screen.fill(colorbg)

    i = 0
    x, y = 1, 1
    while i<len(lvlist):
        if (i==lselect):
            pygame.draw.rect(screen, color1, [x*stdsize, y*stdsize, stdsize, stdsize])
        else:
            pygame.draw.rect(screen, color2, [x*stdsize, y*stdsize, stdsize, stdsize])
        i+=1
        x+=2
        if (x>=cellscope):
            y+=2
            x=1

def print_result(screen, stdsize, width, height, lvl_time, color1, color2):
    rectw = 14*stdsize
    recth = 4*stdsize
    rectx = (width/2)-(rectw/2)
    recty = (height/2)-(recth/2)
    borderw = stdsize*0.70
    pygame.draw.rect(screen, color1, [rectx, recty, rectw, recth])
    pygame.draw.rect(screen, color2, [rectx+borderw, recty+borderw, rectw-(borderw*2), recth-(borderw*2)])

    # basicfont = pygame.font.SysFont('Monospace', stdsize)
    basicfont = pygame.font.Font("media/font/ttf/node.ttf", stdsize)

    text = basicfont.render('GOAL! You pass in:', True, color1, color2)
    textrect = text.get_rect()
    textrect.centerx = screen.get_rect().centerx
    textrect.centery = screen.get_rect().centery-(stdsize/2)-2
    screen.blit(text, textrect)

    text = basicfont.render(str(lvl_time)+'s', True, color1, color2)
    textrect = text.get_rect()
    textrect.centerx = screen.get_rect().centerx
    textrect.centery = screen.get_rect().centery+(stdsize/2)+2
    screen.blit(text, textrect)

def displaygame(screen, womap, goal, player, victory, stdsize, width, height, lvl_time, color1, color2, colorbg):
    # Set the screen background
    screen.fill(colorbg)

    gf.draw_map(womap, screen)
    goal.draw(screen)
    if not victory:
        player.draw(screen)
    else:
        print_result(screen, stdsize, width, height, lvl_time, color1, color2)
