from archivos.dibujo import *
from archivos.procesos import *
from archivos.inicializacion import *


def nivel(reloj, mario, ventana, colores, fondo):

    terminar = False

    FPS = 120

    frames_totales = 0

    segundo = 0

    inicializacion(mario)

    while True:

        if procesos(reloj, mario, FPS, frames_totales, fondo, ventana):
            mario.tiempo = segundo
            return True
        if frames_totales % (FPS / 4) == 0:
            segundo += 1

        dibujo(fondo, ventana, colores)

        frames_totales += 1