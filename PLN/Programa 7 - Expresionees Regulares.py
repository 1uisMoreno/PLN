"""
Created on Wed Mar 30 22:02:43 2022

@author: luis_
"""

from distutils import archive_util
import re

carpeta_nombre = "C:\\Users\\luis_\\OneDrive\\Documentos\\PLN\\"
archivo_nombre = "texto1.txt"

with open(carpeta_nombre+archivo_nombre,"r",encoding="utf8") as archivo:
    texto = archivo.read()

expresion_regular = re.compile(r"cliente")

resultados_busqueda = expresion_regular.finditer(texto)

for resultado in resultados_busqueda:
    print(resultado.group(0))

expresion_regular = re.compile(r"se+")

resultados_busqueda = expresion_regular.finditer(texto)

for resultado in resultados_busqueda:
    print(resultado.group(0))