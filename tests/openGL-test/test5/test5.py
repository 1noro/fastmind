from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

window = 0                                             # glut window number
width, height = 400, 400                               # window size

std_size=20

xr=20
yr=20

maplist=['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#', ' ', ' ', '#', '#', '#', '#', ' ', '#', '$', '#', ' ', '#', ' ', '#', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#', '#', '#', ' ', ' ', ' ', '#', '#', '#', '#', '#', '#', '#', '#', ' ', '#', '#', '#', '#', '#', '#', '#', '#', ' ', '#', '#', '#', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#', ' ', '#', ' ', ' ', ' ', '#', '#', ' ', ' ', ' ', '#', ' ', '#', '#', '#', '#', ' ', '#', ' ', '#', ' ', '#', ' ', '#', '#', '#', '#', '#', '#', ' ', '#', ' ', ' ', ' ', ' ', '#', ' ', '#', ' ', '#', ' ', '#', ' ', ' ', ' ', '#', '#', ' ', ' ', ' ', '#', ' ', '#', '#', ' ', '#', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#', '#', ' ', '#', '#', '#', ' ', '#', ' ', ' ', '#', ' ', ' ', ' ', '#', '#', '#', '#', '#', ' ', '#', '#', ' ', ' ', ' ', '#', '#', '#', '#', '#', '#', ' ', '#', ' ', '#', ' ', ' ', ' ', '#', ' ', '#', '#', '#', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#', ' ', '#', ' ', ' ', ' ', '#', '#', ' ', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', ' ', '#', ' ', '#', '#', '#', ' ', '#', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', '#', ' ', ' ', '#', '#', ' ', '#', ' ', '#', ' ', '#', '#', '#', '#', '#', '#', '#', '#', '#', ' ', '#', '#', '#', '#', '#', ' ', '#', ' ', '#', ' ', ' ', ' ', '#', ' ', ' ', '#', ' ', '@', '#', ' ', ' ', ' ', ' ', '#', '#', ' ', ' ', ' ', '#', '#', '#', ' ', '#', '#', ' ', '#', ' ', '#', '#', '#', '#', '#', ' ', '#', '#', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', '#', ' ', ' ', ' ', ' ', '#', '#', ' ', '#', '#', '#', '#', '#', ' ', '#', '#', '#', '#', ' ', '#', '#', '#', ' ', '#', ' ', '#', '#', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#']

cmap=[]

def draw_rect(x, y, width, height):
    glBegin(GL_QUADS)                                  # start drawing a rectangle
    glVertex2f(x, y)                                   # bottom left point
    glVertex2f(x + width, y)                           # bottom right point
    glVertex2f(x + width, y + height)                  # top right point
    glVertex2f(x, y + height)                          # top left point
    glEnd()                                            # done drawing a rectangle

def draw_map(maplist,lw,lh,std_size):
	global cmap
	
	maxx=std_size*lw
	maxy=std_size*lh
	x=0
	y=maxy-std_size
	i=0
	
	while (y>=0):
		while (x<maxx):
			
			if (maplist[i]=='#'):
				# ~ print('['+str(i)+'] ('+str(x)+','+str(y)+') "#"')
				draw_rect(x,y,std_size,std_size)
				cmap.append([x,y])
			elif (maplist[i]=='$'):
				# ~ print('['+str(i)+'] ('+str(x)+','+str(y)+') "$"')
				glColor3f(1,0,0) #color red
				draw_rect(x,y,std_size,std_size)
				glColor3f(0,0,1) #color blue
			elif (maplist[i]=='@'):
				# ~ print('['+str(i)+'] ('+str(x)+','+str(y)+') "@"')
				glColor3f(1,1,1) #color white
				draw_rect(x,y,std_size,std_size)
				glColor3f(0,0,1) #color blue
			# ~ else:
				# ~ print('['+str(i)+'] ('+str(x)+','+str(y)+') " "')
			
			i+=1	
			x+=std_size
		
		x=0
		y-=std_size

def display():
	global maplist, std_size
	
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # clear the screen

	#BORDER
	glColor3f(0,0,1)			#color blue
	draw_map(maplist,20,20,std_size)
	# ~ draw_rect(0,0,380,20)		#bootom
	# ~ glColor3f(0,1,1)			#color 
	# ~ draw_rect(0,20,20,400)		#left
	# ~ glColor3f(1,1,1)			#color 
	# ~ draw_rect(20,380,400,20)	#top  
	# ~ glColor3f(1,0,1)			#color                    
	# ~ draw_rect(380,0,20,380)		#right                     
	
	glColor3f(0.0, 1.0, 0.0)		# set color to green
	draw_rect(xr, yr, 20, 20)	# rect at (20, 20) with width 20, height 20

	glFlush()
	glutPostRedisplay()
	glutSwapBuffers()
	
def checkMove(x,y):
	out=True
	
	# ~ if (x<=0 or x>=380 or y<=0 or y>=380):
		# ~ print('NO MOVE')
		# ~ out=False
		
	if ([x,y] in cmap):
		print('[FAIL] NO MOVE')
		out=False
	
	return out

def specialkey(key,x,y):
	global xr, yr
	xa, ya = xr, yr
	
	if (key==GLUT_KEY_UP):
		ya+=20
		if (checkMove(xa,ya)):
			yr+=20
			print('[ UP ] xr:'+str(xr)+' yr:'+str(yr))
	elif (key==GLUT_KEY_DOWN):
		ya-=20
		if (checkMove(xa,ya)): 
			yr-=20
			print('[DOWN] xr:'+str(xr)+' yr:'+str(yr))
	elif (key==GLUT_KEY_LEFT):
		xa-=20
		if (checkMove(xa,ya)): 
			xr-=20
			print('[LEFT] xr:'+str(xr)+' yr:'+str(yr))
	elif (key==GLUT_KEY_RIGHT):
		xa+=20
		if (checkMove(xa,ya)):
			xr+=20
			print('[RIGH] xr:'+str(xr)+' yr:'+str(yr))
		
	# ~ print('xr:'+str(xr+20)+' yr:'+str(yr+20))
	
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
