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
            if item.rect.x < -25:
                if item is not mario:
                    Base.sprites.remove(item)
                    if item in Base.bloques:
                        Base.bloques.remove(item)
                    elif item in Base.piso:
                        Base.piso.remove(item)

    @classmethod
    def salto_mario(cls, mario):

        if mario.salto:
            mario.saltar()

    @classmethod
    def colisiones(cls, mario):

        #Mientras anda a pie
        if mario.salto is False:

            #Hay colision con el piso?
            if mario.colision_piso() is False:

                objeto = mario.colision(Base.bloques)
                if objeto is not False:
                    mario.colision_bloques_caida(objeto)

                #Hay colision con algun bloque?
                if mario.colision_bloques(objeto):
                    mario.caerse()

            else:
                if mario.bajando:
                    mario.detenerse()
                    mario.bajando = False