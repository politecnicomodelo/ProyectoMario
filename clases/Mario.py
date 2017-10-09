from clases.control.Controlador import Controlador
from clases.control.Base import *
from clases import *
from clases.control.Corazon import *
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

        self.inmune = False
        self.frame_inmune = 0
        self.rebote = False

        self.vidas = 3

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
        self.image = pygame.transform.scale(self.image, (self.ancho, self.alto))

    def cambiar_sprite(self, movimiento):

        self.image = pygame.image.load(movimiento)
        self.image = pygame.transform.scale(self.image, (self.ancho, self.alto))

    def detenerse(self):

        if self.salto is False:
            self.cambiar_sprite(self.movimientos[0])
            if self.direccion is False:
                self.invertir()

    def activar_salto(self, cantidad):

        self.maximo = self.rect.y - cantidad
        self.salto = True
        self.cambiar_sprite(self.movimientos[4])
        if self.direccion is False:
            self.invertir()

    def saltar(self, frames_totales):

        if self.maximo == self.rect.y:
            self.bajando = True

        if self.bajando is False:

            if self.rect.y <= self.maximo + 60:
                self.rect.y -= 10
            else:
                self.rect.y -= 20

        if self.bajando is True:
            self.rect.y += 20

        self.colisiones_con_salto(frames_totales)

    def colisiones_con_salto(self, frames_totales):

        if self.colision(Base.piso) is not False:
            self.terminar_salto()

        tuberia = self.colision(Base.tuberias)
        if tuberia is not False:
            self.colision_tuberia_salto(tuberia)

        escalera = self.colision(Base.escalera)
        if escalera is not False:
            self.colision_escalera_salto(escalera)

        if self.inmune is False:
            goomba = self.colision(Base.goombas)
            if goomba is not False:
                if goomba.muerto is False:
                    goomba.morir(frames_totales)
                    self.colision_goomba(goomba)

        #Colisiona con dos objetos?
        bloque, bloque2 = Controlador.buscar_objetos(self)

        if bloque2 is not False:
            #Cuál está mas cerca de rect.x
            comparacion = self.rect.x - bloque.rect.x
            comparacion2 = self.rect.x - bloque2.rect.x
            if comparacion < 0:
                comparacion = comparacion + comparacion * -1 + comparacion * -1
            if comparacion2 < 0:
                comparacion2 = comparacion2 + comparacion2 * -1 + comparacion2 * -1
            if comparacion > comparacion2:
                bloque = bloque2

        #Chocó con un bloque?
        if bloque is not False:
            self.colision_bloques_salto(bloque)

    def colision_bloques_salto(self, objeto):

        #Chocó mientras estaba subiendo?
        if self.bajando is False:

            #Está dentro de la hitbox del bloqe?
            if self.rect.x < objeto.rect.x + 45 and self.rect.x > objeto.rect.x - 80:

                #Está debajo del bloque?
                if self.rect.y + 65 >= objeto.rect.y:
                    self.bajando = True
                    if objeto in Base.signos:
                        if objeto.proceso is False:
                            objeto.activar_tocado()
                elif self.rect.y >= objeto.rect.y + 55 and objeto in Base.signos:
                    self.bajando = True

            else:
                #Está a la derecha del bloque?
                if self.rect.x >= objeto.rect.x:
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
            bloque, bloque2 = Controlador.buscar_objetos(self)

            if bloque is not False and bloque2 is not False:
                return False

            #Me caí de un bloque?
            if self.colision_bloques_caida(bloque):
                return True
            else:
                return False

        if bloque is False:
            return True

        return False

    def colision_bloques_caida(self, bloque):

        #Chocó estando en la hitbox?
        if self.rect.x < bloque.rect.x + 60 and self.rect.x > bloque.rect.x - 90:

            #Chocó estando sobre el bloque?
            if bloque.rect.y >= self.rect.y + 82:
                if self.bajando:
                    self.terminar_salto()
                return False

            #Chocó en la derecha?
            elif self.rect.x > bloque.rect.x:
                self.rect.x = bloque.rect.x + 70
            #Chocó en la izquierda?
            elif self.rect.x < bloque.rect.x:
                self.rect.x = bloque.rect.x - 95

        return True

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

    def colision_tuberia(self, tuberia):

        if tuberia.rect.x > self.rect.x:
            self.rect.x = tuberia.rect.x - 90
        else:
            self.rect.x = tuberia.rect.x + 145

    def colision_tuberia_salto(self, tuberia):

        #Está subiendo?
        if self.bajando is False:

            #Está a la derecha del bloque?
            if self.rect.x >= tuberia.rect.x:
                self.rect.x = tuberia.rect.x + 145

            #Está a la izquierda del bloque?
            elif self.rect.x < tuberia.rect.x:
                self.rect.x = tuberia.rect.x - 90

        else:
            self.colision_tuberia_caida(tuberia)

    def colision_tuberia_caida(self, tuberia):

            #Chocó estando sobre el bloque?
            if self.rect.x - 120 <= tuberia.rect.x and self.rect.x + 60 >= tuberia.rect.x:
                if tuberia.alto == 1 or tuberia.alto == 2:
                    if tuberia.rect.y >= self.rect.y + 80:
                        self.terminar_salto()
                elif tuberia.alto == 3:
                    if tuberia.rect.y >= self.rect.y + 75:
                        self.terminar_salto()
                return False
            #Chocó estando fuera de la hitbox?
            else:
                if self.rect.x > tuberia.rect.x:
                    self.rect.x = tuberia.rect.x + 145
                elif self.rect.x < tuberia.rect.x:
                    self.rect.x = tuberia.rect.x - 90
                return True

    def colision_escalera(self, escalera):

        escalera2 = False
        #Estoy sobre una escalera?
        if escalera.rect.y >= self.rect.y + 79:
            if escalera in Base.escaleras:
                escalera2 = self.colision(Base.escaleras2)
            else:
                escalera2 = self.colision(Base.escaleras)

            if escalera2 is not False:
                escalera = escalera2

        if escalera2 is not False or self.colision_piso():
            if escalera.rect.x > self.rect.x:
                self.rect.x = escalera.rect.x - 90
            else:
                self.rect.x = escalera.rect.x + 70
            return False

        if self.colision_escalera_caida() is False:
            return False

        return True

    def colision_escalera_salto(self, escalera):

        if self.bajando is False:
            #Está a la derecha del bloque?
            if self.rect.x >= escalera.rect.x:
                self.rect.x = escalera.rect.x + 70

            #Está a la izquierda del bloque?
            elif self.rect.x < escalera.rect.x:
                self.rect.x = escalera.rect.x - 100

        else:
            self.colision_escalera_caida()

    def colision_escalera_caida(self):

        escalera = self.colision(Base.escalera)

        #Caí sobre la escalera?
        if self.rect.x + 85 >= escalera.rect.x and self.rect.x - 50 <= escalera.rect.x:
            if escalera.rect.y >= self.rect.y + 79:
                self.rect.y = escalera.rect.y - 93
                self.terminar_salto()
                return False
        else:
            #Está a la derecha del bloque?
            if self.rect.x >= escalera.rect.x:
                self.rect.x = escalera.rect.x + 70

            #Está a la izquierda del bloque?
            elif self.rect.x < escalera.rect.x:
                self.rect.x = escalera.rect.x - 90
            return True

    def colision_goomba(self, goomba):
        goomba.achicar()
        self.rebote = True

    def verificar_inmunidad(self, frames_totales):
        if self.inmune:
            if self.frame_inmune + 90 < frames_totales:
                self.inmune = False

    def empiezo_inmunidad(self, frames_totales):
        self.inmune = True
        self.frame_inmune = frames_totales

    def inicializar_vidas(self):

        for i in range(self.vidas):
            vida = Corazon()