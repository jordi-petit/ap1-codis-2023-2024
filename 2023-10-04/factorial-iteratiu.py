"""
Funció per calcular el factorial iterativament
"""


def fact(n: int) -> int:
    """Retorna el factorial de n. Precondició: n >= 0."""

    f = 1 
    for i in range(2, n + 1):
        f = f * i 
    return f 


print(fact(5))