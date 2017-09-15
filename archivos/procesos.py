from clases.control import *
import pygame

def procesos(reloj, mario, FPS, segundo, estatico):

    Controlador.set_fps(reloj, FPS)
    Controlador.buscar_eventos()

    teclas = pygame.key.get_pressed()

    if teclas[pygame.K_d] or teclas[pygame.K_RIGHT]:
        mario.mover_derecha(15)

    elif teclas[pygame.K_a] or teclas[pygame.K_LEFT]:
        mario.mover_izquierda(15)

















    #if teclas[pygame.K_s] or teclas[pygame.K_DOWN]:
    # Algo

    #elif teclas[pygame.K_w] or teclas[pygame.K_UP]:
    # Algo