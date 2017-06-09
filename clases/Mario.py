import sys
import time
import pygame
from pygame.locals import *

ancho = 1080
alto = 720

class Mario(pygame.sprite.Sprite):
    tiempoarriba=False
    tiempoabajo=False
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("imagenes/mario.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = ancho-1000
        self.rect.centery = alto-200
        self.speed = [0.5, -0.5]

    def mover(self, keys):

            if tiempoarriba==True:
                self.rect.centery += 10
                tiempoarriba = False

            if tiempoabajo==True:
                self.rect.centery += 10
                tiempoabajo = False

            if keys[K_UP]:
                self.rect.centery -= 10
                tiempoarriba = True

            if keys[K_DOWN]:
                self.rect.centery += 10
                tiempoabajo = True

            if self.rect.right <= ancho:
                if keys[K_RIGHT]:
                    self.rect.centerx += 5

            if self.rect.left >=0:
                if keys[K_LEFT]:
                    self.rect.centerx -= 5