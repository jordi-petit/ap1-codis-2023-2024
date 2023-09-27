# mòdul amb exemples de funcions per a màxims i valor absolut

def maxim2(a: int, b: int) -> int:
    """Retorna el màxim de dos enters."""

    if a > b:
        return a
    else: 
        return b 
    

def maxim3(a: int, b: int, c: int) -> int:
    """Retorna el màxim de tres enters."""

    return maxim2(maxim2(a, b), c)


def valor_absolut(n: int) -> int:
    if n >= 0:
        return n 
    return -n


"""
Exemple d'ús:

> python3
>>> import maxims
>>> maxims.maxim2(4, 5)
5
>>>
"""