from clases import *
from clases.control.Corazon import Corazon
from clases.control.Letra import Letra

def inicializacion(mario):

    x = 0

    for i in range(5):
        piso = Piso(x,695)
        x += 72

    x = 500

    for i in range(35):
        piso = Piso(x,695)
        x += 72

    mario.inicializar_vidas()

    # e = Escalera(600,620,False)
    # e = Escalera(675,620,True)
    # e = Escalera(675,543,True)
    # e = Escalera(750,620,False)
    # e = Escalera(750,543,False)
    # e = Escalera(750,466,False)

    #LETRAS

    P = Letra(400, 300, "imagenes/letras/P.png")
    A = Letra(500, 300, "imagenes/letras/A.png")
    U = Letra(600, 300, "imagenes/letras/U.png")
    S = Letra(700, 300, "imagenes/letras/S.png")
    A = Letra(800, 300, "imagenes/letras/A.png")