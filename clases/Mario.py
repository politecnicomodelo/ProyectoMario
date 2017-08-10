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
        self.image = pygame.transform.scale(self.image, (90, 90))
        self.rect = self.image.get_rect()
        self.rect.centerx = ancho-1300
        self.rect.centery = 630

    def mover(self, keys, muevePantalla, Activos):

        self.image=pygame.image.load("imagenes/mario/marioder.png")
        Sprite=None

        if self.rect.x<680:
            muevePantalla=False

            if keys[K_UP]:
                self.image = pygame.image.load("imagenes/mario/mariosalta.png")
                self.rect.y -= 30
                if pygame.sprite.spritecollideany(self,Activos)!=None:
                    Sprite=pygame.sprite.spritecollideany(self, Activos)
                    self.rect.top=Sprite.rect.bottom

            if keys[K_DOWN]:
                self.rect.y += 30
                if pygame.sprite.spritecollideany(self,Activos)!=None:
                    Sprite=pygame.sprite.spritecollideany(self, Activos)
                    self.rect.bottom=Sprite.rect.top

            contador1=0

            if keys[K_RIGHT]:
                self.image =self.spriteMario(contador1, ListaSpritesDer)
                self.rect.x += 30
                if pygame.sprite.spritecollideany(self,Activos)!=None:
                    Sprite=pygame.sprite.spritecollideany(self, Activos)
                    self.rect.right=Sprite.rect.left

            contador2=0
            if self.rect.left >= 0:
                if keys[K_LEFT]:
                    self.image =self.spriteMario(contador2, ListaSpritesIzq)
                    self.rect.x -= 30
                    if pygame.sprite.spritecollideany(self, Activos) != None:
                        Sprite = pygame.sprite.spritecollideany(self, Activos)
                        self.rect.left = Sprite.rect.right

        else:
            self.image = pygame.image.load("imagenes/mario/marioder.png")
            muevePantalla = False
            contador1=0
            contador2=0
            if keys[K_RIGHT]:
                self.image =self.spriteMario(contador1, ListaSpritesDer)
                muevePantalla=True

            if keys[K_LEFT]:
                self.image = self.spriteMario(contador2, ListaSpritesIzq)
                self.rect.x -= 30

            if keys[K_UP]:
                self.image =pygame.image.load("imagenes/mario/mariosalta.png")
                self.rect.y -= 30

            if keys[K_DOWN]:
                self.rect.y += 30

        return muevePantalla

    def spriteMario(self, contador, Lista):
        if contador != 0:
            contador+=1
        if contador >= len(Lista):
            contador=0
        return pygame.image.load(Lista[contador])