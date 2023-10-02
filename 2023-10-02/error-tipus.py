"""
Programa amb un error de tipus. 
    1. Proveu-lo. 
    2. Busqueu els errors amb mypy
    3. Busqueu els errors amb Visual Studio Code
       (vegeu com configurar-lo a https://lliçons.jutge.org/ip-python/tipus/comprovacio.html)
"""


import yogi

n = yogi.read(int)
if n == 666:
    print(2 + 'tres')
    
