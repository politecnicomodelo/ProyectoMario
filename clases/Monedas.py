from clases.control.Base import *


class Moneda(Base):

    def __init__(self, x, y, movible):

        Base.__init__(self, x, y, 40, 40, "imagenes/moneda.png")
        Base.sprites.add(self)
        Base.monedas.add(self)

        self.bajando = None
        self.proceso = None
        self.movible = movible

    def activar_movimiento(self):
        self.proceso = True
        self.bajando = False
        self.original = self.rect.y - 40

    def terminar_movimiento(self):
        self.proceso = False
        Base.monedas.remove(self)
        Base.sprites.remove(self)

    def movimiento(self):
        if self.bajando:
            self.rect.y += 8

        elif self.rect.y + 160 == self.original:
            self.bajando = True
        else:
            self.rect.y -= 8

        if self.rect.y == self.original + 40:
            self.terminar_movimiento()