"""
Calcula la mitjana d'una seqüència de reals que acaba "tota sola"
amb tokens().
"""

import yogi 

s = 0.0 
n = 0 
for x in yogi.tokens(float):
    s = s + x 
    n = n + 1 
print(s / n)
