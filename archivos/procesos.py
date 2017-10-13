from clases.control import *
import pygame

def procesos(reloj, mario, FPS, frames_totales, fondo):

    Controlador.set_fps(reloj, FPS)

    Controlador.buscar_eventos(mario)

    teclas = Controlador.buscar_teclas()

    if mario.muerto is False:

        if teclas[pygame.K_d] or teclas[pygame.K_RIGHT]:
            if mario.mover_pantalla():
                Controlador.mover_pantalla(fondo, mario)
            mario.mover_derecha(14, frames_totales)

        elif teclas[pygame.K_a] or teclas[pygame.K_LEFT]:
            mario.mover_izquierda(14, frames_totales)

        if teclas[pygame.K_w] or teclas[pygame.K_UP] and mario.salto is False:
            mario.activar_salto(340)

        Controlador.colisiones(mario, frames_totales)

        Controlador.salto_mario(mario, frames_totales)

    Controlador.actualizar_secundarios(frames_totales, mario)

    Controlador.eliminar_sprites(mario)

    if Controlador.verificar_muerte(mario):
        return True
    return False