#!/usr/bin/python3
#fastmind
#by boot1110001

### IMPORTS ####################################################################
import sys
import getopt
import pygame

from datetime import datetime

from utils import func as uf
from utils.color import Color
from core import func as cf
from core.map import Map
from graphic.rectangle import Rectangle
from graphic.wall import Wall
from graphic.goal import Goal
from graphic.player import Player

### NON EDITABLE VARIABLES #####################################################
window = 0 # glut window number
lvlist = [] # level file list
wmap = [] # wall list
womap = [] # wall object list
goal = 0 # goal object
player = 0 # player object
victory = False
old_time = 0
lvl_time = 0
width = 0
height = 0

hstr='''fastmind, solve mazes...
game options:
 fastmind.py -h\t\t\t--help\t\t\tShow this help.
 fastmind.py -l\t\t\t--list\t\t\tList the available levels.
 fastmind.py -p <level_name>\t--play=<level_name>\tPlay the level.
 fastmind.py -s <square_size>\t--size=<square_size>\tModify the default size (15) of the basic square.'''

### EDITABLE VARIABLES #########################################################
stdsize=15 # test with 10

### FUNCTIONS ##################################################################
def pre_draw_map(maplist,lw,lh,stdsize):
    global wmap, womap, goal, player

    maxx=stdsize*lw
    maxy=stdsize*lh
    x = y = i = 0

    while (y<maxy):
        while (x<maxx):

            if (maplist[i]=='#'):
                # print('['+str(i)+'] ('+str(x)+','+str(y)+') "#"')
                wmap.append([x,y])
                womap.append(Wall(x,y,stdsize,Color.BLUE2))
            elif (maplist[i]=='$'):
                # print('['+str(i)+'] ('+str(x)+','+str(y)+') "$"')
                goal = Goal(x,y,stdsize,Color.RED)
            elif (maplist[i]=='@'):
                # print('['+str(i)+'] ('+str(x)+','+str(y)+') "@"')
                player = Player(x,y,stdsize,Color.GREEN)
            else:
                # print('['+str(i)+'] ('+str(x)+','+str(y)+') " "')
                pass

            i+=1
            x+=stdsize

        x=0
        y+=stdsize

def print_result(screen):
    rectw = 14*stdsize
    recth = 4*stdsize
    rectx = (width/2)-(rectw/2)
    recty = (height/2)-(recth/2)
    borderw = 10
    pygame.draw.rect(screen, Color.WHITE, [rectx, recty, rectw, recth])
    pygame.draw.rect(screen, Color.BLACK, [rectx+borderw, recty+borderw, rectw-(borderw*2), recth-(borderw*2)])
    basicfont = pygame.font.SysFont('Monospace', stdsize)

    text = basicfont.render('GOAL! You pass in:', True, Color.WHITE, Color.BLACK)
    textrect = text.get_rect()
    textrect.centerx = screen.get_rect().centerx
    textrect.centery = screen.get_rect().centery-(stdsize/2)-2
    screen.blit(text, textrect)

    text = basicfont.render(str(lvl_time)+'s', True, Color.WHITE, Color.BLACK)
    textrect = text.get_rect()
    textrect.centerx = screen.get_rect().centerx
    textrect.centery = screen.get_rect().centery+(stdsize/2)+2
    screen.blit(text, textrect)

def display(screen):
    global victory, lvl_time
    # --- PREVIOUS CHECKS ------------------------------------------------------
    if (not victory and (player.x, player.y) == (goal.x, goal.y)):
        new_time = datetime.now()
        lvl_time = new_time - old_time
        print('[GOAL] You pass the level in:', lvl_time)
        victory=True
    # --- DRAWING --------------------------------------------------------------
    # Set the screen background
    screen.fill(Color.BLACK)

    cf.draw_map(womap, screen)
    goal.draw(screen)
    if not victory:
        player.draw(screen)
    else:
        print_result(screen)

