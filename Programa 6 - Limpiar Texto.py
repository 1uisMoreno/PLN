"""
Created on Wed Mar 30 22:02:43 2022

@author: luis_
"""

import os

carpeta_nombre = "C:\\Users\\luis_\\OneDrive\\Documentos\\PLN\\"

simbolos = ["(",")",",",".",";",":","\""]
archivos_lista=os.listdir(carpeta_nombre)
for archivos_nombre in archivos_lista:
    archivo = open(carpeta_nombre+archivos_nombre,encoding="utf8")
    lineas_lista = archivo.readlines()
    archivo.close()
    longitud = len(lineas_lista)
    print("El archivo", archivos_nombre, " TIENE ", longitud, "lineas")


    archivo = open(carpeta_nombre+archivos_nombre)
    texto = archivo.read()
    archivo.close()
    for simbolo in simbolos:
        texto = texto.replace(simbolo, " " + simbolo + " ")
    
    palabras_lista = texto.split()
    palabras_lista.sort()
    for palabras in palabras_lista:
        print(palabras)
    
