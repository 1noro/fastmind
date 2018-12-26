from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

window = 0                                             # glut window number
width, height = 400, 400                               # window size

def draw_rect(x, y, width, height):
    glBegin(GL_QUADS)                                  # start drawing a rectangle
    glVertex2f(x, y)                                   # bottom left point
    glVertex2f(x + width, y)                           # bottom right point
    glVertex2f(x + width, y + height)                  # top right point
    glVertex2f(x, y + height)                          # top left point
    glEnd()                                            # done drawing a rectangle

def refresh2d(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, width, 0.0, height, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def draw():                                            # ondraw is called all the time
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # clear the screen
    glLoadIdentity()                                   # reset position
    refresh2d(width, height)                           # set mode to 2d
       
    glColor3f(0.0, 0.0, 1.0)                           # set color to blue
    draw_rect(10, 10, 10, 10)                        # rect at (10, 10) with width 200, height 100
	# ~ a+=1
    glColor3f(0.0, 1.0, 0.0)                           # set color to blue
    draw_rect(a, b, 10, 10)                        # rect at (10, 10) with width 200, height 100
   
    glutSwapBuffers()                                  # important for double buffering
    
########################################################################

xr=0
yr=0

def draw_rect(x, y, width, height):
    glBegin(GL_QUADS)                                  # start drawing a rectangle
    glVertex2f(x, y)                                   # bottom left point
    glVertex2f(x + width, y)                           # bottom right point
    glVertex2f(x + width, y + height)                  # top right point
    glVertex2f(x, y + height)                          # top left point
    glEnd()                                            # done drawing a rectangle

def display():
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # clear the screen

	#BORDER
	glColor3f(0,0,1)			#color blue
	draw_rect(0,0,380,20)		#bootom
	glColor3f(0,1,1)			#color 
	draw_rect(0,20,20,400)		#left
	glColor3f(1,1,1)			#color 
	draw_rect(20,380,400,20)	#top  
	glColor3f(1,0,1)			#color                    
	draw_rect(380,0,20,380)		#right                     
	
	glColor3f(0.0, 1.0, 0.0)		# set color to green
	draw_rect(20+xr, 20+yr, 20, 20)	# rect at (20, 20) with width 20, height 20

	glFlush()
	glutPostRedisplay()
	glutSwapBuffers()
	
def checkMove(x,y):
	out=True
	
	if 
	
	return out

def specialkey(key,x,y):
	global xr, yr
	print('xr:'+str(xr+20)+' yr:'+str(yr+20))
	if (key==GLUT_KEY_UP):
		print('UP')
		yr+=20
	elif (key==GLUT_KEY_DOWN):
		print('DOWN')
		yr-=20
	elif (key==GLUT_KEY_LEFT):
		print('LEFT')
		xr-=20
	elif (key==GLUT_KEY_RIGHT):
		print('RIGHT')
		xr+=20
	
	glutPostRedisplay()

   
def main():
	# initialization
	glutInit()                                             # initialize glut
	glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
	glutInitWindowSize(width, height)                      # set window size
	glutInitWindowPosition(0, 0)                           # set window position
	window = glutCreateWindow("test4")              # create window with title

	glutDisplayFunc(display)                                  # set draw function callback

	glClearColor(0,0,0,0)
	gluOrtho2D(0.0,width,0.0,height)
	glutSpecialFunc(specialkey)

	glutMainLoop()   

main()
