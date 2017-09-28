from clases.Bloques import *

class Signo(Bloque):

    def __init__(self, x, y):
        Bloque.__init__(self, x, y, "imagenes/signo.png")

        Base.sprites.add(self)
        Base.bloques.add(self)
        Base.signos.add(self)
        self.bajando = True
        self.original = None

    def tocado(self):
        if self.rect.y - 30 == self.original:
            self.bajando = True
        if self.bajando is False:
            self.rect.y -= 10
        else:
            self.rect.y += 10