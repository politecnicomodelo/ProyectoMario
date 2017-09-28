from clases import Base

class Tuberia(Base):

    def __init__(self, x, y, ancho, alto, ruta):

        Base.__init__(x, y, ancho, alto, ruta)
        Base.sprites.add(self)
        Base.tuberias.add(self)