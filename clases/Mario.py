from clases.control.Base import *
import pygame

ancho = 1280
alto = 720

class Mario(Base):

    def __init__(self):

        Base.__init__(self, ancho-1260, 600, 100, 100, "imagenes/mario/mario.png")
        self.estado = 0
        self.direccion = True
        self.movimientos = ("imagenes/mario/mario.png", "imagenes/mario/mario_correr.png",
                            "imagenes/mario/mario_turbio.png", "imagenes/mario/mario_movimiento.png",)
        self.frame = 0
        Base.sprites.add(self)

    def mover_derecha(self, velocidad, frames_totales):

        if self.direccion is False:
            self.direccion = True
            self.invertir()
            self.estado = 0
            return

        if (frames_totales - self.frame > 2):

            if self.estado == 0 or self.estado == 1 or self.estado == 2:
                self.estado += 1
                self.frame = frames_totales
                self.cambiar_sprite(self.movimientos[self.estado])

            elif self.estado == 3:
                self.estado = 1
                self.frame = frames_totales
                self.cambiar_sprite(self.movimientos[self.estado])

        self.rect.x += velocidad

    def mover_izquierda(self, velocidad, frames_totales):

        if self.direccion is True:
            self.direccion = False
            self.invertir()
            return

        if (frames_totales - self.frame > 2):

            if self.estado == 0 or self.estado == 1 or self.estado == 2:
                self.estado += 1
                self.frame = frames_totales
                self.cambiar_sprite(self.movimientos[self.estado])
                self.invertir()

            elif self.estado == 3:
                self.estado = 1
                self.frame = frames_totales
                self.cambiar_sprite(self.movimientos[self.estado])
                self.invertir()

        self.rect.x -= velocidad

    def invertir(self):

        self.image = pygame.transform.flip(self.image, True, False)
        self.image = pygame.transform.scale(self.image, (100, 100))

    def cambiar_sprite(self, movimiento):

        self.image = pygame.image.load(movimiento)
        self.image = pygame.transform.scale(self.image, (100, 100))

    def detenerse(self):

        self.cambiar_sprite(self.movimientos[0])
        if self.direccion is False:
            self.invertir()




