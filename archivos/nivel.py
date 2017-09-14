from clases.control.Controlador import *
from archivos.dibujo import *
from archivos.procesos import *


def nivel(reloj, mario, ventana, colores, fondo):

    FPS = 120

    frames_totales = 0

    segundo = 0

    while True:

        if frames_totales % (FPS / 4) == 0:

            segundo += 0.25

        dibujo()

        procesos()