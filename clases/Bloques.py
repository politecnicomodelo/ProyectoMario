import pygame
from pygame.locals import *
ancho = 640
alto = 360
class Bloque(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("imagenes/bloque.jpg")
        self.rect = self.image.get_rect()
        self.rect.centerx = 500
        self.rect.centery = 200