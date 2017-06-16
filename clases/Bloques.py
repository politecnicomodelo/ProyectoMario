import pygame
from pygame.locals import *

ancho = 1360
alto = 768

class Bloque(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("imagenes/bloque.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = ancho/6
        self.rect.centery = alto/3