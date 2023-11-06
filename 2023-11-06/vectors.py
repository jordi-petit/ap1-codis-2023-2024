"""
Algunes operacions amb vectors.
"""


import math 


def suma(v1: list[float], v2: list[float]) -> list[float]:
    """Retorna la suma dels vectors v1, v2. Prec: v1 i v2 són de la mateixa mida"""

    v: list[float] = []
    for i in range(len(v1)):
        v.append(v1[i] + v2[i])
    return v 


def prod_escalar(v1: list[float], v2: list[float]) -> float:

    p = 0
    for i in range(len(v1)):
        p += v1[i] * v2[i]
    return p 


def modul(v: list[float]) -> float:
    return math.sqrt(prod_escalar(v, v))

    
def capicua(v: list[float]) -> bool:
    for i in range(len(v) // 2):
        if v[i] != v[len(v) - i - 1]:
            return False 
    return True


