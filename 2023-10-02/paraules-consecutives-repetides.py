"""
Calcula el nombre de paraules consutives repetides en un fitxer de text.
"""

import yogi 

c = 0 

p1 = yogi.scan(str)
if p1 is not None:
    for p2 in yogi.tokens(str):
        if p1 == p2:
            c = c + 1 
        p1 = p2 

print(c)