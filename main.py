import pygame
from clases.Controlador import *
from clases.Mario import Mario

ancho = 1280
alto = 720

main()

def main():

    Controlador.iniciar()

    ventana = Controlador.configurar_pantalla(ancho, alto)

    reloj = Controlador.iniciar_reloj()

    fondo = pygame.image.load("imagenes/fondo.jpg")

    while True:

        Controlador.buscar_eventos()

        teclas = pygame.key.get_pressed()

        Controlador.rellenar_pantalla(ventana, fondo, 0, 0)

        pygame.display.flip()

        Controlador.set_fps(reloj, 60)