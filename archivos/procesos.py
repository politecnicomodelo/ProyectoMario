from clases.control import *
import pygame

def procesos(reloj, mario, FPS, frames_totales):

    Controlador.set_fps(reloj, FPS)
    Controlador.buscar_eventos(mario)

    teclas = pygame.key.get_pressed()

    if teclas[pygame.K_d] or teclas[pygame.K_RIGHT]:
        mario.mover_derecha(15, frames_totales)

    elif teclas[pygame.K_a] or teclas[pygame.K_LEFT]:
        mario.mover_izquierda(15, frames_totales)

    elif teclas[pygame.K_w] or teclas[pygame.K_UP] and mario.salto is False:
        mario.activar_salto()

    if mario.salto:
        mario.saltar()