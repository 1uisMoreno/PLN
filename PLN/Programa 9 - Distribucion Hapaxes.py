"""
Created on Wed Mar 30 22:02:43 2022

@author: luis_
"""
from tkinter import simpledialog
import nltk
import matplotlib

carpeta_nombre = "C:\\Users\\luis_\\OneDrive\\Documentos\\PLN\\"
archivo_nombre = "texto1.txt"

with open(carpeta_nombre+archivo_nombre,"r",encoding="utf8") as archivo:
    texto = archivo.read()

tokens = nltk.word_tokenize(texto, "spanish")

for token in tokens:
    print(token)

palabras_totales = len(tokens)
print("Palabras totales: ", palabras_totales)

print("---------------------------------------------------")

texto_nltk = nltk.Text(tokens)
distribucion = nltk.FreqDist(texto)

distribucion.plot()

print("---------------------------------------------------")

hapaxes = distribucion.hapaxes()

for hapax in hapaxes:
    print(hapax)
