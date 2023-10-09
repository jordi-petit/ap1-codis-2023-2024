"""Programa que escriu un nombre en alguna base."""

from yogi import read 

def escriure(n: int, b: int) -> None:
    """Escriu n en base b. Precondicions: n >= 0 i 2 <= b <= 10."""

    if n < b:
        print(n, end='')
    else:
        escriure(n // b, b)
        print(n % b, end='')


def main() -> None:
    n, b = read(int), read(int)
    escriure(n, b)
    print() 


main()