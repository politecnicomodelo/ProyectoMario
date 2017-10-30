from clases.control.Base import Base

class TextoFinal(Base):

    def __init__(self, x, y):
        Base.__init__(self, x, y, 1000, 500, "imagenes/texto.png")

        Base.sprites_principales.add(self)
        Base.texto = self