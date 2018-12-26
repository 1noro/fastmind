#!/usr/bin/python
#fastmind
#by boot1110001

### IMPORTS ####################################################################
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

from utils.color import Color

from graphic.rectangle import Rectangle
from graphic.wall import Wall
from graphic.goal import Goal
from graphic.player import Player

### NON EDITABLE VARIABLES #####################################################
window = 0 # glut window number
wmap = [] # wall list
womap = [] # wall object list
goal = 0 # goal object
player = 0 # player object
victory = False

maplist=['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#', ' ', ' ', '#', '#', '#', '#', ' ', '#', '$', '#', ' ', '#', ' ', '#', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#', '#', '#', ' ', ' ', ' ', '#', '#', '#', '#', '#', '#', '#', '#', ' ', '#', '#', '#', '#', '#', '#', '#', '#', ' ', '#', '#', '#', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#', ' ', '#', ' ', ' ', ' ', '#', '#', ' ', ' ', ' ', '#', ' ', '#', '#', '#', '#', ' ', '#', ' ', '#', ' ', '#', ' ', '#', '#', '#', '#', '#', '#', ' ', '#', ' ', ' ', ' ', ' ', '#', ' ', '#', ' ', '#', ' ', '#', ' ', ' ', ' ', '#', '#', ' ', ' ', ' ', '#', ' ', '#', '#', ' ', '#', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#', '#', ' ', '#', '#', '#', ' ', '#', ' ', ' ', '#', ' ', ' ', ' ', '#', '#', '#', '#', '#', ' ', '#', '#', ' ', ' ', ' ', '#', '#', '#', '#', '#', '#', ' ', '#', ' ', '#', ' ', ' ', ' ', '#', ' ', '#', '#', '#', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#', ' ', '#', ' ', ' ', ' ', '#', '#', ' ', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', ' ', '#', ' ', '#', '#', '#', ' ', '#', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', '#', ' ', ' ', '#', '#', ' ', '#', ' ', '#', ' ', '#', '#', '#', '#', '#', '#', '#', '#', '#', ' ', '#', '#', '#', '#', '#', ' ', '#', ' ', '#', ' ', ' ', ' ', '#', ' ', ' ', '#', ' ', '@', '#', ' ', ' ', ' ', ' ', '#', '#', ' ', ' ', ' ', '#', '#', '#', ' ', '#', '#', ' ', '#', ' ', '#', '#', '#', '#', '#', ' ', '#', '#', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', '#', ' ', ' ', ' ', ' ', '#', '#', ' ', '#', '#', '#', '#', '#', ' ', '#', '#', '#', '#', ' ', '#', '#', '#', ' ', '#', ' ', '#', '#', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#']

### EDITABLE VARIABLES #########################################################
width, height = 400, 400 # window size
stdsize=20
stdR, stdG, stdB=Color.BLUE2

### FUNCTIONS ##################################################################
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

def draw_map(womap):
    for o in womap:
        o.draw()

def display():
    global victory
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # clear the screen
    # --- PREVIOUS CHECKS ------------------------------------------------------
    if (not victory and (player.x, player.y) == (goal.x, goal.y)):
        print('[GOAL] You pass the level.')
        victory=True
    # --- DRAWING --------------------------------------------------------------
    glColor3f(stdR,stdG,stdB)
    draw_map(womap)
    glColor3f(Color.RED[0],Color.RED[1],Color.RED[2])
    goal.draw()
    if not victory:
        glColor3f(Color.GREEN[0],Color.GREEN[1],Color.GREEN[2])
        player.draw()
    # --------------------------------------------------------------------------
    glFlush()
    glutPostRedisplay()
    glutSwapBuffers()

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

    glutPostRedisplay()

### MAIN #######################################################################
def main():
    pre_draw_map(maplist,20,20,stdsize)
    # --- GRAPHIC INIT ---------------------------------------------------------
    glutInit() # initialize glut
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
    glutInitWindowSize(width, height) # set window size
    glutInitWindowPosition(0, 0) # set window position
    window = glutCreateWindow("FASTMIND") # create window with title
    glutDisplayFunc(display) # set draw function callback
    glClearColor(0,0,0,0)
    gluOrtho2D(0.0,width,0.0,height)
    glutSpecialFunc(specialkey)
    glutMainLoop()

### EXEC #######################################################################
main()
