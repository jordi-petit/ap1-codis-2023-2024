"""Resolució de Sudokus"""


from dataclasses import dataclass
from typing import Optional, TypeAlias
from yogi import read


Usats: TypeAlias = list[list[bool]]


@dataclass
class Sudoku:
    graella: list[list[Optional[int]]]
    files: Usats
    columnes: Usats
    caixes: Usats


def llegir() -> Sudoku:
    """Llegeix un sudoku i el retorna."""

    s = buit()
    for i in range(9):
        for j in range(9):
            v = read(str)
            if v != ".":
                marcar_casella(s, i, j, int(v))
    return s


def escriure(s: Sudoku) -> None:
    """Escriu un sudoku."""

    for i in range(9):
        for j in range(9):
            if s.graella[i][j] is None:
                print(".", end=" ")
            else:
                print(s.graella[i][j], end=" ")
        print()
    print()


def crear(text: str) -> Sudoku:
    """Crea i retorna un sudoku a partir d'un text."""

    files = text.split("\n")
    taula = [fila.split() for fila in files]
    s = buit()
    for i in range(9):
        for j in range(9):
            v = taula[i][j]
            if v != ".":
                marcar_casella(s, i, j, int(v))
    return s


def resultat(s: Sudoku) -> str:
    """Retorna el text corresponent a un sudoku."""

    text = ""
    for i in range(9):
        for j in range(9):
            if s.graella[i][j] is None:
                text += "."
            else:
                text += str(s.graella[i][j])
            if j != 8:  # separador
                text += " "
        text += "\n"
    return text


def buit() -> Sudoku:
    """Retorna un sudoku buit."""

    # a les marques, la posició 0 no s'utilitza perquè els valors van de 1 a 9, d'aquí les 10 posicions.

    graella: list[list[Optional[int]]] = [[None for _ in range(9)] for _ in range(9)]
    files = [[False for _ in range(10)] for _ in range(9)]
    columnes = [[False for _ in range(10)] for _ in range(9)]
    caixes = [[False for _ in range(10)] for _ in range(9)]
    return Sudoku(graella, files, columnes, caixes)


def marcar_casella(s: Sudoku, i: int, j: int, v: int):
    """Marca que la casella (i,j) del sudoku s té el valor v."""

    s.graella[i][j] = v
    s.files[i][v] = True
    s.columnes[j][v] = True
    s.caixes[caixa(i, j)][v] = True


def desmarcar_casella(s: Sudoku, i: int, j: int, v: int):
    """Marca que la casella (i,j) del sudoku s ja no té el valor v."""

    s.graella[i][j] = None
    s.files[i][v] = False
    s.columnes[j][v] = False
    s.caixes[caixa(i, j)][v] = False


def caixa(i: int, j: int) -> int:
    """Retorna el número de caixa de la casella (i,j)."""

    return 3 * (i // 3) + j // 3


def seguent(i: int, j: int) -> tuple[int, int]:
    """Retorna la casella que ve després de la (i,j) per columnes i per files."""
    si = i
    sj = j + 1
    if sj == 9:
        si, sj = si + 1, 0
    return si, sj


def resol_rec(s: Sudoku, i: int, j: int) -> bool:
    """Resol el sudoku a partir de la casella (i,j)."""

    if i == 9:
        return True

    si, sj = seguent(i, j)

    if s.graella[i][j] is not None:
        return resol_rec(s, si, sj)
    else:
        for v in range(1, 10):
            if legal(s, i, j, v):
                marcar_casella(s, i, j, v)
                if resol_rec(s, si, sj):
                    return True
                desmarcar_casella(s, i, j, v)
        return False


def legal(s: Sudoku, i: int, j: int, v: int) -> bool:
    """Indica si és legal marcar la casella (i,j) del sudoku s amb le valor v."""

    return not s.files[i][v] and not s.columnes[j][v] and not s.caixes[caixa(i, j)][v]


def resol(s: Sudoku) -> bool:
    """
    Resol un sudoku.

    Si té solució, s esdevé la solució i retorna True.
    Si no en té, retorna False.
    """

    return resol_rec(s, 0, 0)


def main() -> None:
    """Programa principal."""

    s: Sudoku = llegir()
    if resol(s):
        escriure(s)
    else:
        print("Sense solució")


if __name__ == "__main__":
    main()
