from archivos.nivel import *
from clases.control.Controlador import *
from clases.control.Fondo import *
from clases.Mario import Mario
import pygame

def juego(colores):

    mario = Mario()

    ancho = 1280
    alto = 720

    Controlador.iniciar()

    #db = Controlador.iniciar_database()

    #Controlador.cargar_nivel(db)

    pygame.mixer.music.load("musica/juego.mp3")
    pygame.mixer.music.play(10, 0)
    pygame.mixer.music.set_volume(0.6)

    ventana = Controlador.configurar_pantalla(ancho, alto)

    reloj = Controlador.iniciar_reloj()

    fondo = Fondo()

    if nivel(reloj, mario, ventana, colores, fondo):

        Controlador.eliminacion_estatica()

        if mario.animacion_castillo:
            return mario
            #Controlador.cargar_datos(db, mario)
        else:
            pygame.time.delay(3000)
            return False