#core.func
#by boot1110001

### IMPORTS ####################################################################
from os import listdir
from os.path import isfile, join

### FUNCTIONS ##################################################################
def list_lvls():
    onlyfiles = [f for f in listdir('lvls') if isfile(join('lvls', f))]
    for onefile in onlyfiles:
        print(' '+onefile)
