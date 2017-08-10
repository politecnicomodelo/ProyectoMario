import pygame
from pygame.locals import *
from .Hongos import Hongo
from .Monedas import Moneda
import time
import _thread

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

    def moverSigno(self):
        self.image = pygame.image.load("imagenes/signotocado.png")
        self.image = pygame.transform.scale(self.image, (73, 71))
        self.rect.y-=2
        time.sleep(0.5)
        self.rect.y+=2

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
                    _thread.start_new_thread(moneda.matarMoneda, (Activos,))
                    _thread.start_new_thread(self.moverSigno, ())