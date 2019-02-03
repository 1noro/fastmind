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

hstr='''fastmind, solve mazes...
game options:
 fastmind.py -h\t\t\t--help\t\t\tShow this help.
 fastmind.py -l\t\t\t--list\t\t\tList the available levels.
 fastmind.py -p <level_name>\t--play=<level_name>\tPlay the level.
 fastmind.py -s <square_size>\t--size=<square_size>\tModify the default size (15) of the basic square.'''

### EDITABLE VARIABLES #########################################################
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

stdsize=15 # test with 10
stdR, stdG, stdB=Color.BLUE2

### FUNCTIONS ##################################################################
def glut_print( x,  y,  font,  text, r,  g , b , a):
    blending = False
    if glIsEnabled(GL_BLEND) :
        blending = True

    #glEnable(GL_BLEND)
    glColor3f(1,1,1)
    glRasterPos2f(x,y)
    for ch in text :
        glutBitmapCharacter( font , ctypes.c_int( ord(ch) ) )

    if not blending :
        glDisable(GL_BLEND)

def pre_draw_map(maplist,lw,lh,stdsize):
    global wmap, womap, goal, player

    maxx=stdsize*lw
    maxy=stdsize*lh
    x=0
    y=maxy-stdsize
    i=0

    while (y>=0):
        while (x<maxx):

            if (maplist[i]=='#'):
                # ~ print('['+str(i)+'] ('+str(x)+','+str(y)+') "#"')
                wmap.append([x,y])
                womap.append(Wall(x,y,stdsize))
            elif (maplist[i]=='$'):
                # ~ print('['+str(i)+'] ('+str(x)+','+str(y)+') "$"')
                goal = Goal(x,y,stdsize)
            elif (maplist[i]=='@'):
                # ~ print('['+str(i)+'] ('+str(x)+','+str(y)+') "@"')
                player = Player(x,y,stdsize)
            else:
                # ~ print('['+str(i)+'] ('+str(x)+','+str(y)+') " "')
                pass

            i+=1
            x+=stdsize

        x=0
        y-=stdsize

def display():
    global victory, lvl_time
    #~glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # clear the screen
    # --- PREVIOUS CHECKS ------------------------------------------------------
    if (not victory and (player.x, player.y) == (goal.x, goal.y)):
        new_time = datetime.now()
        lvl_time = new_time - old_time
        print('[GOAL] You pass the level in:', lvl_time)
        victory=True
    # --- DRAWING --------------------------------------------------------------
    glColor3f(stdR,stdG,stdB)
    cf.draw_map(womap)
    glColor3f(Color.RED[0],Color.RED[1],Color.RED[2])
    goal.draw()
    if not victory:
        glColor3f(Color.GREEN[0],Color.GREEN[1],Color.GREEN[2])
        player.draw()
    else:
        pass
        #~glut_print(5, 5, GLUT_BITMAP_9_BY_15, 'GOAL!! You pass in: '+str(lvl_time), 1.0, 1.0, 1.0, 1.0)
    # --------------------------------------------------------------------------
    #~glFlush()
    #~glutPostRedisplay()
    #~glutSwapBuffers()

def checkMove(x,y):
    out=True
    if ([x,y] in wmap):
        print('[FAIL] NO MOVE')
        out=False
    return out

def specialkey(key,x,y):
    if not victory:
        xa, ya = player.x, player.y

        if (key==GLUT_KEY_UP):
            ya+=stdsize
            if (checkMove(xa,ya)):
                player.move_up()
                print('[ UP ] xa:'+str(xa)+' ya:'+str(ya))
        elif (key==GLUT_KEY_DOWN):
            ya-=stdsize
            if (checkMove(xa,ya)):
                player.move_down()
                print('[DOWN] xa:'+str(xa)+' ya:'+str(ya))
        elif (key==GLUT_KEY_LEFT):
            xa-=stdsize
            if (checkMove(xa,ya)):
                player.move_left()
                print('[LEFT] xa:'+str(xa)+' ya:'+str(ya))
        elif (key==GLUT_KEY_RIGHT):
            xa+=stdsize
            if (checkMove(xa,ya)):
                player.move_right()
                print('[RIGH] xa:'+str(xa)+' ya:'+str(ya))

    #~glutPostRedisplay()

### MAIN #######################################################################
def main(argv):
    global stdsize, old_time, lvlist

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

    # --- GRAPHIC INIT ---------------------------------------------------------
    #~glutInit() # initialize glut
    #~glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
    #~glutInitWindowSize(width, height) # set window size
    #~glutInitWindowPosition(0, 0) # set window position
    #~window = glutCreateWindow("FASTMIND") # create window with title
    # glutSetWindowTitle("FASTMIND")
    #~glutSetIconTitle("FASTMIND")
    #~glutDisplayFunc(display) # set draw function callback
    #~glClearColor(0,0,0,0)
    #~gluOrtho2D(0.0,width,0.0,height)
    #~glutSpecialFunc(specialkey)
    #~glutMainLoop()

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

        # --- Logic
        #specialkey(key,x,y)

        # --- Drawing
        # Set the screen background
        screen.fill(BLACK)

        # --- Wrap-up

    # Close everything down
    pygame.quit()

### EXEC #######################################################################
if __name__ == "__main__":
    main(sys.argv[1:])
