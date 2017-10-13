from clases.control.Base import *
from clases import *

class Mastil(Base):

    def __init__(self, x, y):

        Base.__init__(self, x, y, 25, 400, "imagenes/poste.png")

        bloque = Escalera(x - 25, 620, True)

        Base.sprites.add(self)