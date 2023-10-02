"""
Calcula la mitjana d'una seqüència de reals que acaba "tota sola"
amb scan().
"""

import yogi 

s = 0.0
n = 0 
x = yogi.scan(float)
while x is not None:
    s = s + x 
    n = n + 1
    x = yogi.scan(float)
print(s / n)
