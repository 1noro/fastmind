#package languages.es
#by boot1110001

### IMPORTS ####################################################################
from .__init__ import default_lang

### CLASSES ####################################################################
class ES(default_lang):
    # --- Graphic --------------------------------------------------------------
    menu_play =         " JUGAR "
    menu_levels =       " NIVELES "
    menu_credits =      " CRÉDITOS "
    menu_config =       " CONFIG "
    menu_exit =         " SALIR "

    result_txt =        "META!! Conseguido en:"
    result_seconds =    "s"

    # --- Shell ----------------------------------------------------------------
    wellcome_msg = "[INIT] Bienvenido a FASTMIND ("
    wellcome_info = "[INFO] Usando pygame ("

    version_warning = "[WARN] El archivo 'version.txt' no se pudo leer"
    select_level_fail = "[FAIL] El nivel seleccionado no está en la lista:"
    level_list_msg = "[INFO] Lista de niveles:"

    exiting = "Saliendo..."
    play_level = "Juagar nivel"
    select_level = "Seleccionar nivel"
    credits = "Créditos"
    config = "Configuración"
    not_implemented = "Aun no implementado :("
    nothing = "Nada"
    return_to_menu = "Volver al menu"
    key_pressed_return_to_menu = "Volver al menu"
    time_stopped_at = "El tiempo se detuvo en:"
    you_pass_the_level_in = "Has pasado el nivel en:"
    playing = "Jugando: "
    time_started_at = "El tiempo comenzó en:"
    no_move_wall = "Ningún movimiento. Hay una pared allí"

    help_string = '''fastmind, resuelve laberintos y mide tu tiempo...
opciones del juego:
 -h\t\t\t--help\t\t\tMuestra esta ayuda.
 -v\t\t\t--verbose\t\tHabilita el modo detallado.
 -l <nombre_idioma>\t--lang=<nombre_idioma>\tCambia el idioma.
 -p <nombre_nivel>\t--play=<nombre_nivel>\tJuega el nivel directamente.
 -s\t\t\t--show\t\t\tMuestra los nveles disponibles.'''

class GL(default_lang):
    # --- Graphic --------------------------------------------------------------
    menu_play =         " XOGO "
    menu_levels =       " NIVEIS "
    menu_credits =      " CRÉDITOS "
    menu_config =       " CONFIG "
    menu_exit =         " SAIR "

    result_txt =        "META!! Conseguido en:"
    result_seconds =    "s"

    # --- Shell ----------------------------------------------------------------
    wellcome_msg = "[INIT] Benvido a FASTMIND ("
    wellcome_info = "[INFO] Usando pygame ("

    version_warning = "[WARN] Non se pode ler o arquivo 'version.txt'"
    select_level_fail = "[FAIL] O nivel seleccionado non se atopa na lista:"
    level_list_msg = "[INFO] Lista de niveis:"

    exiting = "Saíndo..."
    play_level = "Xogar nivel"
    select_level = "Selecionar nivel"
    credits = "Créditos"
    config = "Configuración"
    not_implemented = "Aínda non implementado :("
    nothing = "Nada"
    return_to_menu = "Voltar ó menu"
    key_pressed_return_to_menu = "Voltar ó menu"
    time_stopped_at = "O tempo detívose en:"
    you_pass_the_level_in = "Completaches o nivel en:"
    playing = "Xogando: "
    time_started_at = "O tempo comezou en:"
    no_move_wall = "Ningún movemento. Alí hai unha parede"
