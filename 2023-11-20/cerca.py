"""
algorismes de cerca
"""


from typing import Optional, TypeVar

T = TypeVar('T')


def cerca_lineal(v: list[T], x: T) -> Optional[int]:
    """
    Retorna una posició de v que conté x o None si no hi és.
    """

    n = len(v)
    for i in range(n):
        if v[i] == x:
            return i
    return None


def cerca_binaria(v: list[T], x: T) -> Optional[int]:
    """
    Retorna una posició de v que conté x o None si no hi és.
    Precondició: v està ordenat creixentment.
    """

    n = len(v)
    e = 0
    d = n - 1
    while e <= d:
        m = (e + d) // 2
        if v[m] < x:
            e = m + 1
        elif v[m] > x:
            d = m - 1
        else:
            return m
    return None
