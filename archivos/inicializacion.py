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

    #CREACION DE BLOQUES (escalera = 619)

    bloque = Ladrillo(350, 450, True)
    bloque = Signo(450, 450)
    escalera = Escalera(700,620, True)
    escalera = Escalera(776,620, False)
    escalera = Escalera(776,545, False)
    escalera = Escalera(852,620, True)
    escalera = Escalera(852,545, True)
    escalera = Escalera(852,469, True)


    #TERMINA CREACION DE BLOQUES

    #CREACION DE MONEDAS

    moneda = Moneda(190, 350, False)

    #TERMINA CREACION DE MONEDAS