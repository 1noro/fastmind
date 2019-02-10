#package bin.languages.spanish __init__
#by boot1110001

### IMPORTS ####################################################################
from .__init__ import default

### CLASSES ####################################################################
class ES(default):
    # --- Graphic --------------------------------------------------------------
    menu_play =         "  JUGAR  "
    menu_levels =       " NIVELES "
    menu_credits =      " TÍTULOS "
    menu_exit =         "  SALIR  "

    result_txt =        "META!! Conseguido en:"
    result_seconds =    "s"

    # --- Shell ----------------------------------------------------------------
    wellcome_msg = "[INIT] Bienvenido a FASTMIND ("
    wellcome_info = "[INFO] usando pygame ("

    version_warning = "[WARN] El archivo 'version.txt' no se pudo leer"
    select_level_fail = "[FAIL] El nivel seleccionado no está en la lista:"
    level_list_msg = "[INFO] Lista de niveles:"

    exiting = "Saliendo..."
    play_level = "Juagar nivel"
    select_level = "Seleccionar nivel"
    credits = "Creditos"
    not_implemented = "Aun no implementado :("
    none = "Nada"
    return_to_menu = "Volver al menu"
    key_pressed_return_to_menu = "Volver al menu"
    time_stopped_at = "El tiempo se detuvo en:"
    you_pass_the_level_in = "Has pasado el nivel en:"
    playing = "Jugando: "
    time_started_at = "El tiempo comenzó en:"
    no_move_wall = "Ningún movimiento. Hay una pared allí"


    help_string = '''fastmind, resuelve laberintos y mide tu tiempo...
opciones del juego:
 fastmind.py -h\t\t\t--help\t\t\tMuestra esta ayuda.
 fastmind.py -l\t\t\t--list\t\t\tLista los nveles disponibles.
 fastmind.py -v\t\t\t--verbose\t\tHabilita el modo detallado.
 fastmind.py -p <nombre_nivel>\t--play=<nombre_nivel>\tJuega el nivel directamente.'''

class GL(default):
    # --- Graphic --------------------------------------------------------------
    menu_play =         "  XOGO  "
    menu_levels =       "  MAPA  "
    menu_credits =      "  CRED  "
    menu_exit =         "  SAIR  "

    result_txt =        "META!! Conseguido en:"
    result_seconds =    "s"

    # --- Shell ----------------------------------------------------------------
    wellcome_msg = "[INIT] Benvido a FASTMIND ("
    wellcome_info = "[INFO] usando pygame ("
