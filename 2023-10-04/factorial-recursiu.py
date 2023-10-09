"""
Funció per calcular el factorial recursivament
"""


def fact(n: int) -> int:
    """Retorna el factorial de n. Precondició: n >= 0."""

    if n == 0:
        return 1 
    else:
        return n * fact(n - 1)
    



print(fact(5))