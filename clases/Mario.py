from .Base import *
import _thread
import time

ancho = 1280
alto = 720

class Mario(Base):

    def __init__(self):

        Base.__init__(self, ancho-1300, 600, 100, 100, "imagenes/mario/mario_der.png")
        Base.sprites.add(self)


   # def mover(self):