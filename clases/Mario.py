import sys
import time
import pygame
from .Bloques import Bloque
from pygame.locals import *

ancho = 640
alto = 360

class Mario(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("imagenes/marioder.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = ancho-500
        self.rect.centery = alto-50

    def mover(self, keys):
        self.image = pygame.image.load("imagenes/marioder.png")
        if keys[K_UP]:
            self.image = pygame.image.load("imagenes/mariosalta.png")
            self.rect.y -= 2

        if keys[K_DOWN]:
            self.rect.y += 2

        if self.rect.right <= ancho:
             if keys[K_RIGHT]:
                self.image = pygame.image.load("imagenes/mariocorreder.png")
                self.rect.x += 2

        if self.rect.left >=0:
            if keys[K_LEFT]:
                self.image = pygame.image.load("imagenes/mariocorreizq.png")
                self.rect.x -= 2