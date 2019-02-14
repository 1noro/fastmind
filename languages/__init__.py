#package languages __init__
#by boot1110001

### IMPORTS ####################################################################
from . import en
from . import es

### EDITABLE VARIABLES #########################################################
default_lang = en.EN

### FUNCTIONS ##################################################################
def set_lang(str):
    lang = default_lang
    if str == "en.EN":
        print("[INFO] "+lang.set_lang_info+" '"+str+"'")
        lang = en.EN
    elif str == "es.ES":
        print("[INFO] "+lang.set_lang_info+" '"+str+"'")
        lang = es.ES
    elif str == "es.GL":
        print("[INFO] "+lang.set_lang_info+" '"+str+"'")
        lang = es.GL
    else:
        print("[FAIL] '"+str+"' "+lang.set_lang_error)
    return lang
