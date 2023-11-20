
import time
import random
from typing import Optional, TypeVar

T = TypeVar('T')


def ordenacio_per_seleccio(v: list[T]) -> None:
    """Ordena la llista v."""

    n = len(v)
    i = n
    while i != 0:
        p = posicio_maxim(v, i - 1)
        v[i - 1], v[p] = v[p], v[i - 1]
        i -= 1


def posicio_maxim(v: list[T], d: int) -> int:
    """Retorna la posició de l'element més gran de v[0:d+1]."""

    p = 0
    for j in range(1, d + 1):
        if v[j] > v[p]:
            p = j
    return p


def ordenacio_per_insercio(v: list[T]) -> None:
    """Ordena la llista v."""

    n = len(v)
    for i in range(1, n):
        inserir(v, i)


def inserir(v: list[T], i: int) -> None:
    x = v[i]
    j = i
    while j > 0 and v[j - 1] > x:
        v[j] = v[j - 1]
        j -= 1
    v[j] = x


def main() -> None:
    """Mesures de temps per llistes amb elements a l'atzar."""

    for n in range(1000, 20000, 1000):
        v = [random.randint(0, n) for i in range(n)]
        t1 = time.time()
        ordenacio_per_insercio(v)
        t2 = time.time()
        print(n, t2 - t1)


main()
