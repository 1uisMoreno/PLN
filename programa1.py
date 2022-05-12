# -*- coding: utf-8 -*-
"""
Created on Thu May 12 12:26:29 2022

@author: luis_
"""

import nltk
import matplotlib

print("Moreno Olmos Luis Miguel")

carpeta_nombre = "C:\\Users\\luis_\\OneDrive\\Documentos\\PLN\\"
archivo_nombre = "texto1.txt"

with open(carpeta_nombre+archivo_nombre,"r", encoding="utf8") as archivo:
    texto = archivo.read()

print("----------------------------------------------------")

palabras_funcionales = nltk.corpus.stopwords.words("spanish")

for palabras_funcional in palabras_funcionales:
    print(palabras_funcional)

print("----------------------------------------------------")

tokens = nltk.word_tokenize(texto, "spanish")
tokens_limpios = []

for token in tokens:
    if token not in palabras_funcionales:
        tokens_limpios.append(token)

print(tokens_limpios)
print(len(tokens))
print(len(tokens_limpios))

texto_limpio_nltk = nltk.Text(tokens_limpios)

distribucion_limpia = nltk.FreqDist(texto_limpio_nltk)

distribucion_limpia.plot(40, cumulative=False)
