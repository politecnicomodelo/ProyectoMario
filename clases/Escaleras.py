from clases.control.Base import *

class Escalera(Base):

    def __init__(self, x, y):
        Base.__init__(self, x, y, 75, 75, "imagenes/escalera.png")

        Base.sprites.add(self)
        Base.escaleras.add(self)