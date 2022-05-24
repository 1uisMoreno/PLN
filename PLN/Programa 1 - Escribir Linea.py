"""
Created on Wed Mar 30 22:02:43 2022

@author: luis_
"""


print("Hola MUNDO")
print("Ingenieria en Computo Inteligente")

suma = 103+164

resultado = suma/2

print("resultado = ",resultado)

carpeta_nombre = "C:\\Users\\luis_\\OneDrive\\Documentos\\PLN\\texto1.txt"
archivo_nombre = "texto1.txt"

archivo=open("C:\\Users\\luis_\\OneDrive\\Documentos\\PLN\\texto1.txt")
print(archivo.read())

archivo2=open("C:\\Users\\luis_\\OneDrive\\Documentos\\PLN\\texto1.txt","w+")
archivo2.write("Gabito es chapilin, Dali es el matadito el salon y Hector, pues hector ahi hace la lucha pa no olvidar que necesita respirar")

archivo2=open("C:\\Users\\luis_\\OneDrive\\Documentos\\PLN\\texto1.txt"")
print(archivo2.read())

archivo.close()
archivo2.close()