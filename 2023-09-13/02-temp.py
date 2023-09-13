# ús del elif ("else if")

t = int(input())

if t > 0:
    missatge = 'positiva'
elif t < 0:
    missatge = 'negativa'
else:
    missatge = 'zero'

print(missatge)
