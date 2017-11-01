from tutorial.clases.Base import Base
from tutorial.clases.Controlador import Controlador
import pygame

def dibujo(ventana, colores):

    Controlador.rellenar_pantalla(ventana, colores)
    Base.sprites.draw(ventana)
    pygame.display.flip()