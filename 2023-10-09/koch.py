"""Dibuixa el floc de Koch"""


from yogi import *
from turtle import *


def corba_koch(m: float, n: int) -> None:
    if n == 0:
        forward(m)
    else:
        corba_koch(m / 3, n - 1)
        left(60)
        corba_koch(m / 3, n - 1)
        right(120)
        corba_koch(m / 3, n - 1)
        left(60)
        corba_koch(m / 3, n - 1)


def floc_koch(m: float, n: int) -> None:
    for _ in range(3):
        corba_koch(m, n)
        right(120)


def main() -> None:
    hideturtle()
    m = read(float)
    n = read(int)
    floc_koch(m, n)
    done()


main()