import pygame
from pygame.locals import *
import time
import _thread

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

    def mueveBloque(self):
        self.image = pygame.transform.scale(self.image, (73, 71))
        self.rect.y-=2
        time.sleep(0.5)
        self.rect.y+=2

    def devuelveBloque(self, Mario):
        if self.rect.collidepoint(Mario.rect.midtop):
            _thread.start_new_thread(self.mueveBloque, ())