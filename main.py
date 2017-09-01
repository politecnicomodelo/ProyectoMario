import pygame
from pygame.locals import *
from clases.Mario import Mario
from clases.Bloques import Bloque
from clases.Monedas import Moneda
from clases.Hongos import Hongo
from clases.Signos import Signo
from clases.Piso import Piso

ancho = 1280
alto = 720

Monedas=0
Vidas=0

Activos=pygame.sprite.Group()
Marios=pygame.sprite.Group()
Pisos=pygame.sprite.Group()

mario = Mario()
mario.add(Marios)

piso1=Piso(0, 695,"imagenes/piso1.png")
piso2=Piso(4297,695,"imagenes/piso2.png")
piso3=Piso(5736,695,"imagenes/piso3.jpg")
piso4=Piso(10819,695,"imagenes/piso4.png")
piso1.add(Pisos)
piso2.add(Pisos)
piso3.add(Pisos)
piso4.add(Pisos)

bloque1=Bloque(582, 444)
bloque1.add(Activos)

signo1=Signo(798, 444)
signo1.devuelve(mario, False, True, Activos, Monedas)
signo1.add(Activos)

signo2=Signo(725, 252)
signo2.devuelve(mario, False, True, Activos, Monedas)
signo2.add(Activos)

signo3=Signo(655, 444)
signo3.devuelve(mario, False, True, Activos, Monedas)
signo3.add(Activos)

listaSignos=[signo1, signo2, signo3]
listaBloques=[bloque1]


def main():

    reloj=pygame.time.Clock()
    fondo = pygame.image.load("imagenes/fondo.jpg")
    screen = pygame.display.set_mode((ancho, alto), pygame.FULLSCREEN)
    pygame.display.set_caption("Super Mega Mario Bros")
    x = 0
    y = 0
    muevePantalla = False

    while True:
        for eventos in pygame.event.get():
            if eventos.type == pygame.K_ESCAPE:
                quit()

        teclas = pygame.key.get_pressed()

        if muevePantalla == True:
            x -= 20
            for item in Activos:
                item.rect.x -= 20
            for item in Pisos:
                item.rect.x -= 20

        muevePantalla = mario.mover(teclas, muevePantalla, Activos, Pisos)

        for item in listaSignos:
            item.devuelve(mario, False, True, Activos, Monedas)
        for item in listaBloques:
            item.devuelveBloque(mario)

        if mario.rect.x == 10000:
            ganarJuego(mario)
        screen.blit(fondo, (x, y))
        Activos.draw(screen)
        Marios.draw(screen)
        Pisos.draw(screen)
        pygame.display.flip()
        reloj.tick(60)

def ganarJuego(mario):
    x=0
    #Animacion de victoria

if __name__ == '__main__':
    pygame.init()
    main()