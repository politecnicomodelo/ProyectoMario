import sys
import pygame
from pygame.locals import *
from clases.Mario import Mario
from clases.Bloques import Bloque
from clases.Monedas import Moneda
from clases.Hongos import Hongo
from clases.Signos import Signo
from clases.Piso import Piso

ancho = 1360
alto = 768

def crearObjetos():
    print("Hola")

def main():
    reloj=pygame.time.Clock()
    screen=pygame.display.set_mode((ancho, alto))
    pygame.display.set_caption("Mario Bros")
    fondo=pygame.image.load("imagenes/fondo.jpg")
    mario=Mario()
    unPiso = Piso()
    x=0
    y=0
    muevePantalla=False
    while True:
        for eventos in pygame.event.get():
            if eventos.type == QUIT:
                sys.exit(0)
        teclas = pygame.key.get_pressed()

        if muevePantalla == True:
            x-=15

        screen.blit(fondo, (x, y))
        muevePantalla=mario.mover(teclas, unPiso, muevePantalla)
        screen.blit(mario.image, mario.rect)
        screen.blit(unPiso.image, unPiso.rect)
        mario.update()
        unPiso.update()
        pygame.display.flip()
        reloj.tick(120)

if __name__ == '__main__':
    pygame.init()
    main()