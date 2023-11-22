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


print(fusio([10, 20, 30, 30, 40], [5, 10, 15, 30, 35, 50, 60, 70, 80]))
