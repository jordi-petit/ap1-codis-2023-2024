"""
Programa que diu si existeix un pic en una
seqüència de reals.
"""

from yogi import *


hi_ha_pics = False
a, b, c = read(float), read(float), scan(float)
while not hi_ha_pics and c != None:
    if a < b > c:
        hi_ha_pics = True
    else:
        a, b, c = b, c, scan(float)
print(hi_ha_pics)
