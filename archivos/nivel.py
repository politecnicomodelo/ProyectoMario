from clases.control.Controlador import *
import pygame


def nivel(reloj, mario, ventana, colores, fondo):

    FPS = 120

    frames_totales = 0

    segundo = 0

    while True:

        Controlador.buscar_eventos()

        if frames_totales % (FPS / 4) == 0:

            segundo += 0.25

        teclas = pygame.key.get_pressed()

        if teclas[pygame.K_RIGHT]:

            fondo.rect.x -= 30

        Controlador.rellenar_pantalla(ventana, fondo)

        pygame.display.flip()

        Controlador.set_fps(reloj, FPS)