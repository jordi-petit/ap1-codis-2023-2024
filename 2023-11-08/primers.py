"""Garbell d'Eratostenes"""


def es_primer(n: int) -> bool:
    """Indica si el natural n és primer o no."""

    if n <= 1:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d = d + 1
    return True


def llista_primers1(m: int) -> list[int]:
    """Retorna la llista de tots els nombres primers fins a m (inclòs)."""

    return [i for i in range(m + 1) if es_primer(i)]


def llista_primers2(m: int) -> list[int]:
    """Retorna la llista de tots els nombres primers fins a m (inclòs). Prec: m >= 2"""

    return [2] + [i for i in range(1, m + 1, 2) if es_primer(i)]


def llista_primers(m: int) -> list[int]:
    """Retorna la llista de tots els nombres primers fins a m (inclòs). Prec: m >= 2"""

    ps = garbell_eratostenes(m)
    return [i for i in range(m + 1) if ps[i]]


def garbell_eratostenes(m: int) -> list[bool]:
    """
    Donat un natural m >= 2, retorna una llista ps de m+1 booleans
    tal que ps[i] indica si i és primer o no.
    """

    ps = [True for _ in range(m + 1)]
    ps[0] = ps[1] = False
    i = 2
    while i * i <= m:
        if ps[i]:
            for j in range(i * i, m + 1, i):
                ps[j] = False
        i += 1
    return ps


print(len(llista_primers(1000000)))
