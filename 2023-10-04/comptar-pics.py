"""
Programa que compta el nombre de pics d'una
seqüència de reals.
"""

from yogi import *

pics = 0 
a = scan(float) 
if a is not None:
    b = scan(float)
    if b is not None:
        c = scan(float)
        while c != None:
            if a < b > c:
                pics = pics + 1
            a, b, c = b, c, scan(float)
print(pics)
