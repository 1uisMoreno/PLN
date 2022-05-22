# -*- coding: utf-8 -*-
"""
Created on Mon May  2 10:35:04 2022

@author: luis_
"""

import nltk

carpeta_nombre = "C:\\Users\\luis_\\OneDrive\\Documentos\\PLN\\"
archivo_nombre = "texto1.txt"

with open(carpeta_nombre+archivo_nombre,"r",encoding="utf8") as archivo:
        texto=archivo.read()

tokens=nltk.word_tokenize(texto,"spanish")

for token in tokens: 
    print(token)

"""Palabras totales"""
palabras_total=len(tokens) 
print(palabras_total)

"""Palabbras unicas"""
tokens_conjunto=set(tokens) #Set no repite elementos
palabras_totales=len(tokens) 
palabras_diferentes=len(tokens_conjunto)


"""Riqueza lexica:
La riqueza léxica es la relación que existe entre la extensión de un texto y 
el número de palabras distintas que contiene.
    """
riqueza_lexica=palabras_diferentes/palabras_totales 
print(riqueza_lexica)



"""Funcion que retorna la riqueza lexica"""
def riqueza_lexica(tokens): 
    tokens_conjunto=set(tokens) 
    palabras_totales=len(tokens) 
    palabras_diferentes=len(tokens_conjunto) 
    riqueza_lexica=palabras_diferentes/palabras_totales 
    return riqueza_lexica
    
"""
    ███████████████████████████████████████████████████████████████████████████████████████████████████████████
"""    
import nltk

def riqueza_lexica(tokens): 
    tokens_conjunto=set(tokens) 
    palabras_totales=len(tokens) 
    palabras_diferentes=len(tokens_conjunto) 
    riqueza_lexica=palabras_diferentes/palabras_totales 
    return riqueza_lexica
    
carpeta_nombre = "C:\\Users\\luis_\\OneDrive\\Documentos\\PLN\\"
archivo_nombre = "texto1.txt"

with open(carpeta_nombre+archivo_nombre,"r",encoding="utf8") as archivo:
        texto=archivo.read()

tokens=nltk.word_tokenize(texto,"spanish")
riqueza_lexica=riqueza_lexica(tokens)

print(riqueza_lexica)

conteo_individual=tokens.count("el")
print(conteo_individual)
palabras_totales=len(tokens)
porcentaje=100*conteo_individual/palabras_totales
print(porcentaje,"%")

"""
    ███████████████████████████████████████████████████████████████████████████████████████████████████████████
"""    

"""Ejercicio 15

Modificar la función que se creó para que, en lugar de 
recibir una lista de tokens, reciba texto (el texto que se lea
de un archivo, por ejemplo).


"""

"""
    ███████████████████████████████████████████████████████████████████████████████████████████████████████████
"""    


"""Ejercicio 16

Definir una función que calcule el porcentaje que ocupa una
palabra dentro de un texto. Usen como parámetros de entrada
la palabra y el texto 


"""

def porcentaje(palabra,texto):
    pass

"""
    ███████████████████████████████████████████████████████████████████████████████████████████████████████████
"""    

import nltk
import matplotlib.pyplot as plt

def riqueza_lexica(tokens): 
    tokens_conjunto=set(tokens) 
    palabras_totales=len(tokens) 
    palabras_diferentes=len(tokens_conjunto) 
    riqueza_lexica=palabras_diferentes/palabras_totales 
    return riqueza_lexica
    
carpeta_nombre = "C:\\Users\\luis_\\OneDrive\\Documentos\\PLN\\"
archivo_nombre = "texto1.txt"

with open(carpeta_nombre+archivo_nombre,"r",encoding="utf8") as archivo:
        texto=archivo.read()

tokens=nltk.word_tokenize(texto,"spanish")


texto_nltk=nltk.Text(tokens)
distribucion=nltk.FreqDist(texto_nltk)
distribucion.plot()


plt.rcParams.update({"figure.autolayout": True})
texto_nltk=nltk.Text(tokens)
distribucion=nltk.FreqDist(texto_nltk)
hapaxes=distribucion.hapaxes()
palabrasUnicas=[]
for hapax in hapaxes:
    palabrasUnicas.append(hapax)

distribucion.plot(cumulative=True)
distribucion.plot(40,cumulative=False)









