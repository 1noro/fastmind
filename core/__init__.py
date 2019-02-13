#start.__init__
#by boot1110001

### IMPORTS ####################################################################
import sys, os, re
import getopt
from datetime import datetime
from optparse import OptionParser
# To not show the default message of pygame import
import contextlib
with contextlib.redirect_stdout(None):
    import pygame

import core
from core import cfunc as cf
from core.map import Map
import graphic
from graphic import color
from graphic import displays
from graphic.elements.wall import Wall
from graphic.elements.goal import Goal
from graphic.elements.player import Player
import languages
from languages import *

### EDITABLE VARIABLES #########################################################
lang = en.EN

menu_color_scheme = color.Scheme2
level_color_scheme = color.Scheme2
game_color_scheme = color.Scheme2

stdsize = 40 # 10/15/40...
cellscope = 15 # ODD NUMBER def=15

### AUTOMATIC VARIABLES ########################################################
pxscope = cellscope * stdsize
cellcenter = int((cellscope / 2) + 0.5)
pxcenter = (pxscope / 2) - (stdsize / 2)

home = os.path.expanduser("~")
psv = python_short_version = re.compile(r'([0-9]\.[0-9])\.[0-9] ').match(sys.version).group(1)


### NON EDITABLE VARIABLES #####################################################
# --- Files and folders
version_file = 'version.txt'
icon_file = 'media/icon.ico'
font_file = 'media/node.ttf'
lvls_folder = 'lvls'

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
mmaxselect = 4

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
        print('[INFO] '+lang.time_stopped_at, new_time)
        print('[GOAL] '+lang.you_pass_the_level_in, lvl_time)
        victory = True

def ongamekey(event):
    xcell, ycell = player.xcell, player.ycell
    _xcell, _ycell = xcell, ycell
    if (event.key == pygame.K_UP):
        _ycell-=1
        if (cf.checkmove(xcell, _ycell, wmap, verbose, lang.no_move_wall)):
            player.move_up()
            goal.move_down()
            cf.move_map_down(womap)
            if verbose : print('[ UP ] ('+str(_xcell)+', '+str(ycell)+')')
    elif (event.key == pygame.K_DOWN):
        _ycell+=1
        if (cf.checkmove(xcell, _ycell, wmap, verbose, lang.no_move_wall)):
            player.move_down()
            goal.move_up()
            cf.move_map_up(womap)
            if verbose : print('[DOWN] ('+str(_xcell)+', '+str(ycell)+')')
    elif (event.key == pygame.K_LEFT):
        _xcell-=1
        if (cf.checkmove(_xcell, ycell, wmap, verbose, lang.no_move_wall)):
            player.move_left()
            goal.move_right()
            cf.move_map_right(womap)
            if verbose : print('[LEFT] ('+str(_xcell)+', '+str(ycell)+')')
    elif (event.key == pygame.K_RIGHT):
        _xcell+=1
        if (cf.checkmove(_xcell, ycell, wmap, verbose, lang.no_move_wall)):
            player.move_right()
            goal.move_left()
            cf.move_map_left(womap)
            if verbose : print('[RIGH] ('+str(_xcell)+', '+str(ycell)+')')

def onmenukey(event):
    global mselect
    if (event.key == pygame.K_UP):
        mselect = mselect - 1
        if mselect < 0: mselect = mmaxselect
        if verbose : print('[ UP ] mselect = '+str(mselect))
    elif (event.key == pygame.K_DOWN):
        mselect = mselect + 1
        if mselect > mmaxselect: mselect=0
        if verbose : print('[DOWN] mselect = '+str(mselect))

def onlevelkey(event):
    global lselect
    if (event.key == pygame.K_LEFT):
        lselect-=1
        if lselect < 0: lselect = lmaxselect
        if verbose : print('[LEFT] lselect = '+str(lselect))
    elif (event.key == pygame.K_RIGHT):
        lselect+=1
        if lselect > lmaxselect: lselect = 0
        if verbose : print('[RIGH] lselect = '+str(lselect))

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

    m = Map(open(lvls_folder+'/'+lvname, 'r').read())
    pre_draw_map(m.maplist, m.lvwidth, m.lvheight, stdsize, m.startx, m.starty) # Consider turning this into a class
    print('[INFO] '+lang.playing+m.lvrealname+' ('+lvname+')')
    print('[INFO] '+lang.time_started_at, old_time)

def set_lang(str):
    global lang
    if str == "en.EN":
        print("[INFO] "+lang.set_lang_info+" '"+str+"'")
        lang = en.EN
    elif str == "es.ES":
        print("[INFO] "+lang.set_lang_info+" '"+str+"'")
        lang = es.ES
    elif str == "es.GL":
        print("[INFO] "+lang.set_lang_info+" '"+str+"'")
        lang = es.GL
    else:
        print("[FAIL] '"+str+"' "+lang.set_lang_error)

