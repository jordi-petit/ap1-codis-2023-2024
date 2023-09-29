"""
Programa amb diferentes accions per pintar objectes 
amb la tortuga.
"""


from yogi import *
from turtle import *


def pintar_poligon_regular(mida: int, costats: int) -> None:
    """Pinta un poligon regular de costats costats de mida mida a la posició actual de la tortuga."""

    for _ in range(costats):
        forward(mida)
        right(360 / costats)


def pintar_quadrat(mida: int) -> None:
    """Pinta un quadrat amb costats de mida mida a la posició actual de la tortuga."""

    pintar_poligon_regular(mida, 4)


def pintar_molts_quadrats_rotats(mida: int, quants: int) -> None:
    """Pinta quants quadrats de mida mida rotats al voltant de la posició actual de la tortuga."""

    for _ in range(quants):
        pintar_quadrat(mida)
        right(360 / quants)


def main() -> None:
    """Programa principal"""
    mida = read(int)
    nombre = read(int)
    pintar_molts_quadrats_rotats(mida,nombre)
    done()


# cridar al programa principal si s'executa com a programa
if __name__ == '__main__':
    main()

