"""
Programa per escriure tots els divisors d'un natural 
en ordre i eficientment.
"""

from yogi import read

def escriure_divisors(n: int) -> None:
    """Escriu tots els divisors de n, en ordre creixent."""

    i = 1
    while i * i < n:
        if n % i == 0:
            print(i)
        i = i + 1
    if i * i == n:
        print(i)
    i = i - 1
    while i >= 1:
        if n % i == 0:
            print(n // i)
        i = i - 1
    

escriure_divisors(read(int))