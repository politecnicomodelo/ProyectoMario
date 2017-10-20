from clases import *
from clases.control.Corazon import Corazon
from clases.control.Letra import Letra

def inicializacion(mario):

    x = 0

    for i in range(35):
        piso = Piso(x,695)
        x += 72

    x = 3100

    for i in range(35):
        piso = Piso(x,695)
        x += 72

    mario.inicializar_vidas()
    e = Escalera(800,620,False)
    e = Escalera(875,545,True)
    e = Escalera(875,620,True)
    e = Escalera(950,470,False)
    e = Escalera(950,545,False)
    e = Escalera(950,620,False)

    #LETRAS

    P = Letra(400, 300, "imagenes/letras/P.png")
    A = Letra(500, 300, "imagenes/letras/A.png")
    U = Letra(600, 300, "imagenes/letras/U.png")
    S = Letra(700, 300, "imagenes/letras/S.png")
    A = Letra(800, 300, "imagenes/letras/A.png")