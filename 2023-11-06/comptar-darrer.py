"""Diu quants cops apareix la darrera paraula en una seqüència de paraules."""


import yogi


def llegir_paraules() -> list[str]:
    """Retorna la llista de paraules a l'entrada."""
    
    paraules: list[str] = []
    for paraula in yogi.tokens(str):
        paraules.append(paraula)
    return paraules

    # versió extra curta per a frikis:
    return list(yogi.tokens(str))


def ocurrencies(trobar: str, paraules: list[str]) -> int:
    """Retorna quants cops apareix la paraula trobar a la llista paraules."""

    c = 0
    for paraula in paraules:
        if paraula == trobar:
            c += 1 
    return c 


def main() -> None:
    paraules = llegir_paraules()
    if paraules == []:
        print(0)
    else:
        print(ocurrencies(paraules[-1], paraules))


if __name__ == '__main__':
    main()