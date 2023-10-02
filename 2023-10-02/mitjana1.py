"""
Calcula la mitjana d'una seqüència de reals que comença amb el
seu nombre d'elements.
"""

import yogi 

n = yogi.read(int)
s = 0
for i in range(n):
    x = yogi.read(float)
    s = s + x 
print(s / n)

