from clases.Mario import *
from clases.control.Controlador import *
from clases.control.Fondo import *

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

        if teclas[pygame.K_d] or teclas[pygame.K_RIGHT]:
            print("DERECHA")

        Controlador.rellenar_pantalla(ventana, fondo)

        pygame.display.flip()

        Controlador.set_fps(reloj, 60)


main()