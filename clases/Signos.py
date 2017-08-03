import pygame
from pygame.locals import *
from .Hongos import Hongo
from .Monedas import Moneda

ancho = 1360
alto = 768

class Signo(pygame.sprite.Sprite):

    def __init__(self, centrox, centroy):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("imagenes/signo.png")
        self.image = pygame.transform.scale(self.image, (73, 71))
        self.rect = self.image.get_rect()
        self.rect.centerx = centrox
        self.rect.centery = centroy

    def devuelve(self, Mario, esHongo, esMoneda, Activos, Monedas):
        Toco=False
        if not Toco:
            if self.rect.collidepoint(Mario.rect.midtop):
                Toco=True
                if esHongo==True:
                    hongo=Hongo()
                    hongo.add(Activos)
                elif esMoneda==True:
                    Monedas+=1
                    moneda=Moneda(self)
                    moneda.add(Activos)
                self.image = pygame.image.load("imagenes/signotocado.png")
                self.image = pygame.transform.scale(self.image, (73, 71))