import pygame
import time
from pygame.locals import *

class Moneda(pygame.sprite.Sprite):
    def __init__(self, padre):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("imagenes/moneda.png")
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect()
        self.rect.x=padre.rect.x+15
        self.rect.y=padre.rect.y-47

    def matarMoneda(self, Activos):
        self.rect.y-=5
        time.sleep(1)
        self.rect.y+=5
        Activos.remove(self)