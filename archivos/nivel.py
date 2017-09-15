from clases.control.Controlador import *
from archivos.dibujo import *
from archivos.procesos import *


def nivel(reloj, mario, ventana, colores, fondo):

    FPS = 120

    frames_totales = 0

    estatico = [False, 3]

    segundo = 0

    while True:

        procesos(reloj, mario, FPS, segundo, estatico)

        if frames_totales % (FPS / 4) == 0:

            segundo += 0.25

            print(estatico[0])

            if estatico[0] is True:
                estatico[0] = False

        dibujo(fondo, ventana, colores)

        frames_totales += 1