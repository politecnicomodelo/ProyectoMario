from clases.control.Base import Base
from clases.control.Controlador import Controlador
import pygame

def dibujo(fondo, ventana, colores):

    Controlador.rellenar_pantalla(ventana, fondo, colores)
    Base.sprites.draw(ventana)
    Base.sprites_principales.draw(ventana)
    pygame.display.flip()