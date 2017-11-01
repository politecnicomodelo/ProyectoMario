from clases.control.Base import Base
from clases.control.Controlador import Controlador
import pygame


def dibujo(fondo, ventana, colores, textos, mario):

    Controlador.rellenar_pantalla(ventana, fondo, colores)
    Base.sprites.draw(ventana)
    Base.sprites_principales.draw(ventana)
    ventana.blit(textos[0], (90, 111))
    ventana.blit(textos[1], (120, 102))
    pygame.display.flip()
