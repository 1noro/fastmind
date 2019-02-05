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

### EDITABLE VARIABLES #########################################################
stdsize = 30 # test with 10 (view with 15)
cellscope = 15 # ODD NUMBER def=15
pxscope = cellscope*stdsize
cellcenter = int((cellscope/2)+0.5)
pxcenter = (pxscope/2)-(stdsize/2)

### NON EDITABLE VARIABLES #####################################################
# --- Level atributes
lvlist = [] # level file list
wmap = [] # wall list
womap = [] # wall object list
goal = 0 # goal object
player = 0 # player object

# --- Time control
old_time = 0
lvl_time = 0

# --- Window dimensions
width = 0
height = 0

# --- State control
ongame = False
onmenu = True
select = 0
maxselect = 3
victory = False

# --- Run options
verbose = False
hstr='''fastmind, solve mazes and measure your time...
game options:
 fastmind.py -h\t\t\t--help\t\t\tShow this help.
 fastmind.py -l\t\t\t--list\t\t\tList the available levels.
 fastmind.py -v\t\t\t--verbose\t\tEnables verbose mode.
 fastmind.py -p <level_name>\t--play=<level_name>\tPlay the level.
 fastmind.py -s <square_size>\t--size=<square_size>\tModify the default size (30) of the basic square.'''

### FUNCTIONS ##################################################################
def pre_draw_map(maplist,lw,lh,stdsize,startx,starty):
    global wmap, womap, goal, player

    xcellgap=cellcenter-startx
    ycellgap=cellcenter-starty
    xgap=int((xcellgap*width)/(width/stdsize))
    ygap=int((ycellgap*height)/(height/stdsize))

    maxx=stdsize*lw
    maxy=stdsize*lh
    x = y = i = 0

    while (y<maxy):
        while (x<maxx):
            xcell=int((x*(width/stdsize))/width)+1
            ycell=int((y*(height/stdsize))/height)+1
            if (maplist[i]=='#'):
                wmap.append([xcell,ycell])
                womap.append(Wall(x+xgap,y+ygap,xcell,ycell,stdsize,Color.BLUE2))
                # print('['+str(i)+'] ('+str(x)+','+str(y)+') ('+str(xcell)+','+str(ycell)+') ('+str(xcell+xcellgap)+','+str(ycell+ycellgap)+') "#"')
            elif (maplist[i]=='$'):
                goal = Goal(x+xgap,y+ygap,xcell,ycell,stdsize,Color.RED)
                # print('['+str(i)+'] ('+str(x)+','+str(y)+') ('+str(xcell)+','+str(ycell)+') "$"')
            elif (maplist[i]=='@'):
                player = Player(x+xgap,y+ygap,xcell,ycell,stdsize,Color.GREEN)
                # print('['+str(i)+'] ('+str(x)+','+str(y)+') ('+str(xcell)+','+str(ycell)+') "@"')
            else:
                # print('['+str(i)+'] ('+str(x)+','+str(y)+') ('+str(xcell)+','+str(ycell)+') " "')
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
    borderw = stdsize*0.70
    pygame.draw.rect(screen, Color.WHITE, [rectx, recty, rectw, recth])
    pygame.draw.rect(screen, Color.BLACK, [rectx+borderw, recty+borderw, rectw-(borderw*2), recth-(borderw*2)])

    # basicfont = pygame.font.SysFont('Monospace', stdsize)
    basicfont = pygame.font.Font("../media/font/ttf/node.ttf", stdsize)

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

def displaygame(screen):
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
        # player.draw(screen, pxcenter, pxcenter)
        player.draw(screen)
    else:
        print_result(screen)

def displaymenu(screen):
    # --- PREVIOUS CHECKS ------------------------------------------------------

    # --- DRAWING --------------------------------------------------------------
    # Set the screen background
    screen.fill(Color.BLACK)

    # --- Logo background
    pygame.draw.rect(screen, Color.YELLOW, [0, 0, width, 6*stdsize])
    # --- F
    pygame.draw.rect(screen, Color.BLACK, [pxcenter-(4*stdsize), 1*stdsize, 3*stdsize, stdsize])
    pygame.draw.rect(screen, Color.BLACK, [pxcenter-(4*stdsize), 2*stdsize, stdsize, 3*stdsize])
    pygame.draw.rect(screen, Color.BLACK, [pxcenter-(3*stdsize), 3*stdsize, stdsize, stdsize])
    # --- M
    pygame.draw.rect(screen, Color.BLACK, [pxcenter+(0*stdsize), 1*stdsize, 5*stdsize, stdsize])
    pygame.draw.rect(screen, Color.BLACK, [pxcenter+(0*stdsize), 2*stdsize, stdsize, 3*stdsize])
    pygame.draw.rect(screen, Color.BLACK, [pxcenter+(2*stdsize), 2*stdsize, stdsize, 2*stdsize])
    pygame.draw.rect(screen, Color.BLACK, [pxcenter+(4*stdsize), 2*stdsize, stdsize, 3*stdsize])

    # basicfont = pygame.font.SysFont('Monospace', stdsize)
    basicfont = pygame.font.Font("../media/font/ttf/node.ttf", stdsize)

    # --- Play
    if (select==0):
        text = basicfont.render('  PLAY  ', True, Color.BLACK, Color.YELLOW)
    else:
        text = basicfont.render('  PLAY  ', True, Color.YELLOW, Color.BLACK)
    textrect = text.get_rect()
    textrect.centerx = screen.get_rect().centerx
    textrect.centery = screen.get_rect().centery+(stdsize*0)
    screen.blit(text, textrect)
    # --- Levels
    if (select==1):
        text = basicfont.render(' LEVELS ', True, Color.BLACK, Color.YELLOW)
    else:
        text = basicfont.render(' LEVELS ', True, Color.YELLOW, Color.BLACK)
    textrect = text.get_rect()
    textrect.centerx = screen.get_rect().centerx
    textrect.centery = screen.get_rect().centery+(stdsize*1.5)
    screen.blit(text, textrect)
    # --- Credits
    if (select==2):
        text = basicfont.render('  CRED  ', True, Color.BLACK, Color.YELLOW)
    else:
        text = basicfont.render('  CRED  ', True, Color.YELLOW, Color.BLACK)
    textrect = text.get_rect()
    textrect.centerx = screen.get_rect().centerx
    textrect.centery = screen.get_rect().centery+(stdsize*3)
    screen.blit(text, textrect)
    # --- Exit
    if (select==3):
        text = basicfont.render('  EXIT  ', True, Color.BLACK, Color.YELLOW)
    else:
        text = basicfont.render('  EXIT  ', True, Color.YELLOW, Color.BLACK)
    textrect = text.get_rect()
    textrect.centerx = screen.get_rect().centerx
    textrect.centery = screen.get_rect().centery+(stdsize*4.5)
    screen.blit(text, textrect)

