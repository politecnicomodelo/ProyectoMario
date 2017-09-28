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

        if self.salto is False and self.bajando is False:
            if frames_totales - self.frame > 2:

                if self.estado >= 0 and self.estado <= 2:
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

        if self.salto is False and self.bajando is False:
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

        objeto = self.colision(Base.bloques)

        objeto2 = False
        #Colisiona con dos objetos?
        if objeto in Base.bloques:
            objeto2 = self.colision(Base.ladrillos2)
            if objeto2 is False:
                objeto2 = self.colision(Base.signos)
                if objeto2 is False:
                    objeto2 = self.colision(Base.ladrillos)

        if objeto2 is not False:
            #Cuál está mas cerca de rect.x
            comparacion = self.rect.x - objeto.rect.x
            comparacion2 = self.rect.x - objeto2.rect.x
            if comparacion < 0:
                comparacion = comparacion + -(comparacion) + comparacion
            if comparacion2 < 0:
                comparacion2 = comparacion2 + -(comparacion2) + comparacion2
            if comparacion > comparacion2:
                objeto = objeto2

        #Chocó con un bloque?
        if objeto is not False:
            self.colision_bloques_salto(objeto)

    def colision_bloques_salto(self, objeto):

        #Chocó mientras estaba subiendo?
        if self.bajando is False:

            #Está dentro de la hitbox del bloque?
            if self.rect.x < objeto.rect.x + 60 and self.rect.x > objeto.rect.x - 90:

                #Está debajo del bloque?
                if self.rect.y > objeto.rect.y + 65:
                    self.bajando = True

                #Está a la derecha del bloque?
                elif self.rect.x >= objeto.rect.x:
                    self.rect.x = objeto.rect.x + 70

                #Está a la izquierda del bloque?
                elif self.rect.x < objeto.rect.x:
                    self.rect.x = objeto.rect.x - 95

        #Está bajando?
        else:
            self.colision_bloques_caida(objeto)

    def colision_bloques(self, bloque):

        if bloque is not False:

            #Me crucé con un bloque mientras caminaba?
            if bloque in Base.signos:
                bloque2 = self.colision(Base.ladrillos)
                if bloque2 is False:
                    bloque2 = self.colision(Base.ladrillos2)
            else:
                if bloque in Base.ladrillos:
                    bloque2 = self.colision(Base.ladrillos2)
                elif bloque in Base.ladrillos2:
                    bloque2 = self.colision(Base.ladrillos)
                if bloque2 is False:
                    bloque2 = self.colision(Base.signos)

            if bloque is not False and bloque2 is not False:
                return False

            #Me caí de un bloque?
            if self.rect.x > bloque.rect.x + 60 or self.rect.x < bloque.rect.x - 90:

                return True

        if bloque is False:
            return True

        return False

    def colision_bloques_caida(self, bloque):

        #Chocó estando en la hitbox?
        if self.rect.x < bloque.rect.x + 60 and self.rect.x > bloque.rect.x - 90:

            #Chocó estando sobre el bloque?
            if bloque.rect.y >= self.rect.y + 90:

                self.terminar_salto()

            #Chocó estando fuera de la hitbox?
            #Chocó en la derecha?
            elif self.rect.x > bloque.rect.x:
                self.rect.x = bloque.rect.x + 70
            #Chocó en la izquierda?
            elif self.rect.x < bloque.rect.x:
                self.rect.x = bloque.rect.x - 95

    def terminar_salto(self):
        if self.bajando:
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
        if self.bajando is False:
            self.bajando = True
            self.cambiar_sprite(self.movimientos[4])
            if self.direccion is False:
                self.invertir()

    def calcular_caida(self):

        if self.salto is False:

            objeto = self.colision(Base.bloques)

            if self.bajando:
                self.colision_bloques(objeto)

            if objeto is not False:
                if self.rect.x < objeto.rect.x + 55 and self.rect.x > objeto.rect.x - 90:
                    self.bajando = False
                else:
                    self.caerse()
            else:
                self.caerse()

    def colision_piso(self):

        if self.colision(Base.piso) is False:
            return False
        return True