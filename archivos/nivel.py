from archivos.dibujo import *
from archivos.procesos import *
from archivos.inicializacion import *


def nivel(reloj, mario, ventana, colores, fondo):

    FPS = 120

    frames_totales = 0

    segundo = 0

    inicializacion(mario)

    while True:

        procesos(reloj, mario, FPS, frames_totales, fondo)

        if frames_totales % (FPS / 4) == 0:

            segundo += 0.25

        dibujo(fondo, ventana, colores)

        frames_totales += 1



