"""
Calcula la mitjana d'una seqüència de reals que acaba amb
el valor especial "final".
"""

import yogi 

n = 0
s = 0.0
x = yogi.read(str)
while x != "final":
    s = s + float(x)
    n = n + 1
    x = yogi.read(str)
print(s / n)

