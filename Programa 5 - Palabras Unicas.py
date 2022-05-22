"""
Created on Wed Mar 30 22:02:43 2022

@author: luis_
"""

carpeta_nombre = "C:\\Users\\luis_\\OneDrive\\Documentos\\PLN\\"
archivo_nombre = "texto1.txt"

with open(carpeta_nombre+archivo_nombre,"r",encoding="utf8") as archivo:
    texto = archivo.read()

simbolos=["(",")",",",".",";",":","\""]

for simbolo in simbolos:
    texto=texto.replace(simbolo," "+simbolo+" ")

palabras_lista=texto.split()

palabras_unicas=[]

for palabra in palabras_lista:
    if palabra in palabras_unicas:
        continue
    palabras_unicas.append(palabra)

print(palabras_unicas)
num=len(palabras_unicas)
print("Numero de palabras en el documento: ", num)
print("Numero de palabras en todo el documento: ", len(palabras_lista))