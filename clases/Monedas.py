from clases.control.Base import *


class Moneda(Base):

    def __init__(self, x, y, movible):

        Base.__init__(self, x, y, 40, 40, "imagenes/monedas/inicial.png")
        Base.sprites.add(self)
        Base.monedas.add(self)

        self.bajando = None
        self.proceso = None
        self.movible = movible

    def activar_movimiento(self):
        self.proceso = True
        self.bajando = False
        self.original = self.rect.y

    def terminar_movimiento(self):
        self.proceso = False
        Base.monedas.remove(self)
        Base.sprites.remove(self)
        #TODO: Sumar uno a las monedas de Mario

    def movimiento(self):

        if self.bajando:
            self.rect.y += 15

        elif self.rect.y + 300 == self.original:
            self.bajando = True
        else:
            self.rect.y -= 15

        if self.rect.y == self.original - 60 and self.bajando:
            self.terminar_movimiento()

    def agarrada(self):

        Base.sprites.remove(self)
        Base.monedas.remove(self)
        #TODO: Sumar uno a las monedas de Mario