# programa que pinta un poligon regular amb cert nombre de costats

import turtle 

mida = 100
costats = 8

i = 1
while i <= costats:
    turtle.forward(mida)
    turtle.right(360 / costats)
    i = i + 1 

turtle.done()
