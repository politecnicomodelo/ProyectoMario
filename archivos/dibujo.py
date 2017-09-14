import pygame
from clases.control import *

def dibujo(fondo, ventana, colores):

    Controlador.rellenar_pantalla(ventana, fondo, colores)
    Base.sprites.draw(ventana)
    pygame.display.flip()