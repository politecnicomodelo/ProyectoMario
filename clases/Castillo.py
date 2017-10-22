from clases.control.Base import Base

class Castillo(Base):

    def __init__(self, x):

        Base.__init__(self, x, 195, 800, 500, "imagenes/colegio_tori.png")
        Base.colegio = self
        Base.sprites.add(self)