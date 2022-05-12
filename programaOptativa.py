# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 22:02:43 2022

@author: luis_
"""

"""
Autor: La venganza (Moreno Olmos Luis Miguel)

El programa consiste en leer dos documentos de texto .txt
Cada documento debe tener tres parrafos como minimo
Debe mostrar cuantas lineas con texto y cuantas lineas vacias tiene cada doc
Eliminar los simbolos de puntuacion
Muestre las palabras que contiene cada documento de manera ordenada.
Muestre cuantas palabras tiene cada documento
Que una los documentos en uno nuevo.
Que elimine los simbolos de puntuacion
Que muestre todas las palabras que contiene el documento nuevo de manera ordenada
Que muestre cuantas palabras tiene el doc
Que escriba una palabra e indique si existe o no

"""
  
from tkinter import *
import os 

main = Tk()
main.title("Procesamiento de Lenguage Natrual")
main.resizable(True,True)
main.iconbitmap("xd.ico")
miFrame = Frame(main, width=1200, height=1800)
miFrame.pack()



nombreCarpeta="C:\\Users\\luis_\\OneDrive\\Documentos\\hola\\"

archivoSalida="fuuuusion.txt"

texto_junto = ""

simbolos = [",","(",")",".",";",":","\""]

archivosLista = os.listdir(nombreCarpeta)
cont=0
cont2=0
for nombreArchivo in archivosLista:
    with open(nombreCarpeta+nombreArchivo,"r") as archivo:
        lineas_lista = archivo.readlines()
    num_linea = 1
    num_texto = 0
    num_vacio = 0
    for linea in lineas_lista:
        if linea.strip() == "":
            num_linea = num_linea + 1
            num_vacio = num_vacio+1
        else: 
            num_linea = num_linea+1
            num_texto = num_texto+1
    lineas = Label(miFrame, text=f'EL ARCHIVO "{nombreArchivo}"  TIENE , {num_linea}, lINEAS')
    lineas.grid(row=cont,column=0)
    cont = cont+1
    cont2 = cont2+1
    lineasConTexto = Label(miFrame, text=f'EL ARCHIVO "{nombreArchivo}"  TIENE , {num_texto}, lINEAS CON TEXTO')
    lineasConTexto.grid(row=cont,column=0)
    cont = cont+1
    cont2 = cont2+1
    lineasVacias = Label(miFrame, text=f'EL ARCHIVO "{nombreArchivo}"  TIENE , {num_vacio}, lINEAS VACIAS\n\n')
    lineasVacias.grid(row=cont,column=0)
    cont = cont+1
    cont2 = cont2+1
cont=0
cont2=1    
for nombreArchivo in archivosLista:
    cont=0
    aviso1 = Label(miFrame, text=f"\n ARCHIVO {nombreArchivo}")
    aviso1.grid(row=cont,column=cont2)
    cont = cont+1
    
    with open(nombreCarpeta+nombreArchivo,"r") as archivo:
        texto = archivo.read()
    for simbolo in simbolos:
        texto = texto.replace(simbolo, " ")
    texto_junto = texto_junto + texto + "\n"
    palabras_lista = texto.split()
    palabras_lista.sort()
    
    aviso2 = Label(miFrame, text=f"TIENE {len(palabras_lista)} PALABRAS.")
    aviso2.grid(row=cont,column=cont2)
    cont = cont+1
    funListaFinal= lambda palabras_lista, x: [palabras_lista[i:i+x] for i in range(0, len(palabras_lista), x)]
    ListaFinal=funListaFinal(palabras_lista, 5)
    for lista in ListaFinal:
        aviso4 = Label(miFrame, text=f"{lista} +")
        aviso4.grid(row=cont,column=cont2)
        cont = cont+1
    cont2 = cont2+1
        
with open(nombreCarpeta+archivoSalida,"w") as salida:
    salida.write(texto_junto)

with open(nombreCarpeta+archivoSalida,"r") as archivo:
    texto = archivo.read()

cont=0
aviso5 = Label(miFrame, text=f"\n ARCHIVO {archivoSalida}")
aviso5.grid(row=cont,column=3)
cont=cont+1
palabras_lista2 = texto.split()
palabras_lista2.sort()

aviso6 = Label(miFrame, text=f"\n TIENE {len(palabras_lista2)} PALABRAS")
aviso6.grid(row=cont,column=3)
cont=cont+1

ListaFinal2=funListaFinal(palabras_lista2, 5)
for lista in ListaFinal2:

    aviso7 = Label(miFrame, text=f"{lista} +")
    aviso7.grid(row=cont,column=3)
    cont = cont+1
    
with open(nombreCarpeta+archivoSalida,"r") as archivo:
    lineas_lista = archivo.readlines()



aviso8 = Label(miFrame, text=f"Palabra a bsucar en el documento ༼ つ ◕_◕ ༽つ: ")
aviso8.grid(row=18,column=0)
palabra = StringVar()
palab = Entry(miFrame, textvariable=palabra)
palab.grid(row=18,column=1)

msj = Label(miFrame)
msj.grid(row=20,column=1)
mostrar=Button(miFrame, text="Buscar", command=Mostrar)
mostrar.grid(row=18,column=2)
palabraLabel= palabra.get()
num_palabras=0
 

def Mostrar():
    mensaje=palabra.get()
    nombreCarpeta="C:\\Users\\luis_\\OneDrive\\Documentos\\hola\\"
    archivoSalida="fuuuusion.txt"
    with open(nombreCarpeta+archivoSalida,"r") as archivo:            
        contents2 = archivo.read()
    words= contents2.split()
    nPalabra = str(mensaje)
    aviso9 = Label(miFrame, text=f"LA PALABRA {mensaje} SE ENCUENTRA {words.count(nPalabra)} VECES EN EL DOCUMENTO (❁´◡`❁)")
    aviso9.grid(row=23,column=0)

main.mainloop()