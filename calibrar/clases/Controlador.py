import pygame
from tutorial.clases.Mario_Tuto import Mario_T
from tutorial.clases.Moneda import Moneda
from tutorial.clases.Base import Base
from tutorial.clases.Bloque import Bloque
from tutorial.clases.Fin import *

class Controlador(object):

    @classmethod
    def iniciar(cls):
        pygame.init()
        #pygame.mouse.set_visible(False)

    @classmethod
    def terminar(cls):
        pygame.quit()
        quit()

    @classmethod
    def configurar_pantalla(cls, ancho, alto):

        display = pygame.display.set_mode((ancho, alto)) #, pygame.FULLSCREEN
        pygame.display.set_caption("Super Poli Bros")
        return display

    @classmethod
    def iniciar_reloj(cls):
        return pygame.time.Clock()

    @classmethod
    def set_fps(cls, reloj, frames):
        reloj.tick(frames)

    @classmethod
    def rellenar_pantalla(cls, ventana):
        ventana.fill((255,255,255))

    @classmethod
    def buscar_eventos(cls):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                cls.terminar()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    cls.terminar()
                if evento.key == pygame.K_b:
                    return "empezar"
                if evento.key == pygame.K_v:
                    return "terminar"
                if evento.key == pygame.K_n:
                    return "hecho"
                if evento.key == pygame.K_m:
                    return "falla"
                if evento.key == pygame.K_c:
                    return "listo"
    @classmethod
    def buscar_teclas(cls):
        return pygame.key.get_pressed()
