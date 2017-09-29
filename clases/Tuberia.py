from clases import Base

class Tuberia(Base):

    def __init__(self, x, y, alto):

        if alto == 1:
            alto = "imagenes/tuberias/chica.png"

        Base.__init__(self, x, y, 156, 158, alto)
        Base.sprites.add(self)
        Base.tuberias.add(self)