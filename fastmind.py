#!/usr/bin/python3
#fastmind
#by boot1110001

### IMPORTS ####################################################################
import sys
import getopt
import re
from datetime import datetime
# To not show the default message of pygame import
import contextlib
with contextlib.redirect_stdout(None):
    import pygame

import bin
from bin.core import cfunc as cf
from bin.core.map import Map
from bin.graphic import color
from bin.graphic import displays
from bin.graphic.elements.wall import Wall
from bin.graphic.elements.goal import Goal
from bin.graphic.elements.player import Player
from bin.languages import *

### EDITABLE VARIABLES #########################################################
lang = es.ES

menu_color_scheme = color.Scheme2
level_color_scheme = color.Scheme2
game_color_scheme = color.Scheme2

stdsize = 40 # 10/15/40...
cellscope = 15 # ODD NUMBER def=15

### AUTOMATIC VARIABLES ########################################################
pxscope = cellscope * stdsize
cellcenter = int((cellscope / 2) + 0.5)
pxcenter = (pxscope / 2) - (stdsize / 2)

### NON EDITABLE VARIABLES #####################################################
# --- Version
version = ""
shortversion = ""

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
# 0 - menu
# 1 - game
# 2 - level menu
# 3 - credits
display_state = 0

mselect = 0
mmaxselect = 3

lselect = 0
lmaxselect = 0

victory = False

# --- Run options
verbose = False
hstr = lang.help_string

### FUNCTIONS ##################################################################
def pre_draw_map(maplist, lw, lh, stdsize, startx, starty):
    # Consider turning this into a class
    global wmap, womap, goal, player

    xcellgap = cellcenter - startx
    ycellgap = cellcenter - starty
    xgap = int((xcellgap * width) / (width / stdsize))
    ygap = int((ycellgap * height) / (height / stdsize))

    maxx = stdsize * lw
    maxy = stdsize * lh
    x = y = i = 0

    while (y < maxy):
        while (x < maxx):
            xcell = int((x * (width / stdsize)) / width) + 1
            ycell = int((y * (height / stdsize)) / height) + 1
            if (maplist[i] == '#'):
                wmap.append([xcell, ycell])
                womap.append(Wall(x+xgap, y+ygap, xcell, ycell, stdsize, game_color_scheme.WALL))
            elif (maplist[i] == '$'):
                goal = Goal(x+xgap, y+ygap, xcell, ycell, stdsize, game_color_scheme.GOAL)
            elif (maplist[i] == '@'):
                player = Player(x+xgap, y+ygap, xcell, ycell, stdsize, game_color_scheme.PLAYER1, game_color_scheme.PLAYER2)
            i+=1
            x+=stdsize
        x=0
        y+=stdsize

def checkvictory():
    global victory, lvl_time
    if (not victory and (player.x, player.y) == (goal.x, goal.y)):
        new_time = datetime.now()
        lvl_time = new_time - old_time
        print('[INFO] Time stopped at:', new_time)
        print('[GOAL] You pass the level in:', lvl_time)
        victory = True

def ongamekey(event):
    xcell, ycell = player.xcell, player.ycell
    _xcell, _ycell = xcell, ycell
    if (event.key == pygame.K_UP):
        _ycell-=1
        if (cf.checkmove(xcell, _ycell, wmap, verbose)):
            player.move_up()
            goal.move_down()
            cf.move_map_down(womap)
            if verbose : print('[ UP ] ('+str(_xcell)+', '+str(ycell)+')')
    elif (event.key == pygame.K_DOWN):
        _ycell+=1
        if (cf.checkmove(xcell, _ycell, wmap, verbose)):
            player.move_down()
            goal.move_up()
            cf.move_map_up(womap)
            if verbose : print('[DOWN] ('+str(_xcell)+', '+str(ycell)+')')
    elif (event.key == pygame.K_LEFT):
        _xcell-=1
        if (cf.checkmove(_xcell, ycell, wmap, verbose)):
            player.move_left()
            goal.move_right()
            cf.move_map_right(womap)
            if verbose : print('[LEFT] ('+str(_xcell)+', '+str(ycell)+')')
    elif (event.key == pygame.K_RIGHT):
        _xcell+=1
        if (cf.checkmove(_xcell, ycell, wmap, verbose)):
            player.move_right()
            goal.move_left()
            cf.move_map_left(womap)
            if verbose : print('[RIGH] ('+str(_xcell)+', '+str(ycell)+')')

def onmenukey(event):
    global mselect
    if (event.key == pygame.K_UP):
        mselect = mselect - 1
        if mselect < 0: mselect = mmaxselect
    elif (event.key == pygame.K_DOWN):
        mselect = mselect + 1
        if mselect > mmaxselect: mselect=0

def onlevelkey(event):
    global lselect
    if (event.key == pygame.K_LEFT):
        lselect-=1
        if lselect < 0: lselect = lmaxselect
    elif (event.key == pygame.K_RIGHT):
        lselect+=1
        if lselect > lmaxselect: lselect = 0