def checkMove(x,y):
    out=True
    if ([x,y] in wmap):
        print('[FAIL] NO MOVE')
        out=False
    return out

def specialkey(event):
    xa, ya = player.x, player.y
    if (event.key==pygame.K_UP):
        ya-=stdsize
        if (checkMove(xa,ya)):
            player.move_up()
            xcell=int((xa*(width/stdsize))/width)+1
            ycell=int((ya*(width/stdsize))/width)+1
            print('[ UP ] x: '+str(xa)+'px ('+str(xcell)+') y: '+str(ya)+'px ('+str(ycell)+')')
    elif (event.key==pygame.K_DOWN):
        ya+=stdsize
        if (checkMove(xa,ya)):
            player.move_down()
            xcell=int((xa*(width/stdsize))/width)+1
            ycell=int((ya*(width/stdsize))/width)+1
            print('[DOWN] x: '+str(xa)+'px ('+str(xcell)+') y: '+str(ya)+'px ('+str(ycell)+')')
    elif (event.key==pygame.K_LEFT):
        xa-=stdsize
        if (checkMove(xa,ya)):
            player.move_left()
            xcell=int((xa*(width/stdsize))/width)+1
            ycell=int((ya*(width/stdsize))/width)+1
            print('[LEFT] x: '+str(xa)+'px ('+str(xcell)+') y: '+str(ya)+'px ('+str(ycell)+')')
    elif (event.key==pygame.K_RIGHT):
        xa+=stdsize
        if (checkMove(xa,ya)):
            player.move_right()
            xcell=int((xa*(width/stdsize))/width)+1
            ycell=int((ya*(width/stdsize))/width)+1
            print('[RIGH] x: '+str(xa)+'px ('+str(xcell)+') y: '+str(ya)+'px ('+str(ycell)+')')

### MAIN #######################################################################
def main(argv):
    global stdsize, old_time, lvlist, width, height

    lvlist=cf.get_lvls()
    lvname = '1.lv'
    try:
        opts, args = getopt.getopt(argv,"hp:s:l",["help","play=","size=","list"])
    except getopt.GetoptError:
        print(hstr)
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print(hstr)
            sys.exit()
        elif opt in ("-p", "--play"):
            lvname = arg
        elif opt in ("-s", "--size"):
            stdsize = int(arg)
        elif opt in ("-l", "--list"):
            print('[INFO] Level list:')
            uf.print_list(' > ',lvlist)
            sys.exit()

    if not (lvname in lvlist):
        print("[FAIL] The selected level isn't in the list:")
        uf.print_list(' > ',lvlist)
        sys.exit()

    old_time = datetime.now()
    print('[INFO] Time started at:', old_time)
    m=Map(open('lvls/'+lvname, 'r').read())
    pre_draw_map(m.maplist,m.lvwidth,m.lvheight,stdsize)
    width, height = stdsize*m.lvwidth, stdsize*m.lvheight # window size

    # --- PYGAME INIT ----------------------------------------------------------
    pygame.init()
    # Set the height and width of the screen
    size = [width, height]
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("FASTMIND")
    logo = pygame.image.load('fastmind.png')
    pygame.display.set_icon(logo)
    # Loop until the user clicks the close button.
    done = False
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    # -------- Main Program Loop -----------------------------------------------
    while not done:
        # --- Event Processing
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if not victory:
                if event.type == pygame.KEYDOWN:
                    specialkey(event)
            else:
                if event.type == pygame.KEYDOWN:
                    if (event.key==pygame.K_ESCAPE):
                        print('[ESCP] Exiting...')
                        done = True
                    elif (event.key==pygame.K_RETURN):
                        print('[ENTR] Exiting...')
                        done = True

        # --- Logic
        # --- Drawing
        display(screen)
        # --- Wrap-up
        # Limit to 60 frames per second
        clock.tick(60)

        pygame.display.flip()

    # Close everything down
    pygame.quit()

### EXEC #######################################################################
if __name__ == "__main__":
    main(sys.argv[1:])
