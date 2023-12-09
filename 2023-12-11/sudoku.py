"""
Pàgina web per resoldre sudokus.

instal·lar:
    $ pip3 install streamlit yogi

executar:
    $ streamlit run sudoku.py
"""


import streamlit
import solver

exemple = """. . . . . 2 3 . 7
. . . . . 6 4 5 .
1 . . 9 3 . . . .
. . . . 6 1 8 . .
. 4 8 . . . 5 6 .
. . 6 4 2 . . . .
. . . . 7 5 . . 8
. 2 9 1 . . . . .
4 . 5 6 . . . . ."""

streamlit.title("Sudoku")

streamlit.write("Solucionadar de sudokus d'AP1")

entrada = streamlit.text_area(
    label="Escriu el sudoku (segueix el format de l'exemple):",
    height=250,
    value=exemple,
)

boto = streamlit.button("Soluciona!", type="primary")

if boto:
    sudoku = solver.crear(entrada)
    if solver.resol(sudoku):
        resultat = solver.resultat(sudoku)
        streamlit.text_area(label="✨ Solució:", height=250, value=resultat)
    else:
        streamlit.write("❌ No té solució")
