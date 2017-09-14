from clases.Controlador import *
from clases.Mario import *
from .clases.Fondo import *

ancho = 1280
alto = 720

mario = Mario()

def main():

    Controlador.iniciar()

    ventana = Controlador.configurar_pantalla(ancho, alto)

    reloj = Controlador.iniciar_reloj()

    fondo = Fondo()

    while True:

        Controlador.buscar_eventos()

        teclas = pygame.key.get_pressed()

        print(teclas)

        Controlador.rellenar_pantalla(ventana, fondo, 0, 0)

        pygame.display.flip()

        Controlador.set_fps(reloj, 60)

main()