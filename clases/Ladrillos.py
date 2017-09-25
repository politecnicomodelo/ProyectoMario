from clases.Bloques import *

class Ladrillo(Bloque):

    def __init__(self, x, y):
        Bloque.__init__(self, x, y, "imagenes/bloque.png")

        Base.sprites.add(self)
        Base.bloques.add(self)