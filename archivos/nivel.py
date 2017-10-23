from archivos.dibujo import *
from archivos.procesos import *
from archivos.inicializacion import *


def nivel(reloj, mario, ventana, colores, fondo):

    terminar = False

    FPS = 120

    frames_totales = 0

    segundo = 0

    inicializacion(mario)

    pygame.mixer.music.load("musica/juego.wav")
    #pygame.mixer.music.play(10,0)
    pygame.mixer.music.set_volume(0.5)

    while True:

        if procesos(reloj, mario, FPS, frames_totales, fondo, ventana):
            mario.tiempo = segundo
            return True
        if frames_totales % (FPS / 4) == 0:
            segundo += 1

        dibujo(fondo, ventana, colores)

        frames_totales += 1