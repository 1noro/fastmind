#!/usr/bin/python
#fastmind
#by boot1110001

### IMPORTS ####################################################################
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

from graphic.rectangle import Rectangle
from graphic.wall import Wall

### NON EDITABLE VARIABLES #####################################################
window = 0 # glut window number

BLACK   = (0.0, 0.0, 0.0)
WHITE   = (1.0, 1.0, 1.0)
RED     = (1.0, 0.0, 0.0)
GREEN   = (0.0, 1.0, 0.0)
BLUE    = (0.0, 0.0, 1.0)
BLUE2   = (0.3, 0.3, 1.0)

### EDITABLE VARIABLES #########################################################
width, height = 400, 400 # window size
stdsize=20
stdR, stdG, stdB=BLUE2

### FUNCTIONS ##################################################################
def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # clear the screen

    a=Wall(20,20,stdsize)

    glColor3f(stdR, stdG, stdB) #color
    a.draw()

    glFlush()
    glutPostRedisplay()
    glutSwapBuffers()

### MAIN #######################################################################
def main():
    glutInit() # initialize glut
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
    glutInitWindowSize(width, height) # set window size
    glutInitWindowPosition(0, 0) # set window position
    window = glutCreateWindow("test4") # create window with title

    glutDisplayFunc(display) # set draw function callback

    glClearColor(0,0,0,0)
    gluOrtho2D(0.0,width,0.0,height)
    # glutSpecialFunc(specialkey)

    glutMainLoop()

### EXEC #######################################################################
main()
