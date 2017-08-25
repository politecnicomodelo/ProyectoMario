import pygame
from pygame.locals import *
import _thread
import time

ancho = 1360
alto = 768

ListaSpritesDer=["imagenes/mario/mariocorreder1.png", "imagenes/mario/mariocorreder2.png"]
ListaSpritesIzq=["imagenes/mario/mariocorreizq1.png", "imagenes/mario/mariocorreizqr2.png"]

class Mario(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("imagenes/mario/marioder.png")
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.x = ancho-1300
        self.rect.y = 600

    def mover(self, keys, muevePantalla, Activos, Pisos):

        self.image=pygame.image.load("imagenes/mario/marioder.png")
        self.image = pygame.transform.scale(self.image, (100, 100))

        if self.rect.x<680:
                muevePantalla=False

                if keys[K_UP]:
                    _thread.start_new_thread(self.saltoDerecha, (Activos, Pisos,))

                if keys[K_DOWN]: #NO EXISTE, PRUEBA
                    self.rect.y += 30

                if keys[K_RIGHT]:
                    self.image = pygame.image.load("imagenes/mario/mariocorreder2.png")
                    self.image = pygame.transform.scale(self.image, (100, 100))
                    self.rect.x += 30

                if self.rect.left >= 0:
                    if keys[K_LEFT]:
                        self.image = pygame.image.load("imagenes/mario/mariocorreizqr2.png")
                        self.image = pygame.transform.scale(self.image,(100, 100))
                        self.rect.x -= 30

        else:
            self.image = pygame.image.load("imagenes/mario/marioder.png")
            self.image = pygame.transform.scale(self.image, (100, 100))
            muevePantalla = False
            if keys[K_RIGHT]:
                self.image = pygame.image.load("imagenes/mario/mariocorreder2.png")
                self.image = pygame.transform.scale(self.image, (100, 100))
                muevePantalla=True

            if keys[K_LEFT]:
                self.image = pygame.image.load( "imagenes/mario/mariocorreizqr2.png")
                self.image = pygame.transform.scale(self.image, (100, 100))
                self.rect.x -= 30

            if keys[K_UP]:
                _thread.start_new_thread(self.saltoDerecha, (Activos, Pisos,))

            if keys[K_DOWN]: #NO EXISTE, PRUEBA
                self.rect.y += 30

        return muevePantalla

    def saltoDerecha(self, Activos, Pisos):
        if self.rect.x < 1100:
            self.image = pygame.image.load("imagenes/mario/mariosalta.png")
            self.image = pygame.transform.scale(self.image, (100, 100))
            x=0
            while x < 45:
                self.rect.y -= 1
                self.rect.x += 0.5
                time.sleep(0.1)
                x+=1
            while pygame.sprite.spritecollideany(self, Pisos, collided = None) == None:
                self.rect.y += 40
                self.rect.x += 30
                time.sleep(0.1)

    def saltoIzquierda(self, Activos, Pisos):
        if self.rect.x < 1100:
            self.image = pygame.image.load("imagenes/mario/mariosalta.png")
            self.rect.y -= 37.5
            self.rect.x -= 12.5
            time.sleep(0.00001)
            self.rect.y -= 37.5
            self.rect.x -= 12.5
            time.sleep(0.00001)
            while pygame.sprite.spritecollideany(self, Pisos, collided = None) == None:
                self.rect.y += 25
                self.rect.x -= 12.5
                time.sleep(0000.1)