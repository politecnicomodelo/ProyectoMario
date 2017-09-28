from clases.Bloques import *

class Ladrillo(Bloque):

    def __init__(self, x, y, posicion):
        Bloque.__init__(self, x, y, "imagenes/bloque.png")

        Base.sprites.add(self)
        Base.bloques.add(self)
        if posicion:
            Base.ladrillos.add(self)
        if posicion is False:
            Base.ladrillos2.add(self)