"""
Descomposició horària amb funció que retorna diversos valors en una tupla.
"""


from yogi import *


def descomposio_horaria(segons: int) -> tuple[int, int, int]:
    """Descompon un cert nombre de segons en segons, minuts i hores equivalents."""

    h = segons // 3600 
    m = (segons % 3600) // 60 
    s = segons % 60 
    return h, m, s


n = read(int)
segs, mins, hors = descomposio_horaria(n)
print(f"{hors:02d}:{mins:02d}:{segs:02d}")