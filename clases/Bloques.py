from clases.control.Base import *

ancho = 1280
alto = 720

class Bloque(Base):

    def __init__(self, x, y, ruta):
        Base.__init__(self, x, y, 75, 75, ruta)
