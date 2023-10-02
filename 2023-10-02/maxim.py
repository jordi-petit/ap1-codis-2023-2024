"""
Calcula el màxim d'una seqüència de reals.
"""

import yogi 

m = yogi.read(float)
for x in yogi.tokens(float):
    if x > m:
        m = x 
print(m)