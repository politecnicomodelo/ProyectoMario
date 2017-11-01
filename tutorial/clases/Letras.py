from tutorial.clases.Base import *

class Letra(Base):

    def __init__(self, x, y, ruta):

        Base.__init__(self, x, y, 50, 70, ruta)

        Base.letras.add(self)