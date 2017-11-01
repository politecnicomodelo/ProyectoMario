import pygame

class Base(pygame.sprite.Sprite):

    sprites = pygame.sprite.Group()
    monedas = pygame.sprite.Group()
    piso = pygame.sprite.Group()
    bloques = pygame.sprite.Group()
    letras = pygame.sprite.Group()

    def __init__(self, x, y, ancho, alto, ruta):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(ruta)
        self.image = pygame.transform.scale(self.image, (ancho, alto))

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.ancho = ancho
        self.alto = alto