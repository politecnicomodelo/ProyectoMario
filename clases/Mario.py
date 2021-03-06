from clases.control.Base import *
from clases.control.Corazon import *
from clases.control.Controlador import Controlador
from clases.control.Suma_Corazon import Suma
from clases.control.Moneda_Control import Moneda_c
from clases.control.texto_final import TextoFinal
from clases import *

import pygame

ancho = 1280
alto = 720

class Mario(Base):

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

        self.movimientos_invisibles = ("imagenes/mario/invisible/mario_invisible.png",
                                       "imagenes/mario/invisible/mario_correr_invisible.png",
                                       "imagenes/mario/invisible/mario_turbio_invisible.png",
                                       "imagenes/mario/invisible/mario_movimiento_invisible.png",
                                       "imagenes/mario/invisible/mario_salto_invisible.png",
                                       "imagenes/invisiblex.png", "imagenes/mario/mario_muerto.png",
                                        "imagenes/mario/mario_bandera.png",)

        self.movimientos_muy_invisibles = ("imagenes/mario/invisible/mario_invisible2.png",
                                       "imagenes/mario/invisible/mario_correr_invisible2.png",
                                       "imagenes/mario/invisible/mario_turbio_invisible2.png",
                                       "imagenes/mario/invisible/mario_movimiento_invisible2.png",
                                       "imagenes/mario/invisible/mario_salto_invisible2.png",
                                        "imagenes/invisiblex.png", "imagenes/mario/mario_muerto.png",
                                        "imagenes/mario/mario_bandera.png",)
        self.frame = 0
        self.maximo = 0
        self.salto = False
        self.bajando = False

        self.inmune = False
        self.frame_inmune = 0
        self.invisible = None
        self.frame_invisible = 0

        self.rebote = False

        self.monedas = 0
        self.tiempo = 0
        self.puntos_mastil = 0
        self.cantidad_signo = 0
        self.cantidad_goombas = 0

        self.vidas = 3
        self.muerto = False
        self.animacion = False
        self.frame_caida = 0
        self.flanco = False

        self.terminado = False
        self.prohibir_mastil = False
        self.animacion_castillo = False
        self.caminata_final = False
        self.frame_caida = None
        self.numero_control = 0

        self.permitir_derecha = False
        self.permitir_izquierda = False
        self.permitir_salto = False
        self.salto_permitido = False

        Base.sprites_principales.add(self)

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

        if self.mover_pantalla() is False and self.permitir_derecha:
            self.rect.x += velocidad

    def cambiarme_angulo(self):
        self.invertir()
        self.estado = 0

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

    def invertir(self):

        self.image = pygame.transform.flip(self.image, True, False)
        self.image = pygame.transform.scale(self.image, (self.ancho, self.alto))

    def cambiar_sprite(self, estado):

        if self.inmune:
            if self.invisible == 0:
                self.image = pygame.image.load(self.movimientos_invisibles[estado])
                self.image = pygame.transform.scale(self.image, (self.ancho, self.alto))
                if self.direccion is False:
                    self.invertir()
            else:
                self.image = pygame.image.load(self.movimientos_muy_invisibles[estado])
                self.image = pygame.transform.scale(self.image, (self.ancho, self.alto))
                if self.direccion is False:
                    self.invertir()
        else:
            self.image = pygame.image.load(self.movimientos[estado])
            self.image = pygame.transform.scale(self.image, (self.ancho, self.alto))
            if self.direccion is False:
                self.invertir()
        if estado == 7:
            self.image = pygame.transform.scale(self.image, (self.ancho - 30, self.alto - 10))

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
                self.rect.y -= 10
            else:
                self.rect.y -= 15

        if self.bajando:
            self.rect.y += 15

        if self.bajo_tierra() and self.flanco is False:
            self.permitir_derecha = False
            self.permitir_izquierda = False
            self.perder_vida(frames_totales, 645)

        self.colisiones_con_salto(frames_totales)

    def colisiones_con_salto(self, frames_totales):

        if self.colision_piso():
            self.terminar_salto()

        tuberia = self.colision(Base.tuberias)
        if tuberia is not False:
            self.colision_tuberia_salto(tuberia)

        escalera = self.colision(Base.escalera)
        if escalera is not False:
            self.colision_escalera_salto(escalera)

        if self.inmune is False and self.bajando:
            goomba = self.colision(Base.goombas)
            if goomba is not False:
                if goomba.muerto is False:
                    goomba.morir(frames_totales, self)
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
                            objeto.activar_tocado(self)
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
            if bloque.rect.y >= self.rect.y + 80:
                self.terminar_salto()
                self.detenerse_bloque(bloque, 95)
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
            self.salto_permitido = False

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
            self.cambiar_sprite(4)

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

        piso = self.colision(Base.piso)

        if self.colision(Base.piso) is False:
            return False
        if self.rect.y <= piso.rect.y - 80:
            self.rect.y = piso.rect.y - 95
            return True

    def colision_tuberia(self, tuberia):

        if tuberia.rect.x > self.rect.x:
            self.rect.x = tuberia.rect.x - 95
        else:
            self.rect.x = tuberia.rect.x + 150

    def colision_tuberia_salto(self, tuberia):

        #Está subiendo?
        if self.bajando is False:
            if self.rect.x - 120 >= tuberia.rect.x or self.rect.x + 60 <= tuberia.rect.x:

                #Está a la derecha del bloque?
                if self.rect.x >= tuberia.rect.x:
                    self.rect.x = tuberia.rect.x + 150

                #Está a la izquierda del bloque?
                elif self.rect.x < tuberia.rect.x:
                    self.rect.x = tuberia.rect.x - 95

        else:
            self.colision_tuberia_caida(tuberia)

    def colision_tuberia_caida(self, tuberia):

            # Chocó estando sobre el bloque?
            if self.rect.x - 120 <= tuberia.rect.x and self.rect.x + 60 >= tuberia.rect.x:
                if tuberia.rect.y >= self.rect.y + 80:
                    self.terminar_salto()
                    self.detenerse_bloque(tuberia, 92)
                return False

            #Chocó estando fuera de la hitbox?
            else:
                if self.rect.x > tuberia.rect.x:
                    self.rect.x = tuberia.rect.x + 150
                elif self.rect.x < tuberia.rect.x:
                    self.rect.x = tuberia.rect.x - 95
                return True

    def colision_escalera(self, escalera):

        escalera2 = False

        if self.bajando is False:

            if escalera in Base.escaleras:
                escalera2 = self.colision(Base.escaleras2)
            else:
                escalera2 = self.colision(Base.escaleras)

            if escalera2 is not False:
                if escalera2.rect.x > escalera.rect.x:
                    escalera = escalera2


        if escalera is not False and escalera2 is not False:
            if escalera.rect.x > self.rect.x:
                self.rect.x = escalera.rect.x - 100
            else:
                self.rect.x = escalera.rect.x + 70
            return True

        if self.colision_escalera_caida() is False:
            return True

        return False

    def colision_escalera_salto(self, escalera):

        if self.bajando is False:

            if self.rect.x + 75 <= escalera.rect.x or self.rect.x - 45 >= escalera.rect.x:
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

        if escalera in Base.escaleras:
            escalera2 = self.colision(Base.escaleras2)
        else:
            escalera2 = self.colision(Base.escaleras)

        if escalera2 is not False:
            if escalera2.rect.x < escalera.rect.x:
                escalera = escalera2

        #Caí sobre la escalera?
        if self.rect.x + 75 >= escalera.rect.x and self.rect.x - 45 <= escalera.rect.x:
            if escalera.rect.y >= self.rect.y + 80:
                self.terminar_salto()
                self.detenerse_bloque(escalera, 98)
            return False

        elif self.bajando:

            #Está a la derecha del bloque?
            if self.rect.x >= escalera.rect.x:
                self.rect.x = escalera.rect.x + 70
            #Está a la izquierda del bloque?
            elif self.rect.x < escalera.rect.x:
                self.rect.x = escalera.rect.x - 100
            return True

    def colision_goomba(self, goomba):
        goomba.achicar()
        self.rebote = True

    def verificar_inmunidad(self, frames_totales):
        #Si es inmune
        if self.inmune and self.muerto is False:
            #Ya termina la inmunidad?
            if self.frame_inmune + 100 < frames_totales:
                self.inmune = False
                #self.cambiar_sprite(0)
            #Tengo que actualizar el titileo?
            elif self.frame_invisible + 15 < frames_totales:
                if self.invisible == 0:
                    self.invisible = 1
                else:
                    self.invisible = 0
                self.frame_invisible = frames_totales
                if self.salto:
                    self.cambiar_sprite(4)

    def empiezo_inmunidad(self, frames_totales):
        self.inmune = True
        self.frame_inmune = frames_totales
        self.invisible = 0
        self.frame_invisible = self.frame_inmune
        self.cambiar_sprite(0)

    def inicializar_vidas(self):

        for i in range(self.vidas):
            vida = Corazon()
        moneda = Moneda_c()

    def perder_vida(self, frames_totales, cantidad):

        self.vidas -= 1

        Controlador.quitar_corazones()

        if self.vidas == 0:
            self.muerte(cantidad)
            self.cambiar_sprite(6)
            self.animacion = True

        if self.muerto is False:

            if self.bajando is False:
                self.empiezo_inmunidad(frames_totales)

            elif self.bajando and self.flanco is False and self.salto is False:
                self.flanco = True
                self.frame_caida = frames_totales

            elif self.bajando and self.flanco is False and self.salto:
                self.flanco = True
                self.frame_caida = frames_totales


        #TODO llamar a funcion inicializar_vidas cuando se sume una vida, si se suma

    def detenerse(self):
        if self.detenido is False:
            self.detenido = True
        if self.salto is False:
            self.cambiar_sprite(0)

    def muerte(self, cantidad):

        self.muerto = True
        self.maximo = self.rect.y - cantidad
        self.bajando = False

    def animacion_muerte(self):

        if self.animacion:

            if self.maximo == self.rect.y:
                self.bajando = True

            if self.bajando is False:
                if self.rect.y <= self.maximo + 60:
                    self.rect.y -= 10
                else:
                    self.rect.y -= 15

            if self.bajando is True:
                self.rect.y += 15

            if self.bajo_tierra() and self.bajando:
                self.animacion = False

    def bajo_tierra(self):
        if self.rect.y > 1000:
            return True
        return False

    def verificar_flanco(self, frames_totales):

        if self.flanco and self.frame_caida + 60 < frames_totales:

            self.buscar_reaparicion()
            self.empiezo_inmunidad(frames_totales)
            self.flanco = False
            self.salto_permitido = False

    def colision_piso_caida(self):
        piso = self.colision(Base.piso)
        if piso is not False:
            if self.rect.x > piso.rect.x:
                if self.rect.y > piso.rect.y - 75:
                    self.rect.x = piso.rect.x + 80

    def animacion_final_bandera(self, frames_totales, velocidad):

        for item in Base.bandera:
            bandera = item
        for item in Base.mastil:
            mastil = item

        #La bandera está sobre Mario?

        if bandera.rect.y - 40 < self.rect.y:
            bandera.rect.y += velocidad

        #La bandera está abajo de Mario?
        elif bandera.rect.y > self.rect.y + 15:
            self.rect.y += 15

        #La bandera está similar a Mario?
        else:
            bandera.rect.y -= velocidad
            self.rect.y += velocidad

        if self.colision(Base.escalera):
            self.terminado = False
            self.prohibir_mastil = True
            self.rect.x += 65
            self.rect.y = mastil.rect.y + 340
            self.invertir()
            self.image = pygame.transform.scale(self.image, (self.ancho - 30, self.alto - 10))
            self.salto = False
            self.bajando = False
            self.caminata_final = True
            self.frame_caida = frames_totales

    def animacion_final_caminata(self, frames_totales, fondo):
        if self.numero_control == 3:
            self.rect.y += 65
        if self.numero_control < 40:
            if self.mover_pantalla():
                Controlador.mover_pantalla(fondo, self)
            self.mover_derecha(5, frames_totales)
        if self.numero_control == 40:
            self.detenerse()
        if self.numero_control == 70:
            Base.colegio.image = pygame.image.load("imagenes/colegio_tori.png")
            Base.colegio.image = pygame.transform.scale(Base.colegio.image, (Base.colegio.ancho, Base.colegio.alto))
        if self.numero_control == 120:
            t = TextoFinal(Base.colegio.rect.x - 300, Base.colegio.rect.y + 80)
        if self.numero_control == 350:
            return True
        return False

    def animacion_final(self, frames_totales, fondo):
        if self.terminado:
            self.animacion_final_bandera(frames_totales, 8)
        if self.caminata_final:
            if self.frame_caida + 30 < frames_totales:
                if self.animacion_final_caminata(frames_totales, fondo) is False:
                    self.numero_control += 1
                else:
                    return True
        return False

    def mastil_tocado(self, mastil):
        if self.rect.y > mastil.rect.y - 120 and self.rect.y < mastil.rect.y + 350:
            if mastil.tocado is None:
                mastil.tocado = self.rect.y
                self.puntos_mastil = 550 - self.rect.y
                self.terminado = True
                self.animacion_castillo = True
                self.cambiar_sprite(7)
                self.rect.x = mastil.rect.x - 55

    def buscar_reaparicion(self):

        self.rect.y = 600
        self.rect.x = 50
        while self.rect.x < 1000:
            if self.colision_piso():
                piso = self.colision(Base.piso)
                self.rect.x = piso.rect.x
                return
            else:
                self.rect.x += 10

    def agarrar_hongo(self, hongo, frames_totales):

        self.vidas += 1
        c = Suma(self.rect.x + 100, self.rect.y - 50)
        c.frame = frames_totales
        for vida in Base.corazon:
            Base.corazon.remove(vida)
            Base.sprites.remove(vida)
        self.inicializar_vidas()
        Base.hongos.remove(hongo)
        Base.sprites.remove(hongo)
