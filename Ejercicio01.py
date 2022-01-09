#
# Ejercicio 1
#
#
# Enunciado: Imprime todos los ficheros existentes en tu carpeta de Descargas.


# ESTE EJERCICIO NO LO CORRIJAS AÚN, POR FAVOR, QUE ME SIGUE DANDO ERROR :-S
import os
from os import listdir
from os.path import isfile, join

directorio= r"/Usuarios/Javier/Descargas/"
isFile = os.path.isfile(directorio)
archivos = os.listdir(directorio)

for i in archivos:
    print(i)

    if (i in archivos == isFile):
        print(i)




# Traceback (most recent call last):
#   File "/Users/Javier/PycharmProjects/nuevo_Proyecto/Ejercicio01.py", line 13, in <module>
#     archivos = os.listdir(directorio)
# FileNotFoundError: [Errno 2] No such file or directory: '/Usuarios/Javier/Descargas/'