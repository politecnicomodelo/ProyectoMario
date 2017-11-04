from clases import *
from clases.control.Corazon import Corazon
from clases.control.Letra import Letra

def inicializacion(mario):

    x = 0

    for i in range(71):
        piso = Piso(x,695)
        x += 72

    x = 5264

    for i in range(16):
        piso = Piso(x,695)
        x += 72

    x = 6580

    for i in range(17):
        piso = Piso(x, 695)
        x += 72

    x = 6811

    for i in range(51):
        piso = Piso(x, 695)
        x += 72

    x = 10699

    for i in range(40):
        piso = Piso(x, 695)
        x += 72

    mario.inicializar_vidas()

    #LETRAS

    P = Letra(400, 300, "imagenes/letras/P.png")
    A = Letra(500, 300, "imagenes/letras/A.png")
    U = Letra(600, 300, "imagenes/letras/U.png")
    S = Letra(700, 300, "imagenes/letras/S.png")
    A = Letra(800, 300, "imagenes/letras/A.png")
