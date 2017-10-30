from clases.control.Base import *
from clases.Bandera import Bandera
from clases.Escaleras import Escalera
from clases.Castillo import Castillo

class Mastil(Base):

    def __init__(self, x):

        Base.__init__(self, x, 190, 25, 430, "imagenes/poste.png")

        escalera = Escalera(x - 25, 620, True)
        bandera = Bandera(self.rect.x - 65)
        castillo = Castillo(self.rect.x + 250)
        self.tocado = None

        Base.sprites.add(self)
        Base.mastil.add(self)