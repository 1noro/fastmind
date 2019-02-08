#utils.color
#by boot1110001

### CLASES #####################################################################
class Color:

    BLACK           = (  0,   0,   0)
    BLACK222        = ( 34,  34,  34)
    BLACK333        = ( 51,  51,  51)
    WHITE           = (255, 255, 255)
    RED             = (255,   0,   0)
    GREEN           = (  0, 255,   0)
    BLUE            = (  0,   0, 255)
    BLUE2           = ( 76,  76, 255)
    YELLOW          = (250, 255,   2)

    BG              = BLACK
    WALL            = BLUE2
    PLAYER1         = GREEN
    PLAYER2         = BLACK
    GOAL            = RED
    RESULT1         = WHITE
    RESULT2         = BLACK

    BG_MENU         = BLACK

class Scheme1:

    YANKEES_BLUE    = ( 37,  40,  61)
    SMOKY_TOPAZ     = (152,  68,  71)
    LIGHT_BLUE      = (173, 217, 244)
    QUEEN_BLUE      = ( 71, 108, 155)
    STEEL_BLUE      = ( 70, 140, 152)

    BG              = YANKEES_BLUE
    WALL            = QUEEN_BLUE
    PLAYER1         = LIGHT_BLUE
    PLAYER2         = YANKEES_BLUE
    GOAL            = SMOKY_TOPAZ
    RESULT1         = LIGHT_BLUE
    RESULT2         = Color.BLACK333
