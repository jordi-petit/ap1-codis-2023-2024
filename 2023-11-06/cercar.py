
def hies_a(patro: str, text: str, i: int) -> bool:
    """Diu si el patró es troba al text començant a la posició i."""

    m = len(patro)
    for j in range(m):
        if text[j + i] != patro[j]:
            return False 
    return True


def hies(patro: str, text: str) -> bool:
    """Diu si el patró es troba al text."""

    m = len(patro)
    n = len(text)
    for i in range(n - m):
        if hies_a(patro, text, i):
            return True 
    return False
