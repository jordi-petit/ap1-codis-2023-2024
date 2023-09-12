# programa que pinta una estrella (no gaire bé, arregleu-lo!)

import turtle

amp = 200
puntes = 11
angle = 360 / puntes

for i in range(puntes):
    turtle.forward(amp)
    turtle.right(angle * 2)

turtle.done()