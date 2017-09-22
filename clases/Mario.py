from clases.control.Base import *
from clases import *
import pygame

ancho = 1280
alto = 720

class Mario(Base):

    def __init__(self):

        Base.__init__(self, ancho-1260, 600, 100, 100, "imagenes/mario/mario.png")
        self.estado = 0
        self.direccion = True
        self.movimientos = ("imagenes/mario/mario.png", "imagenes/mario/mario_correr.png",
                            "imagenes/mario/mario_turbio.png", "imagenes/mario/mario_movimiento.png",
                            "imagenes/mario/mario_salto.png",)
        self.frame = 0

        self.maximo = 0
        self.salto = False
        self.bajando = False

        Base.sprites.add(self)

    def mover_derecha(self, velocidad, frames_totales):

        if self.direccion is False:
            self.direccion = True
            self.invertir()
            self.estado = 0
            return

        if self.salto is False:
            if (frames_totales - self.frame > 2):

                if self.estado == 0 or self.estado == 1 or self.estado == 2:
                    self.estado += 1
                    self.frame = frames_totales
                    self.cambiar_sprite(self.movimientos[self.estado])

                elif self.estado == 3:
                    self.estado = 1
                    self.frame = frames_totales
                    self.cambiar_sprite(self.movimientos[self.estado])

        if self.mover_pantalla() is False:
            self.rect.x += velocidad

    def mover_izquierda(self, velocidad, frames_totales):

        if self.direccion is True:
            self.direccion = False
            self.invertir()
            return

        if self.salto is False:
            if (frames_totales - self.frame) > 2:

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

        if self.rect.x > -10:
            self.rect.x -= velocidad

    def invertir(self):

        self.image = pygame.transform.flip(self.image, True, False)
        self.image = pygame.transform.scale(self.image, (100, 100))

    def cambiar_sprite(self, movimiento):

        self.image = pygame.image.load(movimiento)
        self.image = pygame.transform.scale(self.image, (100, 100))

    def detenerse(self):

        if self.salto is False:
            self.cambiar_sprite(self.movimientos[0])
            if self.direccion is False:
                self.invertir()

    def activar_salto(self):

        self.original = self.rect.y
        self.maximo = self.rect.y - 320
        self.salto = True
        self.cambiar_sprite(self.movimientos[4])
        if self.direccion is False:
            self.invertir()

    def saltar(self):

        if self.maximo == self.rect.y:
            self.bajando = True

        if self.bajando is False:

            if self.rect.y <= self.maximo + 60:
                self.rect.y -= 10
            else:
                self.rect.y -= 20

        if self.bajando is True:
            self.rect.y += 20

        self.colisiones_con_salto()

    def colisiones_con_salto(self):

        if self.colision(Base.piso) is not False:
            self.terminar_salto()

        self.colision_bloques()

    def colision_bloques(self):

        objeto = self.colision(Base.bloques)

        if objeto is not False:

            if self.bajando is False:
                if self.rect.x < objeto.rect.x + 60 and self.rect.x > objeto.rect.x - 90 and self.rect.y > objeto.rect.y + 65: #Está dentro de los parametros del bloque?
                    self.bajando = True
                else: #Si está colisionando, pero fuera de los parámetros regulares del bloque, entonces evita la solapación
                    if self.rect.x > objeto.rect.x:
                        self.rect.x = objeto.rect.x + 80
                    else:
                        self.rect.x = objeto.rect.x - 120

            elif self.bajando is True and objeto.rect.y >= self.rect.y + 90: #Si está sobre el bloque se mantiene
                self.terminar_salto()

            elif self.bajando: #Si está bajando por alguno de los bordes
                if self.rect.x > objeto.rect.x:
                    self.rect.x = objeto.rect.x + 80
                else:
                    self.rect.x = objeto.rect.x - 120

    def terminar_salto(self):
        self.bajando = False
        self.salto = False
        self.detenerse()

    def mover_pantalla(self):
        if self.rect.x > 680:
            return True
        return False

    def colision(self, grupo):

        elemento = pygame.sprite.spritecollideany(self, grupo, collided = None)
        if elemento is not None:
            return elemento
        else:
            return False

    def caerse(self):
        self.rect.y += 20
        self.bajando = True