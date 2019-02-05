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
