from clases.control import *
import pygame


def procesos(reloj, mario, FPS, frames_totales, fondo, fuentes, textos):

    Controlador.set_fps(reloj, FPS)

    Controlador.buscar_eventos(mario)

    teclas = Controlador.buscar_teclas()

    if mario.muerto is False:

        if teclas[pygame.K_F1]:
            Controlador.pausa(mario, ventana)

        if mario.animacion_castillo is False:

            #if teclas[pygame.K_d] or teclas[pygame.K_RIGHT]:
            if mario.permitir_derecha:
                if mario.mover_pantalla():
                    Controlador.mover_pantalla(fondo, mario)
                if mario.salto:
                    mario.mover_derecha(6, frames_totales)
                else:
                    mario.mover_derecha(8, frames_totales)

            elif mario.permitir_izquierda:
                if mario.salto:
                    mario.mover_izquierda(6, frames_totales)
                else:
                    mario.mover_izquierda(8, frames_totales)

            if mario.permitir_salto and mario.salto is False:
                if mario.colision_piso():
                    mario.activar_salto(340)
                else:
                    mario.activar_salto(290)

            Controlador.salto_mario(mario, frames_totales)

            Controlador.colisiones(mario, frames_totales)

            Controlador.actualizar_monedas(mario, fuentes, textos)

    if Controlador.actualizar_secundarios(frames_totales, mario, fondo):
        return True

    Controlador.eliminar_sprites(mario)

    '''
    print("Pos X: " + str(mario.rect.x))
    print("Pos Y: " + str(mario.rect.y))
    print("Bajando? :" + str(mario.bajando))
    print("Salto: " + str(mario.salto))
    print("Detenido? :" + str(mario.detenido))
    print("Flanco: " + str(mario.flanco))
    '''
    if Controlador.verificar_muerte(mario):
        return True
    return False