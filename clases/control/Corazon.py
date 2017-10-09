from clases.control.Base import Base

class Corazon(Base):

    def __init__(self):

        Base.__init__(self, 40, 40, 60, 53, "imagenes/corazon.png")

        Base.sprites.add(self)

        self.rect.x = self.proxima_posicion()

        Base.corazon.add(self)

    def proxima_posicion(self):

        maximo = 0
        if Base.corazon.sprites() == []:
            return 40
        for corazon in Base.corazon:
            if corazon.rect.x > maximo:
                maximo = corazon.rect.x
        return maximo + 70
