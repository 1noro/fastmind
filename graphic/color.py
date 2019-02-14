#graphic.color
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

class Scheme2:

    YANKEES_BLUE    = ( 37,  40,  61)
    BABY_POWDER     = (251, 254, 249)
    LIGHT_BLUE      = (173, 217, 244)
    STAR_CMD_BLUE   = ( 14, 121, 178) #STAR_COMMAND_BLUE
    ROSE_RED        = (191,  19,  99)

    BG              = YANKEES_BLUE
    WALL            = STAR_CMD_BLUE
    PLAYER1         = LIGHT_BLUE
    PLAYER2         = YANKEES_BLUE
    GOAL            = ROSE_RED
    RESULT1         = BABY_POWDER
    RESULT2         = Color.BLACK333

    MENU1           = LIGHT_BLUE
    MENU2           = YANKEES_BLUE
    BG_MENU         = MENU2

    LEVEL1          = LIGHT_BLUE
    LEVEL2          = STAR_CMD_BLUE
    BG_LEVEL        = YANKEES_BLUE

class Scheme3:

    DESIRE          = (230,  57,  70)
    HENEYDEW        = (241, 250, 238)
    LIGHT_BLUE2     = (168, 218, 220)
    QUEEN_BLUE2     = ( 69, 123, 157)
    SPACE_CADET     = ( 29,  53,  87)
