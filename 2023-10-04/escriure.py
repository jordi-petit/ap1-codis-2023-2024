def escriu(n: int, t: str) -> None:
    """Escriu el text t n cops, prec: n >= 0."""

    if n == 0:
        pass
    elif n == 1:
        print(t)
    else:
        escriu(n//2, t)
        escriu(n - n//2, t)        



escriu(8, '*')