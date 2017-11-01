from .Base import *


class Letra(Base):

    def __init__(self, x, y, ancho, alto, ruta, tipo):

        Base.__init__(self, x, y, ancho, alto, ruta)

        self.maximo = y - 25
        self.minimo = y + 25

        self.subiendo = False
        self.bajando = False

        self.velocidad = 3

        Base.sprites.add(self)
        if tipo is False:
            Base.letras_pasivas.add(self)