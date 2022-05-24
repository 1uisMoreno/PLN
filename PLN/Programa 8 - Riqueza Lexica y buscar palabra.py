"""
Created on Wed Mar 30 22:02:43 2022

@author: luis_
"""

from tkinter import simpledialog
import nltk

carpeta_nombre = "C:\\Users\\luis_\\OneDrive\\Documentos\\PLN\\"
archivo_nombre = "texto1.txt"

with open(carpeta_nombre+archivo_nombre,"r",encoding="utf8") as archivo:
    texto = archivo.read()

tokens = nltk.word_tokenize(texto, "spanish")

for token in tokens:
    print(token)

palabras_totales = len(tokens)
print("Palabras totales: ", palabras_totales)

tokens_conjunto = set(tokens)
palabras_diferentes = len(tokens_conjunto)
print("Palabras diferentes: ", palabras_diferentes)

riqueza_lexica = palabras_diferentes/palabras_totales
print("Riqueza lexica: ", riqueza_lexica)

riqueza_lexica_por = 100 * riqueza_lexica
print("Riqueza lexica porcentaje: ", riqueza_lexica_por,"%")

texto_nltk = nltk.Text(tokens)
palabra = input("Escribe la palabra a buscar en el documento: ")

texto_nltk.concordance(palabra)

print("-------------------------------------------------------------------")

texto_nltk.similar(palabra)

print("-------------------------------------------------------------------")

conteo_individual = tokens.count(palabra)
print("Numero de veces que se encuentra la palabra en el texto: ", conteo_individual)
