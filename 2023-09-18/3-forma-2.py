# programa que pinta un poligon regular amb cert nombre de costats molts cops, rotant-lo cada cop

import turtle 

mida = 100
costats = 8
cops = 10
angle1 = 360 / costats
angle2 = 360 / cops

j = 1 
while j <= cops:
    i = 1
    while i <= costats:
        turtle.forward(mida)
        turtle.right(angle1)
        i = i + 1 
    j = j + 1 
    turtle.right(angle2)

turtle.done()
