from .Controlador import *
from .Base import *

def dibujo(fondo, ventana, colores):

    Controlador.rellenar_pantalla(ventana, fondo, colores)
    Base.sprites.draw(ventana)
    Base.sprites_principales.draw(ventana)
    pygame.display.flip()