#core.cfunc
#by boot1110001

### IMPORTS ####################################################################
from os import listdir
from os.path import isfile, join

### FUNCTIONS ##################################################################
def get_lvls():
    onlyfiles = [f for f in listdir('lvls') if isfile(join('lvls', f))]
    return onlyfiles

def print_list(string,list):
    for i in list: print(string+str(i))

def print_level_list(lvlist):
    _lvlist=[]
    for lv in lvlist:
        _lvlist.append(lv.replace('.lv',''))
    print_list(' > ',_lvlist)

def draw_map(womap, screen):
    for o in womap: o.draw(screen)

def move_map_left(womap):
    for o in womap: o.move_left()

def move_map_right(womap):
    for o in womap: o.move_right()

def move_map_up(womap):
    for o in womap: o.move_up()

def move_map_down(womap):
    for o in womap: o.move_down()

def checkmove(x, y, wmap, verbose):
    out=True
    if ([x,y] in wmap):
        if verbose : print('[FAIL] ('+str(x)+', '+str(y)+') No move. There is a wall there.')
        out=False
    return out
