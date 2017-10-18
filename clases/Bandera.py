from clases.control.Base import *

class Bandera(Base):

    def __init__(self, x):

        Base.__init__(self, x, 210, 75, 60, "imagenes/banderita.png")

        Base.sprites.add(self)
        Base.bandera.add(self)