import pygame
from pygame.locals import *
from .Hongos import Hongo
from .Monedas import Moneda

ancho = 1360
alto = 768

class Signo(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("imagenes/signo.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = ancho/6
        self.rect.centery = alto/3

    def devuelve(self, Mario):
        esHongo=False
        esMoneda=False
        if self.rect.colliderect(Mario):
            self.rect.y-=3
            if esHongo==True:
                hongo=Hongo()
            elif esMoneda==True:
                moneda=Moneda()
            self.image = pygame.image.load("imagenes/signoTocado.png")
            return