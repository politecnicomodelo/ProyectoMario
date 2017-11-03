from archivos.dibujo import *
from archivos.procesos import *
from archivos.inicializacion import *
from clases.control.Base import Base


def nivel(reloj, mario, ventana, colores, fondo):

    terminar = False

    FPS = 120

    frames_totales = 0

    segundo = 0

    inicializacion(mario)

    fuentes = (pygame.font.SysFont("mariokartdsregular", 50), pygame.font.SysFont("mariokartdsregular", 35))
    textos = [fuentes[1].render("x", False, colores["Negro"]), fuentes[0].render("5", False, colores["Negro"])]

    while True:

        if procesos(reloj, mario, FPS, frames_totales, fondo, fuentes, textos, ventana):
            mario.tiempo = segundo
            return True

        if frames_totales % (FPS / 4) == 0:
            segundo += 1

        dibujo(fondo, ventana, colores, textos)

        frames_totales += 1
