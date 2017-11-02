from listo.clases.controlador import Controlador
import pygame


def listo():

    ancho = 1280
    alto = 720

    Controlador.iniciar()

    ventana = Controlador.configurar_pantalla(ancho, alto)

    reloj = Controlador.iniciar_reloj()

    FPS = 120

    fuente = pygame.font.SysFont("mariokartds", 180)

    texto = fuente.render("listo?", False, (255,255,255))

    cuenta = False

    estado = 3

    while True:

        Controlador.rellenar_pantalla(ventana, (0,0,0))

        if cuenta is False:

            teclas = Controlador.buscar_teclas()

            if teclas[pygame.K_SPACE]:
                cuenta = True

            ventana.blit(texto, (340, 150))

        else:
            ventana.blit(texto2, (590, 100))
            pygame.time.delay(1000)
            if estado == -1:
                Controlador.rellenar_pantalla(ventana, (0,0,0))
                pygame.time.delay(1000)
                return True
            if estado == 0:
                estado = -1

        Controlador.set_fps(reloj, FPS)

        Controlador.buscar_eventos()

        pygame.display.flip()

        if estado == 3 and cuenta:
            estado = 2
            fuente2 = pygame.font.SysFont("mariokartds", 300)
            texto2 = fuente2.render("3", False, (255, 255, 255))

        elif estado == 2:
            estado = 1
            fuente2 = pygame.font.SysFont("mariokartds", 300)
            texto2 = fuente2.render("2", False, (255, 255, 255))

        elif estado == 1:
            estado = 0
            fuente2 = pygame.font.SysFont("mariokartds", 300)
            texto2 = fuente2.render("1", False, (255, 255, 255))


