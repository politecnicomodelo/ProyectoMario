from clases.Bloques import *
from clases.Monedas import *
from clases.Hongo import *

class Signo(Bloque):

    def __init__(self, x, y):
        Bloque.__init__(self, x, y, "imagenes/signo.png")

        Base.sprites.add(self)
        Base.bloques.add(self)
        Base.signos.add(self)
        self.bajando = True
        self.original = None
        self.proceso = False
        self.unico = True
        self.tipo = True

    def activar_tocado(self):
        if self.unico:
            self.proceso = True
            self.bajando = False
            self.original = self.rect.y
            self.image = pygame.image.load("imagenes/signotocado.png")
            self.image = pygame.transform.scale(self.image, (self.ancho, self.alto))
            self.unico = False

    def terminar_tocado(self):
        self.proceso = False

    def tocado(self):
        if self.bajando:
            self.rect.y += 2
        elif self.rect.y + 16 == self.original:
            self.bajando = True
            if self.tipo:
                hongo = Hongo(self.rect.x + 20, self.rect.y - 60)
                hongo.direccion = True
            if self.tipo is False:
                moneda = Moneda(self.rect.x + 20, self.rect.y - 35, True)
                moneda.activar_movimiento()
        else:
            self.rect.y -= 2

        if self.rect.y == self.original:
            self.terminar_tocado()