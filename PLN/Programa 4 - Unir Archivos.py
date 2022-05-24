"""
Created on Wed Mar 30 22:02:43 2022

@author: luis_
"""
import os

carpeta_nombre = "C:\\Users\\luis_\\OneDrive\\Documentos\\PLN\\"

carpeta_salida = "C:\\Users\\luis_\\OneDrive\\Documentos\\PLN\\"

archivo_nombre = "texto1.txt"

archivo_lista=os.listdir(carpeta_nombre)

union=""

for archivo_nombre in archivo_lista:
    archivo=open(carpeta_nombre+archivo_nombre,encoding="utf8")
    union+=archivo.read()+"\n"
    archivo.close()

with open(carpeta_salida+archivo_salida,"w") as salida:
    salida.write(union)