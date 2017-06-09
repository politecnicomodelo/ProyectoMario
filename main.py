import sys
import pygame
import time
from pygame.locals import *
from clases.Mario import Mario

ancho = 1080
alto = 720

def main():
    screen=pygame.display.set_mode((ancho, alto))
    pygame.display.set_caption("Mario Bros")
    fondo=pygame.image.load("imagenes/celeste.png")
    mario=Mario()
    while True:
        teclas = pygame.key.get_pressed()
        for eventos in pygame.event.get():
            if eventos.type == QUIT:
                sys.exit(0)
        mario.mover(teclas)
        screen.blit(fondo, (0, 0))
        screen.blit(mario.image, mario.rect)
        pygame.display.flip()

if __name__ == '__main__':
    pygame.init()
    main()