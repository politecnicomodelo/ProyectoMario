from clases import *
from clases.control.Corazon import Corazon

# Separacion entre bloques de piso: 72

def inicializacion(mario):

    # CREACION DE PISO

    x = 0

    for i in range(20):
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
    mario.inicializar_vidas()

'''
    l = Ladrillo(500, 450, False)
    l = Ladrillo(580, 450, True)
    s = Signo(660, 450)
    s = Signo(820, 450)
    l = Ladrillo(740, 450, True)
    m = Moneda(650, 300, False)
    t = Tuberia(1000, 2)
    t = Tuberia(1600, 3)
    g = Goomba(1300, 630)
    m = Mastil(2000)
    e = Escalera(2300, 620, False)
    e = Escalera(2375, 620, True)
    e = Escalera(2375, 545, True)
'''