from tutorial.clases.Base import *

import pygame

ancho = 1280
alto = 720

class Mario_T(Base):

    def __init__(self):

        Base.__init__(self, 20, 600, 100, 100, "imagenes/mario/mario.png")

        self.estado = 0
        self.direccion = True
        self.detenido = False
        self.movimientos = ("imagenes/mario/mario.png", "imagenes/mario/mario_correr.png",
                            "imagenes/mario/mario_turbio.png", "imagenes/mario/mario_movimiento.png",
                            "imagenes/mario/mario_salto.png", "imagenes/invisiblex.png",
                            "imagenes/mario/mario_muerto.png",
                            "imagenes/mario/mario_bandera.png",)
        self.frame = 0
        self.maximo = 0
        self.salto = False
        self.bajando = False
        self.detenido = True

        self.terminado = False

        self.permitir_derecha = False
        self.permitir_izquierda = False
        self.permitir_salto = False
        self.permitir = True
        self.frame_permitido = 0

        Base.sprites.add(self)

    def mover_derecha(self, velocidad, frames_totales):

        self.detenido = False

        if self.salto is False and self.bajando is False:
            if frames_totales - self.frame > 4:
                if self.estado <= 2:
                    self.estado += 1
                    self.frame = frames_totales
                    self.cambiar_sprite(self.estado)

                elif self.estado == 3:
                    self.estado = 1
                    self.frame = frames_totales
                    self.cambiar_sprite(self.estado)

        if self.permitir_derecha and self.rect.x < 1180:
            self.rect.x += velocidad

    def mover_izquierda(self, velocidad, frames_totales):

        self.detenido = False

        if self.salto is False and self.bajando is False:
            if (frames_totales - self.frame) > 4:

                if self.estado == 0 or self.estado == 1 or self.estado == 2:
                    self.estado += 1
                    self.frame = frames_totales
                    self.cambiar_sprite(self.estado)

                elif self.estado == 3:
                    self.estado = 1
                    self.frame = frames_totales
                    self.cambiar_sprite(self.estado)

        if self.rect.x > -10:
            self.rect.x -= velocidad

    def cambiar_sprite(self, estado):
        self.image = pygame.image.load(self.movimientos[estado])
        self.image = pygame.transform.scale(self.image, (self.ancho, self.alto))
        if self.direccion is False:
            self.invertir()

    def invertir(self):
        self.image = pygame.transform.flip(self.image, True, False)
        self.image = pygame.transform.scale(self.image, (self.ancho, self.alto))

    def colision(self, grupo):
        elemento = pygame.sprite.spritecollideany(self, grupo, collided=None)
        if elemento is not None:
            return elemento
        else:
            return False

    def colision_piso(self):

        piso = self.colision(Base.piso)

        if self.colision(Base.piso) is False:
            return False
        if self.rect.y <= piso.rect.y - 80:
            self.rect.y = piso.rect.y - 95
            return True

    def detenerse(self):
        if self.detenido is False:
            self.detenido = True
        if self.salto is False:
            self.cambiar_sprite(0)

    def detenerse_bloque(self, objeto, cantidad):

        if self.detenido and self.salto is False:
            self.cambiar_sprite(5)
            self.rect.y = objeto.rect.y - cantidad
            self.cambiar_sprite(0)
            self.permitir_derecha = False
            self.permitir_izquierda = False

    def activar_salto(self, cantidad):

        self.maximo = self.rect.y - cantidad
        self.salto = True
        self.cambiar_sprite(4)
        self.permitir_salto = False

    def saltar(self, frames_totales):

        self.detenido = False

        if self.maximo >= self.rect.y + 5 and self.maximo <= self.rect.y + 15:
            self.bajando = True

        if self.bajando is False:

            if self.rect.y <= self.maximo + 60:
                self.rect.y -= 5
            else:
                self.rect.y -= 10

        if self.bajando:
            self.rect.y += 10

        self.colisiones_con_salto(frames_totales)

    def colisiones_con_salto(self, frames_totales):

        if self.colision_piso():
            self.terminar_salto()

        bloque = self.colision(Base.bloques)

        if bloque is not False:
            self.colision_bloques_salto(bloque)

    def colision_bloques_salto(self, objeto):

        # Chocó mientras estaba subiendo?
        if self.bajando is False:

            # Está dentro de la hitbox del bloqe?
            if self.rect.x < objeto.rect.x + 45 and self.rect.x > objeto.rect.x - 80:

                # Está debajo del bloque?
                if self.rect.y + 65 >= objeto.rect.y:
                    self.bajando = True

            else:
                # Está a la derecha del bloque?
                if self.rect.x >= objeto.rect.x:
                    self.rect.x = objeto.rect.x + 70

                # Está a la izquierda del bloque?
                elif self.rect.x < objeto.rect.x:
                    self.rect.x = objeto.rect.x - 95

        # Está bajando?
        else:
            self.colision_bloques_caida(objeto)

    def colision_bloques_caida(self, bloque):

        # Chocó estando en la hitbox?
        if self.rect.x < bloque.rect.x + 60 and self.rect.x > bloque.rect.x - 90:

            # Chocó estando sobre el bloque?
            if bloque.rect.y >= self.rect.y + 80:
                self.terminar_salto()
                self.detenerse_bloque(bloque, 95)
                return False


            # Chocó en la derecha?
            elif self.rect.x > bloque.rect.x:
                self.rect.x = bloque.rect.x + 70
            # Chocó en la izquierda?
            elif self.rect.x < bloque.rect.x:
                self.rect.x = bloque.rect.x - 95

        return True

    def terminar_salto(self):
        if self.bajando:
            self.bajando = False
            self.salto = False
            self.detenerse()

    def colision_bloques(self, bloque):

        if bloque is not False:

            # Me caí de un bloque?
            if self.colision_bloques_caida(bloque):
                return True
            else:
                return False

        if bloque is False:
            return True

        return False

    def caerse(self):
        self.rect.y += 10
        if self.bajando is False:
            self.bajando = True
            self.cambiar_sprite(4)