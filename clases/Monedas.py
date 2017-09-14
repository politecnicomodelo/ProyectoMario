import time
from clases.control.Base import *
import time

from clases.control.Base import *


class Moneda(pygame.sprite.Sprite):

    def __init__(self, Padre):

        Base.__init__(self, Padre.rect.x + 15, Padre.rect.y - 51, 40, 40, "imagenes/moneda.png")
        Base.sprites.add(self)

    def matarMoneda(self, Activos):
        time.sleep(1)
        Activos.remove(self)
        self.kill(self)