"""Dibuixa un arbre fractal"""


from yogi import *
from turtle import *

def arbre(m: float, n: int, a: float) -> None:
    if n > 0:
        forward(m)
        left(a / 2)
        arbre(m * 3 / 4, n - 1, a)
        right(a)
        arbre(m * 3 / 4, n - 1, a)
        left(a/2)
        backward(m)


def main() -> None:
    m = read(float)
    n = read(int)
    a = read(float)
    left(90)
    arbre(m, n, a)
    done()


main()