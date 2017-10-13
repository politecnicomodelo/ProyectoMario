from clases import *
from clases.control.Corazon import Corazon

# Separacion entre bloques de piso: 72

def inicializacion(mario):

    # CREACION DE PISO

    x = 0

    for i in range(15):
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