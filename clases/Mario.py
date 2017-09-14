from .Base import *
import _thread
import time

ancho = 1280
alto = 720

ListaSpritesDer=["imagenes/mario/mariocorreder1.png", "imagenes/mario/mariocorreder2.png"]
ListaSpritesIzq=["imagenes/mario/mariocorreizq1.png", "imagenes/mario/mariocorreizqr2.png"]

class Mario(Base):

    def __init__(self):

        Base.__init__(self, ancho-1300, 600, 100, 100, "imagenes/mario/marioder.png")
        Base.sprites.add(self)

    def mover(self, keys, muevePantalla, Activos, Pisos):

        self.image=pygame.image.load("imagenes/mario/marioder.png")
        self.image = pygame.transform.scale(self.image, (100, 100))
        muevePantalla=False
        if keys[pygame.K_UP]:
            _thread.start_new_thread(self.saltoLugar, (Activos,Pisos,))

        if keys[pygame.K_RIGHT] and keys[pygame.K_UP]:
            _thread.start_new_thread(self.saltoDerecha, (Activos, Pisos,))

        if keys[pygame.K_LEFT] and keys[pygame.K_UP]:
            _thread.start_new_thread(self.saltoIzquierda, (Activos, Pisos,))

        if keys[pygame.K_RIGHT]:
            self.image = pygame.image.load("imagenes/mario/mariocorreder2.png")
            self.image = pygame.transform.scale(self.image, (100, 100))
            if self.rect.x < 680:
                 self.rect.x += 30
            else:
                 muevePantalla = True

        if keys[pygame.K_LEFT]:
            if self.rect.left >= 0:
                self.image = pygame.image.load("imagenes/mario/mariocorreizqr2.png")
                self.image = pygame.transform.scale(self.image,(100, 100))
                self.rect.x -= 30

        return muevePantalla

    def saltoLugar(self, Activos, Pisos):
        self.rect.y -= 30
        time.sleep(0.1)
        self.rect.y -= 30
        time.sleep(0.1)
        while pygame.sprite.spritecollideany(self, Pisos, collided=None) == None and \
        pygame.sprite.spritecollideany(self, Activos, collided=None) == None:
            self.rect.y += 30
            time.sleep(0.1)

    def saltoDerecha(self, Activos, Pisos):
        if self.rect.x < 1100:
            self.image = pygame.image.load("imagenes/mario/mariosalta.png")
            self.image = pygame.transform.scale(self.image, (100, 100))
            x=0
            while x<3 and pygame.sprite.spritecollideany(self, Activos, collided=None) == None:
                self.rect.y -= 20
                self.rect.x += 10
                time.sleep(0.1)
                x+=1
            while pygame.sprite.spritecollideany(self, Pisos, collided = None) == None and \
                  pygame.sprite.spritecollideany(self, Activos, collided=None) == None:
                self.rect.y += 20
                self.rect.x += 10
                time.sleep(0.1)

    def saltoIzquierda(self, Activos, Pisos):
        if self.rect.x < 1100:
            self.image = pygame.image.load("imagenes/mario/mariosalta.png")
            self.image = pygame.transform.scale(self.image, (100, 100))
            x=0
            while x<3 and pygame.sprite.spritecollideany(self, Activos, collided=None) == None:
                self.rect.y -= 20
                self.rect.x -= 10
                time.sleep(0.1)
                x+=1
            while pygame.sprite.spritecollideany(self, Pisos, collided = None) == None and \
                  pygame.sprite.spritecollideany(self, Activos, collided=None) == None:
                self.rect.y += 20
                self.rect.x -= 10
                time.sleep(0.1)

    def caerGravedad(self, Activos, Pisos):
        while pygame.sprite.spritecollideany(self, Pisos, collided=None) == None and \
        pygame.sprite.spritecollideany(self, Activos, collided=None) == None:
            self.rect.y += 30
            time.sleep(0.1)