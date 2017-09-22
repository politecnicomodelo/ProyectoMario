from clases.control.Base import *

ancho = 1280
alto = 720

class Bloque(Base):

    def __init__(self, centrox, centroy):

        Base.__init__(self, centrox, centroy, 73, 71, "imagenes/bloque.png")

        Base.sprites.add(self)
        Base.bloques.add(self)