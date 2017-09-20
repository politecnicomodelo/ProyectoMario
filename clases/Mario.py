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

        self.rect.x += velocidad

    def mover_izquierda(self, velocidad, frames_totales):

        if self.direccion is True:
            self.direccion = False
            self.invertir()
            return

        if self.salto is False:
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

        if self.salto is False:
            self.cambiar_sprite(self.movimientos[0])
            if self.direccion is False:
                self.invertir()
            if self.salto is True:
                self.continuar = False

    def activar_salto(self):

        self.original = self.rect.y
        self.maximo = self.rect.y - 300
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
            self.bajando = False
            self.salto = False
            self.detenerse()


    def mover_pantalla(self):
        if self.rect.x > 680:
            return True

    def colision(self, grupo):

        elemento = pygame.sprite.spritecollideany(self, grupo, collided = None)
        if elemento is not None:
            return elemento
        else:
            return False

    def caerse(self):
        self.rect.y += 20
        # Reaparecer