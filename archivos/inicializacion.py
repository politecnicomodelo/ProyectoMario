from clases import *
from clases.control.Corazon import Corazon
from clases.control.Letra import Letra

def inicializacion(mario):

    x = 0

    for i in range(35):
        piso = Piso(x,695)
        x += 72

    x = 500

    for i in range(35):
        piso = Piso(x,695)
        x += 72

    mario.inicializar_vidas()
    s = Signo(500,400)
    m = Moneda(550, 200, False)
    m = Moneda(600, 600, False)
    m = Moneda(800, 600, False)
    m = Moneda(1000, 600, False)
    m = Moneda(1200, 600, False)
    m = Moneda(1400, 600, False)
    m = Moneda(1600, 600, False)
    m = Moneda(1800, 600, False)
    m = Moneda(2000, 600, False)
    m = Moneda(2200, 600, False)
    m = Moneda(2400, 600, False)

    #LETRAS

    P = Letra(400, 300, "imagenes/letras/P.png")
    A = Letra(500, 300, "imagenes/letras/A.png")
    U = Letra(600, 300, "imagenes/letras/U.png")
    S = Letra(700, 300, "imagenes/letras/S.png")
    A = Letra(800, 300, "imagenes/letras/A.png")