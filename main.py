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

Monedas=0
Vidas=0

Activos=pygame.sprite.Group()
Marios=pygame.sprite.Group()

mario = Mario()
mario.add(Marios)
unPiso = Piso()
unPiso.add(Activos)
bloque1=Bloque(582, 444)
bloque1.add(Activos)
signo1=Signo(798, 444)
signo1.add(Activos)

def main():

    reloj=pygame.time.Clock()
    fondo = pygame.image.load("imagenes/fondo.jpg")
    screen = pygame.display.set_mode((ancho, alto))
    pygame.display.set_caption("Mario Bros")
    x = 0
    y = 0
    muevePantalla = False
    while True:
        for eventos in pygame.event.get():
            if eventos.type == QUIT:
                sys.exit(0)
        teclas = pygame.key.get_pressed()

        if muevePantalla == True:
            x -= 15
            for item in Activos:
                item.rect.x -= 15

        signo1.devuelve(mario, False, True, Activos)
        muevePantalla = mario.mover(teclas, unPiso, muevePantalla, Activos)
        screen.blit(fondo, (x, y))
        Activos.draw(screen)
        Marios.draw(screen)
        pygame.display.flip()
        reloj.tick(60)

if __name__ == '__main__':
    pygame.init()
    main()