#core.func
#by boot1110001

### IMPORTS ####################################################################
from os import listdir
from os.path import isfile, join

### FUNCTIONS ##################################################################
def get_lvls():
    onlyfiles = [f for f in listdir('lvls') if isfile(join('lvls', f))]
    return onlyfiles

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

def px2cell(xy,wh,stdsize):
    # 10 --> 1
    # 20 --> ?
    # (20*1)/10 = 2
    return int((xy*(wh/stdsize))/wh)+1

def cell2px(xy,wh,stdsize):
    # 1 --> 10
    # 2 --> ?
    # (2*10)/1 = 20
    return int((xy*wh)/(wh/stdsize))-stdsize
