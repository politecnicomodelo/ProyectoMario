import pygame
from clases.control.Grupo_Sprites import *


class Base(pygame.sprite.Sprite):

    sprites = Sprites()
    piso = Sprites()
    bloques = Sprites()
    ladrillos = Sprites()
    ladrillos2 = Sprites()
    signos = Sprites()
    monedas = Sprites()
    tuberias = Sprites()
    escaleras = Sprites()
    escaleras2 = Sprites()
    escalera = Sprites()
    goombas = Sprites()
    corazon = Sprites()
    letras = Sprites()
    mastil = Sprites()
    bandera = Sprites()

    def __init__(self, x, y, ancho, alto, ruta):

        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(ruta)
        self.image = pygame.transform.scale(self.image, (ancho, alto))

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.ancho = ancho
        self.alto = alto