from clases.Bloques import *
from clases.Monedas import *
from clases.Hongo import *

class Signo(Bloque):

    def __init__(self, x, y, tipo):
        Bloque.__init__(self, x, y, "imagenes/signo.png")

        Base.sprites_principales.add(self)
        Base.bloques.add(self)
        Base.signos.add(self)
        self.bajando = True
        self.original = None
        self.proceso = False
        self.unico = True
        self.tipo = tipo

    def activar_tocado(self, mario):
        if self.unico:
            self.proceso = True
            self.bajando = False
            self.original = self.rect.y
            self.image = pygame.image.load("imagenes/signotocado.png")
            self.image = pygame.transform.scale(self.image, (self.ancho, self.alto))
            self.unico = False
            if self.tipo == False:
                mario.monedas += 1
            mario.cantidad_signo += 1

    def terminar_tocado(self):
        self.proceso = False

    def tocado(self):
        if self.bajando:
            self.rect.y += 2
        elif self.rect.y + 16 == self.original:
            self.bajando = True
            if self.tipo:
                hongo = Hongo(self.rect.x + 13, self.rect.y + 20)
                hongo.estatico = True
                hongo.direccion = True
            if self.tipo is False:
                moneda = Moneda(self.rect.x + 20, self.rect.y - 35, True)
                moneda.activar_movimiento()
        else:
            self.rect.y -= 2

        if self.rect.y == self.original:
            self.terminar_tocado()