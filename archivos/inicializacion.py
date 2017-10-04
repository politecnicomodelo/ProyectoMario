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

    #CREACION DE BLOQUES (escalera = 620, 76 de diferencia entre escaleras)

    bloque = Ladrillo(350, 450, True)
    bloque = Signo(428, 450)
    bloque = Ladrillo(504, 450, True)
    bloque = Ladrillo(580, 450, False)
    bloque = Ladrillo(700, 250, True)

    escalera = Escalera(765,620, True)
    escalera = Escalera(842,620, False)
    escalera = Escalera(842,545, False)
    escalera = Escalera(919,620, True)
    escalera = Escalera(919,545, True)
    escalera = Escalera(919,469, True)
    escalera = Escalera(996,620, False)
    escalera = Escalera(996,545, False)
    escalera = Escalera(996,469, False)
    escalera = Escalera(996,393, False)

    #TERMINA CREACION DE BLOQUES

    #CREACION DE MONEDAS

    moneda = Moneda(190, 350, False)

    #TERMINA CREACION DE MONEDAS

    tuberia = Tuberia(1600, 3)