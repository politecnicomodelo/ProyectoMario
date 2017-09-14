from clases.control.Base import *
import pygame

ancho = 1280
alto = 720

movimientos = {"quieto": "imagenes/mario/mario.png",
               "camina": "imagenes/mario/mario_movimiento.png",
               "correr": "imagenes/mario/mario_correr.png"}

class Mario(Base):

    def __init__(self):

        Base.__init__(self, ancho-1260, 600, 100, 100, "imagenes/mario/mario.png")
        self.direccion = True
        Base.sprites.add(self)
        self.movimiento = 0

    def mover_derecha(self, velocidad):

        if self.direccion is False:
            self.direccion = True
            self.cambiar_sprite(movimientos["quieto"])
            self.movimiento = 0
            return

        if self.movimiento == 2:
            self.cambiar_sprite(movimientos["camina"])
            self.movimiento = 1

        elif self.movimiento == 1:
            print("ENTRE")
            self.cambiar_sprite(movimientos["correr"])
            self.movimiento = 2

        elif self.movimiento == 0:
            self.cambiar_sprite(movimientos["camina"])
            self.movimiento = 1

        self.rect.x += velocidad

    def mover_izquierda(self, velocidad):

        if self.direccion is True:
            self.direccion = False
            self.invertir()
            return

        if self.movimiento == 2:
            self.cambiar_sprite(movimientos["camina"])
            self.invertir()
            self.movimiento = 1

        elif self.movimiento == 1:
            print("ENTRE")
            self.cambiar_sprite(movimientos["correr"])
            self.invertir()
            self.movimiento = 2

        elif self.movimiento == 0:
            self.cambiar_sprite(movimientos["camina"])
            self.invertir()
            self.movimiento = 1

        self.rect.x -= velocidad

    def invertir(self):

        self.image = pygame.transform.flip(self.image, True, False)
        self.image = pygame.transform.scale(self.image, (100, 100))

    def cambiar_sprite(self, movimiento):

        self.image = pygame.image.load(movimiento)
        self.image = pygame.transform.scale(self.image, (100, 100))




