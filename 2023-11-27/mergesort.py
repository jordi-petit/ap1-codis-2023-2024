
import time
import random
from typing import TypeVar

T = TypeVar('T')


def fusio(l1: list[T], l2: list[T]) -> list[T]:
    """
    Donades dues llistes ordenades, retorna la seva fusió 
    (és a dir, una llista ordenada amb tots els elements de les
    dues d'entrada).
    """

    r: list[T] = []
    i, j = 0, 0
    n1, n2 = len(l1), len(l2)
    while i < n1 and j < n2:
        if l1[i] <= l2[j]:
            r.append(l1[i])
            i += 1
        else:
            r.append(l2[j])
            j += 1
    r.extend(l1[i:])
    r.extend(l2[j:])
    return r


def mergesort0(L: list[T]) -> list[T]:
    """Donada una llista, retorna una altra llista amb els seus elements ordenats."""
    if len(L) <= 1:
        return L
    else:
        m = len(L) // 2
        return fusio(mergesort0(L[:m+1]), mergesort0(L[m+1:]))


def mergesort(L: list[T]) -> None:
    """Ordena la llista L."""

    mergesortR(L, 0, len(L) - 1)


def mergesortR(L: list[T], e: int, d: int) -> None:
    """Ordena la llista L entre les posicions e i d (incloses)"""

    if d - e >= 1:
        m = (e + d) // 2
        mergesortR(L, e, m)
        mergesortR(L, m + 1, d)
        merge(L, e, m, d)


def merge(L: list[T], e: int, m: int, d: int) -> None:
    """
    Fusiona els elements de L[e..m] i els de L[m+1..d].
    Prec: L[e..m] està ordenada i L[m+1..d] està ordenada,
    """

    R: list[T] = []
    i1 = e
    i2 = m + 1
    while i1 <= m and i2 <= d:
        if L[i1] < L[i2]:
            R.append(L[i1])
            i1 += 1
        else:
            R.append(L[i2])
            i2 += 1
    R.extend(L[i1:m + 1])
    R.extend(L[i2:d + 1])

    L[e:d + 1] = R


def main() -> None:
    """Mesures de temps per llistes amb elements a l'atzar."""

    for n in range(10000, 2000000, 10000):
        v = [random.randint(0, n) for i in range(n)]
        t1 = time.time()
        v.sort()
        t2 = time.time()
        print(n, t2 - t1)


main()
