from clases import *

# Separacion entre bloques de piso: 72

def inicializacion():

    # CREACION DE PISO

    x = 0

    for i in range(57):
        piso = Piso(x,695)
        x += 72

    x = 4320

    for i in range(17):
        piso = Piso(x,695)
        x += 72

    x = 5760

    for i in range(6):
        piso = Piso(x,695)
        x += 72

    #TERMINA CREACION DE PISO

    #CREACION DE BLOQUES

    bloque = Ladrillo(120,450, True)

    bloque = Ladrillo(190, 450, False)

    bloque = Signo(270, 450)