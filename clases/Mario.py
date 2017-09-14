from clases.control.Base import *
import pygame

ancho = 1280
alto = 720

movimientos = {"derecha": "imagenes/mario/mario_der.png", "izquierda": "imagenes/mario/mario_izq.png"}

class Mario(Base):

    def __init__(self):

        Base.__init__(self, ancho-1260, 600, 100, 100, "imagenes/mario/mario_der.png")
        self.direccion = True
        Base.sprites.add(self)

    def mover_derecha(self, velocidad):

        if self.direccion is False:
            self.direccion = True
            self.image = self.nuevo_sprite(movimientos["derecha"])

        self.rect.x += velocidad

    def mover_izquierda(self, velocidad):

        if self.direccion is True:
            self.direccion = False
            #self.image = self.nuevo_sprite(movimientos["izquierda"])


        self.rect.x -= velocidad

    def nuevo_sprite(self, movimiento):


