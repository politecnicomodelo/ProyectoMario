from archivos.nivel import *
from clases.control.Controlador import *
from clases.control.Fondo import *

def juego(colores, mario):

    ancho = 1280
    alto = 720

    Controlador.iniciar()

    ventana = Controlador.configurar_pantalla(ancho, alto)

    reloj = Controlador.iniciar_reloj()

    fondo = Fondo()

    nivel(reloj, mario, ventana, colores, fondo)

    Controlador.terminar()