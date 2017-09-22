from clases import *

# Separacion entre bloques de piso: 72

def inicializacion():

    # CREACION DE PISO

    x = 0

    for i in range(57):
        piso = Piso(x,695,"imagenes/piso_bloque.png")
        x += 72

    x = 4320

    for i in range(17):
        piso = Piso(x,695,"imagenes/piso_bloque.png")
        x += 72

    x = 5760

    for i in range(6):
        piso = Piso(x,695,"imagenes/piso_bloque.png")
        x += 72

    #TERMINA CREACION DE PISO

    #CREACION DE BLOQUES

    bloque = Bloque(50,450)
    bloque = Bloque(1000,450)
    bloque = Bloque(1600,450)