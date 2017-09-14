import pygame
from clases.control import *
from clases import *

def dibujo(ventana, colores):

    Controlador.rellenar_pantalla(ventana, colores["Negro"])
    #IMPRIMIR PERSONAJES Y COSAS NAZIS
    pygame.display.flip()