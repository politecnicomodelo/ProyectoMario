import pygame
from pygame.locals import *

ancho = 1360
alto = 768

class Piso(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("imagenes/piso.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = ancho/2
        self.rect.centery = 570
