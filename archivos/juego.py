from archivos.nivel import *
from clases.control.Controlador import *
from clases.control.Fondo import *
from clases.Mario import Mario
import pygame

def juego(colores, nombre):

    mario = Mario()

    ancho = 1280
    alto = 720

    Controlador.iniciar()

    db = Controlador.iniciar_database()

    Controlador.cargar_nivel(db)

    pygame.mixer.music.load("musica/juego.mp3")
    pygame.mixer.music.play(10, 0)
    pygame.mixer.music.set_volume(0.1)

    ventana = Controlador.configurar_pantalla(ancho, alto)

    reloj = Controlador.iniciar_reloj()



    fondo = Fondo()

    if nivel(reloj, mario, ventana, colores, fondo):

        Controlador.eliminacion_estatica()

        if mario.animacion_castillo:
            total = int((((3 * 1000 + mario.monedas * 200 + mario.puntos_mastil * 4 + 100 * mario.cantidad_signo + 50 * mario.cantidad_goombas) / mario.tiempo) * 125))
            Controlador.cargar_datos(db, mario, nombre, total)
            i = Controlador.buscar_posicion(db, total)
            return mario, i, total
        else:
            pygame.time.delay(2000)
            return False, False, False
