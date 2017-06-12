import sys
import pygame
import time
from pygame.locals import *
from clases.Mario import Mario
from clases.Bloques import Bloque

ancho = 640
alto = 360

def main():
    reloj=pygame.time.Clock()
    screen=pygame.display.set_mode((ancho, alto))
    pygame.display.set_caption("Mario Bros")
    fondo=pygame.image.load("imagenes/celeste.png")
    mario=Mario()
    bloque=Bloque()
    while True:
        teclas = pygame.key.get_pressed()
        for eventos in pygame.event.get():
            if eventos.type == QUIT:
                sys.exit(0)
        reloj.tick(60)
        mario.mover(teclas)
        screen.blit(fondo, (0, 0))
        screen.blit(mario.image, mario.rect)
        screen.blit(bloque.image, bloque.rect)
        mario.update()
        bloque.update()
        pygame.display.flip()

if __name__ == '__main__':
    pygame.init()
    main()