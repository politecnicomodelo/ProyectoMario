from clases import *
import pygame.locals
from clases.control.Base import *

class Controlador(object):

    @classmethod
    def iniciar(cls):
        pygame.init()

    @classmethod
    def terminar(cls):
        pygame.quit()
        quit()

    @classmethod
    def configurar_pantalla(cls, ancho, alto):

        display = pygame.display.set_mode((ancho, alto)) #, pygame.FULLSCREEN
        pygame.display.set_caption("Super Mega Mario Bros")
        return display

    @classmethod
    def iniciar_reloj(cls):
        return pygame.time.Clock()

    @classmethod
    def set_fps(cls, reloj, frames):
        reloj.tick(frames)

    @classmethod
    def rellenar_pantalla(cls, ventana, fondo, colores):
        ventana.fill(colores["Negro"])
        ventana.blit(fondo.image, fondo.rect)

    @classmethod
    def mover_pantalla(cls, fondo, mario):
        fondo.rect.x -= 20
        for item in Base.sprites:
            if item is not mario:
                item.rect.x -= 20


    @classmethod
    def buscar_eventos(cls, mario):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                cls.terminar()
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
                cls.terminar()
            if evento.type == pygame.KEYUP:
                if mario.bajando is False:
                    mario.detenerse()

    @classmethod
    def buscar_teclas(cls):
        return pygame.key.get_pressed()

    @classmethod
    def eliminar_sprites(cls, mario):
        for item in Base.sprites:
            if item.rect.x < -40:
                if item is not mario:

                    if item in Base.tuberias:
                        if item.rect.x < -85:
                            Base.sprites.remove(item)
                            Base.tuberias.remove(item)
                    else:
                        Base.sprites.remove(item)
                        if item in Base.bloques:

                            Base.bloques.remove(item)
                            if item in Base.ladrillos:
                                Base.ladrillos.remove(item)
                            elif item in Base.ladrillos2:
                                Base.ladrillos2.remove(item)
                            else:
                                Base.signos.remove(item)

                        elif item in Base.piso:
                            Base.piso.remove(item)

    @classmethod
    def salto_mario(cls, mario):

        if mario.salto:
            mario.saltar()

    @classmethod
    def colisiones(cls, mario):

        moneda = mario.colision(Base.monedas)
        if moneda is not False:
            moneda.agarrada()

        #Mientras anda a pie
        if mario.salto is False:

            #Hay colision con el piso?
            if mario.colision_piso() is False:

                objeto = mario.colision(Base.escalera)
                if objeto is not False:
                    if mario.colision_escalera_caida(objeto) is False:
                        objeto = False
                    else:
                        mario.colision_escalera(objeto)
                        #Si está cayendo, evitar buscar colision y evitar que solape

                if objeto is False:
                    #Hay colision con la tuberia?
                    objeto = mario.colision(Base.tuberias)

                    if objeto is not False:
                        bajar = mario.colision_tuberia_caida(objeto)
                        if bajar is False:
                            mario.caerse()
                    else:
                        #Hay colision con algun bloque?
                        objeto = mario.colision(Base.bloques)
                        if objeto is not False:
                            mario.colision_bloques_caida(objeto)

                        if mario.colision_bloques(objeto):
                            mario.caerse()
            else:
                tuberia = mario.colision(Base.tuberias)
                if tuberia is not False:
                    mario.colision_tuberia(tuberia)

                escalera = mario.colision(Base.escalera)
                if escalera is not False:
                    mario.colision_escalera(escalera)

                if mario.bajando:
                    mario.detenerse()
                    mario.bajando = False

    @classmethod
    def buscar_objetos(cls, mario):
        bloque = mario.colision(Base.bloques)
        bloque2 = False

        if bloque in Base.signos:
            bloque2 = mario.colision(Base.ladrillos)
            if bloque2 is False:
                bloque2 = mario.colision(Base.ladrillos2)
        else:
            if bloque in Base.ladrillos:
                bloque2 = mario.colision(Base.ladrillos2)
            elif bloque in Base.ladrillos2:
                bloque2 = mario.colision(Base.ladrillos)
            if bloque2 is False:
                bloque2 = mario.colision(Base.signos)

        return bloque, bloque2

    @classmethod
    def actualizar_secundarios(cls, frames_totales):
        for moneda in Base.monedas:
            if moneda.movible:
                moneda.movimiento()
                moneda.animacion(frames_totales)
        for item in Base.signos:
            if item.proceso:
                item.tocado()