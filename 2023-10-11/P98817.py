from yogi import tokens

def are_primes(p: int, q: int) -> bool:
    """
    Indica si els nombres p i q són ambdós primers,
    suposant que p, q >= 2.
    """

    # es podria fer return is_prime(p) and is_prime(q) 
    # però, com diu l'observació, seria més lent. Per tant,
    # busquem els factors alhora.

    d = 2   
    while d * d <= max(p, q):
        if (d * d <= p and p % d == 0) or (d * d <= q and q % d == 0):
            return False
        d = d + 1  
    return True


def nth_twin_primes(n: int) -> tuple[int, int]:
    """
    Retorna l'n-èsim parell de nombres bessons per a n >= 1.
    """
    p = 2
    c = 0
    while c != n:
        p = p + 1 
        if are_primes(p, p + 2):
            c = c + 1 
    return p, p + 2


def main() -> None:
    for n in tokens(int):
        p, q = nth_twin_primes(n)
        print(p, q)


main()