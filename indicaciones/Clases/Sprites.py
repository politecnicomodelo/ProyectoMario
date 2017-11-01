from .Base import *

class Sprite(Base):

    def __init__(self, x, y, ancho, alto, ruta):
        Base.__init__(self, x, y, ancho, alto, ruta)

    def Animacion_Corazones(self, frames_totales, ventana):
        if self.rect.x <= 750:
            self.rect.x += 6
        if frames_totales % 5 == 0 and self.ancho > 0 and self.alto > 0:
            self.ancho -= 1
            self.alto -= 1
            self.image = pygame.transform.scale(self.image, (self.ancho, self.alto))
            self.image = pygame.image.load("corazon_invertido.png")
            self.ancho -= 1
            self.alto -= 1
            self.image = pygame.image.load("Corazon.png")
            self.image = pygame.transform.scale(self.image, (self.ancho, self.alto))
        if self.rect.x > 750:
            self.rect.y -= 6
            self.rect.x += 2

    def Animacion_Monedas(self, posx, posy):
        self.rect.y -= 15
        if self.rect.y < 250:
            self.rect.x += 30
        else:
            self.rect.x += 25
        if self.rect.x > 750 and self.rect.y < 200:
            self.rect.x = posx
            self.rect.y = posy
            return True