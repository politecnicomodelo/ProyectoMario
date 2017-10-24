from clases.control.Base import *

class Moneda(Base):

    def __init__(self, x, y, movible):

        Base.__init__(self, x, y, 40, 40, "imagenes/monedas/inicial.png")
        Base.sprites.add(self)
        Base.monedas.add(self)

        self.bajando = None
        self.proceso = None
        self.movible = movible
        if self.movible:
            self.frame = 0
            self.estado = 0
            self.animaciones = ("imagenes/monedas/1.png", "imagenes/monedas/2.png",
                                "imagenes/monedas/3.png", "imagenes/monedas/inicial.png",)

    def activar_movimiento(self):
        self.proceso = True
        self.bajando = False
        self.original = self.rect.y

    def terminar_movimiento(self):
        self.proceso = False
        Base.monedas.remove(self)
        Base.sprites.remove(self)
        #TODO: Sumar uno a las monedas de Mario

    def movimiento(self):

        if self.bajando:
            self.rect.y += 12

        elif self.rect.y + 180 == self.original:
            self.bajando = True
        else:
            self.rect.y -= 12

        if self.rect.y == self.original - 48 and self.bajando:
            self.terminar_movimiento()

    def agarrada(self):

        Base.sprites.remove(self)
        Base.monedas.remove(self)

    def animacion(self, frames_totales):

        if frames_totales - self.frame > 8:

            if self.estado >= 0 and self.estado <= 2:
                self.estado += 1
                self.frame = frames_totales
                self.cambiar_sprite(self.animaciones[self.estado])

            elif self.estado == 3:
                self.estado = 1
                self.frame = frames_totales
                self.cambiar_sprite(self.animaciones[self.estado])

    def cambiar_sprite(self, movimiento):
        self.image = pygame.image.load(movimiento)
        self.image = pygame.transform.scale(self.image, (self.ancho, self.alto))
