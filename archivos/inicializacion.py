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

    for i in range(6):
        piso = Piso(x,695)
        x += 72

    #TERMINA CREACION DE PISO

    #CREACION DE BLOQUES (escalera = 620, 76 de diferencia entre escaleras)

    #TERMINA CREACION DE BLOQUES

    #CREACION DE MONEDAS

    moneda = Moneda(190, 350, False)

    #TERMINA CREACION DE MONEDAS

    tuberia = Tuberia(1200, 3)

    escalera = Escalera(500, 620, True)

    goomba = Goomba(700, 630)
    goomba = Goomba(630, 630)
    goomba = Goomba(780, 630)

    ladrillo = Signo(720, 350)
    ladrillo = Ladrillo(800, 350, False)
    ladrillo = Ladrillo(640, 350, False)

    mario.inicializar_vidas()