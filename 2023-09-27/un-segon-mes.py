"""
Rellotge
"""


import time

def suma_un_segon(h: int, m: int, s: int) -> tuple[int, int, int]:
    """Donada una hora de rolltge h:m:s, en retorna una altra, un segon més tard."""

    s = s + 1
    if s == 60:
        s = 0 
        m = m + 1
        if m == 60:
            m = 0 
            h = h + 1 
            if h == 24:
                h = 0 
    return h, m, s



h, m, s = 23, 59, 50 
while True:
    print(f'{h:02d}:{m:02d}:{s:02d}')
    time.sleep(1)  # esperar un segon
    h, m, s = suma_un_segon(h, m, s)
    