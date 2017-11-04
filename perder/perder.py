from perder.clases.controlador import Controlador
import pygame


def perdiste():

    pygame.mixer.music.load("musica/perdiste.mp3")
    pygame.mixer.music.play(1,0)
    pygame.mixer.music.set_volume(0.5)

    ancho = 1280
    alto = 720

    Controlador.iniciar()

    ventana = Controlador.configurar_pantalla(ancho, alto)

    reloj = Controlador.iniciar_reloj()

    FPS = 120

    frames_totales = 0

    fuente = pygame.font.SysFont("mariokartds", 180)

    texto = fuente.render("perdiste!", False, (255,255,255))

    fuente2 = pygame.font.SysFont("mariokartds", 80)

    texto2 = fuente2.render("gracias por jugar", False, (255,255,255))

    while True:

        teclas = Controlador.buscar_teclas()

        Controlador.set_fps(reloj, FPS)

        Controlador.buscar_eventos()

        frames_totales += 1

        if teclas[pygame.K_SPACE]:
            return True

        Controlador.rellenar_pantalla(ventana, (0,0,0))

        ventana.blit(texto, (220, 100))
        ventana.blit(texto2, (270, 400))

        pygame.display.flip()
