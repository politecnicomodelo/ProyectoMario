import pygame
class Palabra(object):

    def __init__(self, x, y, c, p, t):
        self.posX = x
        self.posY = y
        self.Color = c
        self.Tamanio_Final = t
        self.texto = p
        self.Fuente = pygame.font.SysFont("mariokartdsregular", self.Tamanio_Final)
        self.Palabra = self.Fuente.render(self.texto, True, self.Color)

    def Aparecer(self, tamanio, Color):
        self.Fuente = pygame.font.SysFont("mariokartdsregular", tamanio)
        self.Palabra = self.Fuente.render(self.texto, True, Color)
        self.posX -= 1

    def Escritura(self, Color, palabra, Diferenciador):
        if Diferenciador:
            self.texto = palabra
            self.Fuente = pygame.font.SysFont("mariokartdsregular", 80)
            self.Palabra = self.Fuente.render(self.texto, True, Color)
        if not Diferenciador:
            self.texto = palabra
            self.Fuente = pygame.font.SysFont("mariokartdsregular", 50)
            self.Palabra = self.Fuente.render(self.texto, True, Color)