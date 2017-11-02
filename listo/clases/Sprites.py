from .Base import *

class Sprites(Base):

    def __init__(self, x, y, ancho, alto, ruta):
        Base.__init__(self, x, y, ancho, alto, ruta)

        self.image = pygame.image.load(ruta)
        self.image = pygame.transform.scale(self.image, (ancho, alto))

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.ancho = ancho
        self.alto = alto