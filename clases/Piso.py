import pygame
from pygame.locals import *

ancho = 1280
alto = 720

class Piso(pygame.sprite.Sprite):
    def __init__(self, x, y, imagen):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(imagen)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
