from clases.control.Base import *

class Escalera(Base):

    def __init__(self, x, y, posicion):
        Base.__init__(self, x, y, 75, 75, "imagenes/escalera.png")

        Base.sprites.add(self)
        Base.escalera.add(self)
        if posicion:
            Base.escaleras.add(self)
        else:
            Base.escaleras2.add(self)
