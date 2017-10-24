from clases.control.Base import Base
import pygame


class Moneda_c(Base):

    def __init__(self):

        Base.__init__(self, 40, 100, 40, 40, "imagenes/monedas/inicial.png")

        Base.sprites_principales.add(self)
        self.cantidad = None