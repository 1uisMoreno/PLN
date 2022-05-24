"""
Created on Wed Mar 30 22:02:43 2022

@author: luis_
"""
carpeta_nombre = "C:\\Users\\luis_\\OneDrive\\Documentos\\PLN\\"
archivo_nombre = "texto1.txt"

palabra = input("Escribe la palabra a buscar en el documento: ")

with open(carpeta_nombre+archivo_nombre,"r",encoding="utf8") as archivo:
    texto = archivo.read()

if palabra in texto:
    print("La palabra ", palabra, " fue encontrada en el texto.")
else:
    print("La palabra ", palabra, " no fue encontrada en el texto.")