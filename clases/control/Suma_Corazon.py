from clases.control.Base import Base

class Suma(Base):

    def __init__(self, x, y):

        Base.__init__(self, x, y, 55, 42, "imagenes/+1.png")

        Base.sprites_principales.add(self)
        self.frame = None

    def desaparecer(self, frames_totales):

        if self.frame + 60 < frames_totales:
            Base.sprites_principales.remove(self)