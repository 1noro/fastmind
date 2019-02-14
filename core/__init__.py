#core.__init__
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

# --- Time control
old_time = 0

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
def ongamekey(event, map):
    xcell, ycell = map.player.xcell, map.player.ycell
    _xcell, _ycell = xcell, ycell
    if (event.key == pygame.K_UP):
        _ycell-=1
        if (cf.checkmove(xcell, _ycell, map.wmap, verbose, lang.no_move_wall)):
            map.player.move_up()
            map.goal.move_down()
            map.move_down()
            if verbose : print('[ UP ] ('+str(_xcell)+', '+str(ycell)+')')
    elif (event.key == pygame.K_DOWN):
        _ycell+=1
        if (cf.checkmove(xcell, _ycell, map.wmap, verbose, lang.no_move_wall)):
            map.player.move_down()
            map.goal.move_up()
            map.move_up()
            if verbose : print('[DOWN] ('+str(_xcell)+', '+str(ycell)+')')
    elif (event.key == pygame.K_LEFT):
        _xcell-=1
        if (cf.checkmove(_xcell, ycell, map.wmap, verbose, lang.no_move_wall)):
            map.player.move_left()
            map.goal.move_right()
            map.move_right()
            if verbose : print('[LEFT] ('+str(_xcell)+', '+str(ycell)+')')
    elif (event.key == pygame.K_RIGHT):
        _xcell+=1
        if (cf.checkmove(_xcell, ycell, map.wmap, verbose, lang.no_move_wall)):
            map.player.move_right()
            map.goal.move_left()
            map.move_left()
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

def play_level(lvname):
    global old_time, victory

    victory = False
    old_time = datetime.now()
    map = Map(open(lvls_folder+'/'+lvname, 'r').read(), stdsize, cellcenter, width, height, game_color_scheme)
    print('[INFO] '+lang.playing+map.lvrealname+' ('+lvname+')')
    print('[INFO] '+lang.time_started_at, old_time)
    return map

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

    map = 0

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
        help="play the LEVEL instantly.", metavar="LEVEL"
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
        map = play_level(lvname)

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
                            map = play_level(lvname)
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
                            ongamekey(event, map)
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
                        map = play_level(lvname)
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
            if not victory: victory, lvl_time = map.checkvictory(victory, old_time, lang)
            displays.displaygame(
                screen, map, victory,
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
