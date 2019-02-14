#core.cfunc
#by boot1110001

### IMPORTS ####################################################################
from os import listdir
from os.path import isfile, join

### FUNCTIONS ##################################################################
def get_lvls(dir):
    onlyfiles = [f for f in listdir(dir) if isfile(join('lvls', f))]
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

def checkmove(x, y, wmap, verbose, txt):
    out=True
    if ([x,y] in wmap):
        if verbose : print('[FAIL] ('+str(x)+', '+str(y)+') '+txt)
        out=False
    return out
