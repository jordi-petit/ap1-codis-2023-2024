# programa que escriu tots els divisors de n (lent)

n = 1000_000_007

i = 1
while i <= n:
    if n % i == 0:
        print(i)
    i = i + 1




