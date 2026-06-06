import msvcrt
from config import KEY_BINDINGS

def get_direction():
    if msvcrt.kbhit():
        key = msvcrt.getwch()

        if key in KEY_BINDINGS:
            return KEY_BINDINGS[key]

    return None
