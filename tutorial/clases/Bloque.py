from tutorial.clases.Base import Base

class Bloque(Base):

    def __init__(self, x, y):

        Base.__init__(self, x, y, 75, 75, "imagenes/bloques.png")

        Base.sprites.add(self)
        Base.bloques.add(self)