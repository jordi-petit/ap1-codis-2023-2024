# programa que converteix n segons en hores, minuts i segons

# llegir dades entrada
n = int(input('nombre de segons: '))

# calcular el resultat 
h = n // 3600
m = (n % 3600) // 60
s = n % 60

# escriure les dades de sortida
print(h, m, s)