def reset_level():
    global victory, wmap, womap, goal, player, old_time, lvl_time

    victory = False

    # --- Level atributes ---
    wmap = [] # wall list
    womap = [] # wall object list
    goal = 0 # goal object
    player = 0 # player object

    # --- Time control ---
    old_time = 0
    lvl_time = 0

def play_level(lvname):
    global old_time

    reset_level()
    old_time = datetime.now()

    m = Map(open('lvls/'+lvname, 'r').read())
    pre_draw_map(m.maplist, m.lvwidth, m.lvheight, stdsize, m.startx, m.starty) # Consider turning this into a class
    print('[INFO] Playing: '+m.lvrealname+' ('+lvname+')')
    print('[INFO] Time started at:', old_time)

### MAIN #######################################################################
def main(argv):
    global old_time, lvlist, width, height, verbose, lmaxselect, victory, version, shortversion, display_state

    try:
        version = open('version.txt', 'r').read().replace('\n','')
        patron = re.compile(r'(.*\..*\..*)\.')
        shortversion = patron.search(version).group(1)
    except:
        print(lang.version_warning)

    # --- CMD INIT -------------------------------------------------------------
    print(lang.wellcome_msg+version+")")
    print(lang.wellcome_info+pygame.version.ver+")")

    lvlist = cf.get_lvls()
    lmaxselect = len(lvlist) - 1
    lvname = '1.lv'

    width, height = pxscope, pxscope # window size

    # --- Parameters -----------------------------------------------------------
    try:
        opts, args = getopt.getopt(argv, "hp:lv", ["help","play=","list","verbose"])
    except getopt.GetoptError:
        print(hstr)
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print(hstr)
            sys.exit()
        elif opt in ("-p", "--play"):
            lvname = arg+".lv"
            onmenu = False
            ongame = True
            if not (lvname in lvlist):
                print(lang.select_level_fail)
                cf.print_level_list(lvlist)
                sys.exit()
            play_level(lvname)
        elif opt in ("-v", "--verbose"):
            verbose = True
        elif opt in ("-l", "--list"):
            print(lang.level_list_msg)
            cf.print_level_list(lvlist)
            sys.exit()

    # --- PYGAME INIT ----------------------------------------------------------
    pygame.init()
    # Set the height and width of the screen
    size = [width, height]
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("FASTMIND " + shortversion)
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
            elif (display_state == 0): # on menu
                if event.type == pygame.KEYDOWN:
                    if (event.key == pygame.K_ESCAPE):
                        print('[ESCP] Exiting...')
                        done = True
                    elif (event.key == pygame.K_RETURN):
                        if (mselect == 0):
                            print('[ENTR] Play level')
                            display_state = 1
                            play_level(lvname)
                        elif (mselect == 1):
                            print('[ENTR] Select level')
                            display_state = 2
                        elif (mselect == 2):
                            print('[ENTR] Not implemented :(')
                        elif (mselect == 3):
                            print('[ENTR] Exiting...')
                            done = True
                        else:
                            print('[ENTR] None')
                            pass
                    else:
                        onmenukey(event)
            elif (display_state == 1): # on game
                if not victory:
                    if event.type == pygame.KEYDOWN:
                        if (event.key == pygame.K_ESCAPE):
                            print('[ESCP] Return to menu')
                            display_state = 0
                        else:
                            ongamekey(event)
                else:
                    if (event.type == pygame.KEYDOWN):
                        if not (event.key in [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]):
                            print('[INFO] Key pressed, return to menu')
                            display_state = 0
            elif (display_state == 2): # on menu level
                if event.type == pygame.KEYDOWN:
                    if (event.key == pygame.K_ESCAPE):
                        print('[ESCP] Return to menu')
                        display_state = 0
                    elif (event.key == pygame.K_RETURN):
                        print('[ENTR] Play level')
                        display_state = 1
                        lvname = str(lselect)+'.lv'
                        play_level(lvname)
                    else:
                        onlevelkey(event)
        # --- Logic
        # --- Drawing
        if (display_state == 0):
            displays.displaymenu(
                screen, width, stdsize, pxcenter, mselect,
                menu_color_scheme.MENU1,
                menu_color_scheme.MENU2,
                menu_color_scheme.BG_MENU,
                [   lang.menu_play,
                    lang.menu_levels,
                    lang.menu_credits,
                    lang.menu_exit
                ]
            )
        elif (display_state == 1):
            checkvictory()
            displays.displaygame(
                screen, womap, goal, player, victory,
                stdsize, width, height, lvl_time,
                game_color_scheme.RESULT1,
                game_color_scheme.RESULT2,
                game_color_scheme.BG,
                [lang.result_txt, lang.result_seconds]
            )
        elif (display_state == 2):
            displays.displaylevel(
                screen, lvlist, lselect, stdsize, cellscope,
                level_color_scheme.LEVEL1,
                level_color_scheme.LEVEL2,
                level_color_scheme.BG_LEVEL
            )
        # --- Wrap-up
        # Limit to 60 frames per second
        clock.tick(60)

        pygame.display.flip()

    # Close everything down
    pygame.quit()

### EXEC #######################################################################
if __name__ == "__main__":
    main(sys.argv[1:])
