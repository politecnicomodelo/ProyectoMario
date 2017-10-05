from clases import *

ancho = 1280
alto = 720

class Goomba(Base):

    def __init__(self, x, y):

        Base.__init__(self, x, y, 65, 65, "imagenes/goomba/1.png")

        Base.sprites.add(self)
        Base.goombas.add(self)

        self.direccion = False
        self.frame = 0

    def movimiento(self, frames_totales):

        objeto = self.colision(Base.tuberias)
        if objeto is False:
            objeto = self.colision(Base.escalera)

        if objeto is not False:
            if self.direccion:
                self.direccion = False
            else:
                self.direccion = True

        if self.direccion:
            self.rect.x += 5
        else:
            self.rect.x -= 5

        self.animacion(frames_totales)

    def animacion(self, frames_totales):

        if frames_totales - self.frame > 10:
            self.frame = frames_totales
            self.invertir()

    def invertir(self):
        self.image = pygame.transform.flip(self.image, True, False)
        self.image = pygame.transform.scale(self.image, (self.ancho, self.alto))

    def colision(self, grupo):

        elemento = pygame.sprite.spritecollideany(self, grupo, collided = None)
        if elemento is not None:
            return elemento
        else:
            return False