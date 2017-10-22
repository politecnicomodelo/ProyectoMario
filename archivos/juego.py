from archivos.nivel import *
from clases.control.Controlador import *
from clases.control.Fondo import *

def juego(colores, mario):

    ancho = 1280
    alto = 720

    Controlador.iniciar()

    #db = Controlador.iniciar_database()

    #Controlador.cargar_nivel(db)

    ventana = Controlador.configurar_pantalla(ancho, alto)

    reloj = Controlador.iniciar_reloj()

    fondo = Fondo()

    if nivel(reloj, mario, ventana, colores, fondo):
        if mario.animacion_castillo:
            pass
            #Controlador.cargar_datos(db, mario)

    Controlador.terminar()