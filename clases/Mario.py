import pygame
from pygame.locals import *

ancho = 1360
alto = 768

ListaSpritesDer=["imagenes/mario/mariocorreder1.png", "imagenes/mario/mariocorreder2.png"]
ListaSpritesIzq=["imagenes/mario/mariocorreizq1.png", "imagenes/mario/mariocorreizqr2.png"]

class Mario(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("imagenes/mario/marioder.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = ancho-1300
        self.rect.centery = alto-200

    def mover(self, keys, objpiso, objcubo):

        self.image = pygame.image.load("imagenes/mario/marioder.png")
        if keys[K_UP] and not self.rect.colliderect(objcubo):
            self.image = pygame.image.load("imagenes/mario/mariosalta.png")
            self.rect.y -= 10

        if keys[K_DOWN] and not self.rect.colliderect(objpiso):
             self.rect.y += 10

        contador=0
        if self.rect.right <= ancho:
             if keys[K_RIGHT]:
                self.image = pygame.image.load(ListaSpritesDer[contador])
                contador += 1
                if contador>len(ListaSpritesDer):
                    contador=0
                self.rect.x += 10

        if self.rect.left >=0:
            if keys[K_LEFT]:
                self.rect.x -= 10
