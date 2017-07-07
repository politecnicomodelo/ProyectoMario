import pygame
from pygame.locals import *

ancho = 1360
alto = 768

class Bloque(pygame.sprite.Sprite):
    def __init__(self, centrox, centroy):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("imagenes/bloque.png")
        self.image = pygame.transform.scale(self.image, (73, 71))
        self.rect = self.image.get_rect()
        self.rect.centerx = centrox
        self.rect.centery = centroy