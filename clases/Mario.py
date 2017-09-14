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