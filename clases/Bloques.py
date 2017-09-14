import pygame
import time
import _thread
from .Base import *

ancho = 1280
alto = 720

class Bloque(pygame.sprite.Sprite):

    def __init__(self, centrox, centroy):

        Base.__init__(self, centrox, centroy, 73, 71, "imagenes/bloque.png")
        Base.sprites.add(self)

    def mueveBloque(self):
        self.image = pygame.transform.scale(self.image, (73, 71))
        self.rect.y-=2
        time.sleep(0.5)
        self.rect.y+=2

    def devuelveBloque(self, Mario):
        if self.rect.collidepoint(Mario.rect.midtop):
            _thread.start_new_thread(self.mueveBloque, ())