from clases.Bloques import *

class Signo(Bloque):

    def __init__(self, x, y):
        Bloque.__init__(self, x, y, "imagenes/signo.png")

        Base.sprites.add(self)
        Base.bloques.add(self)
        Base.signos.add(self)