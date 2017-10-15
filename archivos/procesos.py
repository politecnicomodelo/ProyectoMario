from clases.control import *
import pygame

def procesos(reloj, mario, FPS, frames_totales, fondo, ventana):

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

        if teclas[pygame.K_F1]:
            Controlador.pausa(mario, ventana)

        Controlador.colisiones(mario, frames_totales)

        Controlador.salto_mario(mario, frames_totales)

    Controlador.actualizar_secundarios(frames_totales, mario)

    Controlador.eliminar_sprites(mario)

    '''
    print("Salto: " + str(mario.salto))
    print("Bajando? :" + str(mario.bajando))
    print("Pos Y: " + str(mario.rect.y))
    print("Pos X: " + str(mario.rect.x))
    print("Detenido? :" + str(mario.detenido))
    print("Flanco: " + str(mario.flanco))
    '''
    if Controlador.verificar_muerte(mario):
        return True
    return False
