# core.logs
# by boot1110001

### CLASSES ####################################################################
class bcolor:
    NONE = ''
    INFO = ''
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    BLACKBG = '\033[40m'
    REDBG = '\033[41m'
    GREENBG = '\033[42m'
    YELLOWBG = '\033[43m'
    BLUEBG = '\033[44m'
    PURPLEBG = '\033[45m'
    CIANBG = '\033[46m'
    WHITEBG = '\033[47m'

class p:
    def init(txt):      print(bcolor.INFO + "[INIT] " + txt + bcolor.ENDC)
    def info(txt):      print(bcolor.INFO + "[INFO] " + txt + bcolor.ENDC)
    def sinfo(txt):     print(bcolor.HEADER + "[INFO] " + txt + bcolor.ENDC)
    def ok(txt):        print(bcolor.OKGREEN + "[ OK ] " + txt + bcolor.ENDC)
    def warning(txt):   print(bcolor.WARNING + "[WARN] " + txt + bcolor.ENDC)
    def fail(txt):      print(bcolor.FAIL + "[FAIL] " + txt + bcolor.ENDC)
    def exit(txt):      print(bcolor.OKBLUE + "[EXIT] " + txt + bcolor.ENDC)
    def loop(txt):      print(bcolor.OKBLUE + "[LOOP] " + txt + bcolor.ENDC)
    def entr(txt):      print(bcolor.INFO + "[ENTR] " + txt + bcolor.ENDC)
    def escp(txt):      print(bcolor.INFO + "[ESCP] " + txt + bcolor.ENDC)
    def up(txt):        print(bcolor.GREENBG + "[ UP ] " + txt + bcolor.ENDC)
    def down(txt):      print(bcolor.YELLOWBG + "[DOWN] " + txt + bcolor.ENDC)
    def left(txt):      print(bcolor.PURPLEBG + "[LEFT] " + txt + bcolor.ENDC)
    def right(txt):     print(bcolor.CIANBG + "[RIGH] " + txt + bcolor.ENDC)
