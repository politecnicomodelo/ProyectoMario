import pygame
from clases.Mario import Mario

ancho = 1280
alto = 720

Marios=pygame.sprite.Group()

mario = Mario()
mario.add(Marios)

main()

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
            x -= 30
            for item in Activos:
                item.rect.x -= 30
            for item in Pisos:
                item.rect.x -= 30

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