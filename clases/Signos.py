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

    def devuelve(self, Mario, esHongo, esMoneda, Activos):
        Toco=False
        if not Toco:
            if self.rect.colliderect(Mario):
                Toco=True
                self.rect.y-=1
                if esHongo==True:
                    hongo=Hongo()
                    hongo.add(Activos)
                elif esMoneda==True:
                    moneda=Moneda(self)
                    moneda.add(Activos)
                self.image = pygame.image.load("imagenes/signotocado.png")
                self.image = pygame.transform.scale(self.image, (73, 71))
                self.rect.y+=1