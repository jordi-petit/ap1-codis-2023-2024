"""
Demostració 2 d'streamlit: crea una pàgina web que passa un frase a majúscules/minúscules.
"""


import streamlit

streamlit.title("Títol")

frase = streamlit.text_input("Escriu una frase")

opcions = streamlit.radio("Transforma a:", ["Majúscules", "Minúscules"])

boto = streamlit.button("Transforma", type="primary")

if boto:
    if opcions == "Majúscules":
        resultat = frase.upper()
    else:
        resultat = frase.lower()

    streamlit.write("Aquí ho tens:")
    streamlit.header(resultat)