def print_file_vars():
    print("[INFO] version_file = '"+version_file+"'")
    print("[INFO] icon_file = '"+icon_file+"'")
    print("[INFO] font_file = '"+font_file+"'")
    print("[INFO] lvls_folder = '"+lvls_folder+"'")

### MAIN #######################################################################
def main():
    argv = '' # temporal
    global old_time, lvlist, width, height, verbose, lmaxselect, victory, version, shortversion, display_state

    try:
        version = open(version_file, 'r').read().replace('\n','')
        patron = re.compile(r'(.*\..*\..*)\.')
        shortversion = patron.search(version).group(1)
    except:
        print(lang.version_warning)

    # --- CMD INIT -------------------------------------------------------------
    print(lang.wellcome_msg+version+")")
    print(lang.wellcome_info+pygame.version.ver+")")

    lvlist = cf.get_lvls(lvls_folder)
    lmaxselect = len(lvlist) - 1
    lvname = '1.lv'

    width, height = pxscope, pxscope # window size

    # --- Parameters -----------------------------------------------------------
    parser = OptionParser()
    parser.add_option(
        "-v", "--verbose", dest="verbose",
        action="store_true", default=False,
        help="print status messages to stdout.")
    parser.add_option(
        "-l", "--lang", dest="lang",
        help="changes the default language."
    )
    parser.add_option(
        "-p", "--play", dest="lvshortname",
        help="play the instantly."
    )
    parser.add_option(
        "-s", "--show", dest="show_level_list",
        action="store_true", default=False,
        help="show the available levels.")

    (options, args) = parser.parse_args()

    # --- Verbose
    verbose = options.verbose

    # --- Language
    if options.lang:
        set_lang(options.lang)

    # --- Play instantly
    if options.lvshortname:
        lvname = options.lvshortname+".lv"
        display_state = 1
        if not (lvname in lvlist):
            print(lang.select_level_fail)
            cf.print_level_list(lvlist)
            sys.exit()
        play_level(lvname)

    # --- Show level-list
    if  options.show_level_list:
        print(lang.level_list_msg)
        cf.print_level_list(lvlist)
        sys.exit()

    # --- Post-parameters ------------------------------------------------------
    if verbose: print_file_vars()

    # --- PYGAME INIT ----------------------------------------------------------
    pygame.init()
    # Set the height and width of the screen
    size = [width, height]
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("FASTMIND " + shortversion)
    logo = pygame.image.load(icon_file)
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
                        print('[ESCP] '+lang.exiting)
                        done = True
                    elif (event.key == pygame.K_RETURN):
                        if (mselect == 0):
                            print('[ENTR] '+lang.play_level)
                            display_state = 1
                            play_level(lvname)
                        elif (mselect == 1):
                            print('[ENTR] '+lang.select_level)
                            display_state = 2
                        elif (mselect == 2):
                            print('[ENTR] '+lang.credits)
                            print('[FAIL] '+lang.not_implemented)
                        elif (mselect == 3):
                            print('[ENTR] '+lang.config)
                            print('[FAIL] '+lang.not_implemented)
                        elif (mselect == 4):
                            print('[ENTR] '+lang.exiting)
                            done = True
                        else:
                            print('[ENTR] '+lang.nothing)
                            pass
                    else:
                        onmenukey(event)
            elif (display_state == 1): # on game
                if not victory:
                    if event.type == pygame.KEYDOWN:
                        if (event.key == pygame.K_ESCAPE):
                            print('[ESCP] '+lang.return_to_menu)
                            display_state = 0
                        else:
                            ongamekey(event)
                else:
                    if (event.type == pygame.KEYDOWN):
                        if not (event.key in [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]):
                            print('[INFO] '+lang.key_pressed_return_to_menu)
                            display_state = 0
            elif (display_state == 2): # on menu level
                if event.type == pygame.KEYDOWN:
                    if (event.key == pygame.K_ESCAPE):
                        print('[ESCP] '+lang.return_to_menu)
                        display_state = 0
                    elif (event.key == pygame.K_RETURN):
                        print('[ENTR] '+lang.play_level)
                        display_state = 1
                        lvname = str(lselect)+'.lv'
                        play_level(lvname)
                    else:
                        onlevelkey(event)
        # --- Logic
        # --- Drawing
        if (display_state == 0):
            displays.displaymenu(
                screen, width, stdsize, pxcenter, mselect, font_file,
                menu_color_scheme.MENU1,
                menu_color_scheme.MENU2,
                menu_color_scheme.BG_MENU,
                [   lang.menu_play,
                    lang.menu_levels,
                    lang.menu_credits,
                    lang.menu_config,
                    lang.menu_exit
                ]
            )
        elif (display_state == 1):
            checkvictory()
            displays.displaygame(
                screen, womap, goal, player, victory,
                stdsize, width, height, lvl_time, font_file,
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
