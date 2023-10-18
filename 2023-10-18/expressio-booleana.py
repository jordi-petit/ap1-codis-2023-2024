"""Problema P42181 però amb espais entre els elements."""

from yogi import read


def avalua() -> bool:
    """Avalua retorna el resultat d'avaluar una expressió llegida de l'entrada."""

    primer = read(str)
    if primer == '0':
        return False 
    if primer == '1':
        return True 
    if primer == '!':
        return not avalua()
    assert primer == '('
    r1 = avalua()
    op = read(str)
    r2 = avalua()
    darrer = read(str)
    assert darrer == ')'
    if op == '+':
        return r1 or r2 
    if op == '*':
        return r1 and r2 
    assert False
        



def main() -> None:
    if avalua():
        print(1)
    else:
        print(0)


main()