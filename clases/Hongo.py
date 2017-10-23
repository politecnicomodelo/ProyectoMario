from clases.control.Base import Base
import pygame

class Hongo(Base):

    def __init__(self, x, y):

        Base.__init__(self, x, y, 50, 50, "imagenes/hongo.png")
        Base.sprites.add(self)
        Base.hongos.add(self)

        self.estatico = False
        self.direccion = False
        self.frame = 0
        self.agarrado = False
        self.bajando = False

    def movimiento(self, frames_totales):

        if self.estatico:
            self.frame = frames_totales
            self.estatico = False

        piso = self.colision(Base.piso)
        if piso is not False:
            if self.bajando:
                self.bajando = False
            objeto = self.colision(Base.tuberias)
            if objeto is False:
                objeto = self.colision(Base.escalera)

            if objeto is not False:
                if self.direccion:
                    self.direccion = False
                else:
                    self.direccion = True
            self.moverse(6)
        else:
            if self.frame + 50 < frames_totales:
                bloque = self.colision(Base.bloques)
                if bloque is not False:
                    if self.bajando:
                        self.bajando = False
                    self.moverse(4)
                else:
                    if self.bajando is False:
                        self.bajando = True

                    self.rect.y += 9
                    self.rect.x += 2

                    piso = self.colision(Base.piso)
                    if piso is not False:
                        self.rect.y = piso.rect.y - 49
            else:
                self.rect.y -= 1

    def colision(self, grupo):

        elemento = pygame.sprite.spritecollideany(self, grupo, collided = None)
        if elemento is not None:
            return elemento
        else:
            return False

    def moverse(self, velocidad):
        if self.direccion:
            self.rect.x += velocidad
        else:
            self.rect.x -= velocidad