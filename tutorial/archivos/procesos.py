import pygame
from tutorial.clases.Controlador import Controlador


def procesos(reloj, mario, FPS, frames_totales, ventana):

    Controlador.set_fps(reloj, FPS)

    Controlador.buscar_eventos(mario)

    teclas = pygame.key.get_pressed()

    if teclas[pygame.K_F1]:
        Controlador.pausa(mario, ventana)

    if mario.permitir:

        if mario.permitir_derecha:
            mario.mover_derecha(3, frames_totales)

        elif mario.permitir_izquierda:
            mario.mover_izquierda(3, frames_totales)

        if mario.permitir_salto and mario.salto is False:
            mario.activar_salto(340)

    else:
        mario.detenerse()

    Controlador.salto_mario(mario, frames_totales)

    if Controlador.colisiones(mario, frames_totales):
        return True