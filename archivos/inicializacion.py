from clases import *
from clases.control.Corazon import Corazon

# Separacion entre bloques de piso: 72

def inicializacion(mario):

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

    for i in range(52):
        piso = Piso(x,695)
        x += 72

    x = 9720

    for i in range(6):
        piso = Piso(x,695)
        x += 72

    #TERMINA CREACION DE PISO

    #CREACION DE BLOQUES (escalera = 620, 76 de diferencia entre escaleras)

    ladri = Ladrillo(1100, 300, True)

    #TERMINA CREACION DE BLOQUES

    #CREACION DE MONEDAS
    #TERMINA CREACION DE MONEDAS

    tuberia = Tuberia(1250, 3)

    escalera = Escalera(300,620, True)

    mario.inicializar_vidas()