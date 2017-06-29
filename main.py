import sys
import pygame
from pygame.locals import *
from clases.Mario import Mario
from clases.Bloques import Bloque
from clases.Piso import Piso

ancho = 1360
alto = 768

def main():
    reloj=pygame.time.Clock()
    screen=pygame.display.set_mode((ancho, alto))
    pygame.display.set_caption("Mario Bros")
    fondo=pygame.image.load("imagenes/celeste.png")
    mario=Mario()
    bloque=Bloque()
    unPiso = Piso()
    x=0
    y=0
    muevePantalla=False
    while True:
        for eventos in pygame.event.get():
            if eventos.type == QUIT:
                sys.exit(0)
        teclas = pygame.key.get_pressed()

        muevePantalla = mario.mover(teclas, unPiso, bloque, muevePantalla)

        while muevePantalla is True:
            x-=10

        screen.blit(fondo, (x, y))
        mario.mover(teclas, unPiso, bloque, muevePantalla)
        screen.blit(mario.image, mario.rect)
        #screen.blit(bloque.image, bloque.rect)
        screen.blit(unPiso.image, unPiso.rect)
        mario.update()
        unPiso.update()
        bloque.update()
        pygame.display.flip()
        reloj.tick(120)

if __name__ == '__main__':
    pygame.init()
    main()