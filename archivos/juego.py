import pygame
from clases.control.Controlador import *
from clases.control.Fondo import *

def juego(colores, ancho, alto, mario):

    Controlador.iniciar()

    ventana = Controlador.configurar_pantalla(ancho, alto)

    reloj = Controlador.iniciar_reloj()

    fondo = Fondo()

    while True:
        Controlador.buscar_eventos()

        teclas = pygame.key.get_pressed()

        Controlador.rellenar_pantalla(ventana, fondo)

        pygame.display.flip()

        Controlador.set_fps(reloj, 60)