def checkMove(x,y):
    out=True
    if ([x,y] in wmap):
        if verbose : print('[FAIL] ('+str(x)+', '+str(y)+') No move. There is a wall there.')
        out=False
    return out

def ongamekey(event):
    xcell, ycell = player.xcell, player.ycell
    _xcell, _ycell = xcell, ycell
    if (event.key==pygame.K_UP):
        _ycell-=1
        if (checkMove(xcell,_ycell)):
            player.move_up()
            goal.move_down()
            cf.move_map_down(womap)
            if verbose : print('[ UP ] ('+str(_xcell)+', '+str(ycell)+')')
    elif (event.key==pygame.K_DOWN):
        _ycell+=1
        if (checkMove(xcell,_ycell)):
            player.move_down()
            goal.move_up()
            cf.move_map_up(womap)
            if verbose : print('[DOWN] ('+str(_xcell)+', '+str(ycell)+')')
    elif (event.key==pygame.K_LEFT):
        _xcell-=1
        if (checkMove(_xcell,ycell)):
            player.move_left()
            goal.move_right()
            cf.move_map_right(womap)
            if verbose : print('[LEFT] ('+str(_xcell)+', '+str(ycell)+')')
    elif (event.key==pygame.K_RIGHT):
        _xcell+=1
        if (checkMove(_xcell,ycell)):
            player.move_right()
            goal.move_left()
            cf.move_map_left(womap)
            if verbose : print('[RIGH] ('+str(_xcell)+', '+str(ycell)+')')

def onmenukey(event):
    global select
    if (event.key==pygame.K_UP):
        select=select-1
        if select<0: select=maxselect
    elif (event.key==pygame.K_DOWN):
        select=select+1
        if select>maxselect: select=0

### MAIN #######################################################################
def main(argv):
    global stdsize, old_time, lvlist, width, height, verbose, ongame, onmenu

    lvlist=cf.get_lvls()
    lvname = '1.lv'
    try:
        opts, args = getopt.getopt(argv,"hp:s:lv",["help","play=","size=","list","verbose"])
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
        elif opt in ("-v", "--verbose"):
            verbose = True
        elif opt in ("-l", "--list"):
            print('[INFO] Level list:')
            uf.print_list(' > ',lvlist)
            sys.exit()

    if not (lvname in lvlist):
        print("[FAIL] The selected level isn't in the list:")
        uf.print_list(' > ',lvlist)
        sys.exit()

    # width, height = stdsize*m.lvwidth, stdsize*m.lvheight # window size
    width, height = pxscope, pxscope # window size
    old_time = datetime.now()
    print('[INFO] Time started at:', old_time)
    m=Map(open('lvls/'+lvname, 'r').read())
    pre_draw_map(m.maplist,m.lvwidth,m.lvheight,stdsize,m.startx,m.starty)

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
            elif onmenu:
                if event.type == pygame.KEYDOWN:
                    if (event.key==pygame.K_ESCAPE):
                        print('[ESCP] Exiting...')
                        done = True
                    elif (event.key==pygame.K_RETURN):
                        print('[ENTR] Play level')
                        onmenu = False
                        ongame = True
                    else:
                        onmenukey(event)
            elif ongame:
                if not victory:
                    if event.type == pygame.KEYDOWN:
                        ongamekey(event)
                else:
                    if event.type == pygame.KEYDOWN:
                        if (event.key==pygame.K_ESCAPE):
                            print('[ESCP] Exiting...')
                            done = True
                        elif (event.key==pygame.K_RETURN):
                            print('[ENTR] Return to menu')
                            onmenu = True
                            ongame = False

        # --- Logic
        # --- Drawing
        if onmenu:
            displaymenu(screen)
        elif ongame:
            displaygame(screen)
        # --- Wrap-up
        # Limit to 60 frames per second
        clock.tick(60)

        pygame.display.flip()

    # Close everything down
    pygame.quit()

### EXEC #######################################################################
if __name__ == "__main__":
    main(sys.argv[1:])
