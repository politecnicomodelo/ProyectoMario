from tutorial.clases.Base import *

class Moneda(Base):

    def __init__(self, x, y, identificador):

        Base.__init__(self, x, y, 40, 40, "imagenes/monedas/inicial.png")
        self.identificador = identificador
        Base.sprites.add(self)
        Base.monedas.add(self)

    def agarrada(self):

        Base.sprites.remove(self)
        Base.monedas.remove(self)
