from clases.control.Base import *
import pygame

ancho = 1280
alto = 720

movimientos = {"quieto": "imagenes/mario/mario.png",
               "turbio": "imagenes/mario/mario_turbio.png",
               "camina": "imagenes/mario/mario_movimiento.png",
               "correr": "imagenes/mario/mario_correr.png"}

class Mario(Base):

    def __init__(self):

        Base.__init__(self, ancho-1260, 600, 100, 100, "imagenes/mario/mario.png")
        self.direccion = True
        Base.sprites.add(self)
        self.movimiento = "quieto"

    def mover_derecha(self, velocidad):

        if self.direccion is False:
            self.direccion = True
            return

        self.rect.x += velocidad

    def mover_izquierda(self, velocidad):

        if self.direccion is True:
            self.direccion = False
            self.invertir()
            return

        self.rect.x -= velocidad

    def invertir(self):

        self.image = pygame.transform.flip(self.image, True, False)
        self.image = pygame.transform.scale(self.image, (100, 100))

    def cambiar_sprite(self, movimiento):

        self.image = pygame.image.load(movimiento)
        self.image = pygame.transform.scale(self.image, (100, 100))




