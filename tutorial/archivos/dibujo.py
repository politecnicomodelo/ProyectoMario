from tutorial.clases.Base import Base
from tutorial.clases.Controlador import Controlador
import pygame

def dibujo(ventana, colores, mario):

    Controlador.rellenar_pantalla(ventana, colores)
    Base.sprites.draw(ventana)
    if mario.estado_texto == 0:
        ventana.blit(mario.texto, (460, 100))
    elif mario.estado_texto == 1:
        ventana.blit(mario.texto, (290, 100))
    elif mario.estado_texto == 2:
        ventana.blit(mario.texto, (250, 100))
    pygame.display.flip()