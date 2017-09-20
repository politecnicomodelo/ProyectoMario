import pygame
from clases.control import *

def dibujo(fondo, ventana, colores, mario):

    if mario.mover_pantalla():
        Controlador.mover_pantalla(fondo, mario)
    Controlador.rellenar_pantalla(ventana, fondo, colores)
    Base.sprites.draw(ventana)
    pygame.display.flip()