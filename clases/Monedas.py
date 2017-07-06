import pygame
from pygame.locals import *

class Moneda(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("imagenes/Moneda.png")
        self.rect = self.image.get_rect()