import pygame
from pygame.locals import *

class Hongo(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("imagenes/hongo.png")
        self.rect = self.image.get_rect()