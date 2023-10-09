"""Resol el problema de les torres de Hanoi"""


import yogi 

def hanoi(d: int, ini: str, aux: str, dst: str) -> None:
    if d > 0:
        hanoi(d - 1, ini, dst, aux)
        print(ini, '->', dst)
        hanoi(d - 1, aux, ini, dst)


def main() -> None:
    d = yogi.read(int)
    hanoi(d, 'a', 'b', 'c')


main()