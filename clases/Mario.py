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

    def mover_derecha(self, velocidad, estatico, segundo):

        if self.direccion is False:
            self.direccion = True
            self.cambiar_sprite(movimientos["quieto"])
            self.movimiento = "caminar"
            return

        if self.movimiento == "caminar" and estatico[0] is False:
            self.cambiar_sprite(movimientos["camina"])
            self.movimiento = "correr"
            estatico[1] = segundo
            estatico[0] = True

        elif self.movimiento == "correr" and estatico[0] is False:
            self.cambiar_sprite(movimientos["correr"])
            self.movimiento = "caminar_bajo"
            estatico[1] = segundo
            estatico[0] = True

        elif self.movimiento == "caminar_bajo" and estatico[0] is False:
            self.cambiar_sprite(movimientos["turbio"])
            self.movimiento = "turbio"
            estatico[1] = segundo
            estatico[0] = True

        elif self.movimiento == "turbio" and estatico[0] is False:
            self.cambiar_sprite(movimientos["camina"])
            self.movimiento = "caminar"
            estatico[1] = segundo
            estatico[0] = True

        self.rect.x += velocidad

    def mover_izquierda(self, velocidad, estatico, segundo):

        if self.direccion is True:
            self.direccion = False
            self.invertir()
            return

        if self.movimiento == 2:
            self.cambiar_sprite(movimientos["camina"])
            self.invertir()
            self.movimiento = 1

        elif self.movimiento == 1:
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




