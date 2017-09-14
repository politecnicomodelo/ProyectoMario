from .Base import *
import _thread
import time

ancho = 1280
alto = 720

class Goomba(Base):
    def __init__(self):
        Base.__init__(self, 100, 640, 100, 100, "imagenes/goomba.png")
        self.image = pygame.transform.scale(self.image, (60, 60))
        Base.sprites.add(self)

    def mueveGoomba(self, Activos, Mario):
        self.rect.x+=3
        if self.rect.collidepoint(Mario.rect.midbottom):
            self.image = pygame.transform.scale(self.image, (60, 10))
            self.rect.y = 500
            self.rect.x-=3
