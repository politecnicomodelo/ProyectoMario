from tutorial.archivos.nivel import *
from tutorial.clases.Controlador import *

def juegos(colores, mario):

    ancho = 1280
    alto = 720

    Controlador.iniciar()

    ventana = Controlador.configurar_pantalla(ancho, alto)

    reloj = Controlador.iniciar_reloj()

    if nivel(reloj, mario, ventana, colores):
        return True
