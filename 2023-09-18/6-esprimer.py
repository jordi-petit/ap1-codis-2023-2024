# programa que diu si un nombre n és o no primer

n = 25

if n <= 1:
    print(n, 'no és primer')
else:
    c = 0
    d = 2 
    while d*d <= n and c == 0:
        if n % d == 0:
            c = 1
        else:
            d = d + 1 
    if c == 0:
        print(n, 'és primer')
    else:
        print(n, 'no és primer')
    
