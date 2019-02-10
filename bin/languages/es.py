#package bin.languages.spanish __init__
#by boot1110001

### IMPORTS ####################################################################
from .__init__ import default

### CLASSES ####################################################################
class ES(default):
    menu_play =         "  JUGAR  "
    menu_levels =       " NIVELES "
    menu_credits =      " TÍTULOS "
    menu_exit =         "  SALIR  "

    result_txt =        "META!! Conseguido en:"
    result_seconds =    "s"

    help_string = '''fastmind, resuelve laberintos y mide tu tiempo...
opciones del juego:
 fastmind.py -h\t\t\t--help\t\t\tMuestra esta ayuda.
 fastmind.py -l\t\t\t--list\t\t\tLista los nveles disponibles.
 fastmind.py -v\t\t\t--verbose\t\tHabilita el modo detallado.
 fastmind.py -p <nombre_nivel>\t--play=<nombre_nivel>\tJuega el nivel directamente.'''

class GL(default):
    menu_play =         "  XOGO  "
    menu_levels =       "  MAPA  "
    menu_credits =      "  CRED  "
    menu_exit =         "  SAIR  "

    result_txt =        "META!! Conseguido en:"
    result_seconds =    "s"
