# programa que llegeix una amplada i una alçada i pinta un rectangle d'aquella mida

import turtle

amp = int(input('amplada? '))
alc = int(input('alçada? ')) 

turtle.forward(amp)
turtle.left(90)
turtle.forward(alc)
turtle.left(90)
turtle.forward(amp)
turtle.left(90)
turtle.forward(alc)
turtle.left(90)

turtle.done()