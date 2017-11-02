from inicios.Clases import *
from inicios.Clases.Dibujo import *
import pygame

def inicio():

    Controlador.iniciar()

    colores = {"Blanco": (255, 255, 255), "Negro": (0, 0, 0)}

    ancho = 1280
    alto = 720

    fps = 120

    fondo = Fondo()

    ventana = Controlador.configurar_pantalla(ancho, alto)

    reloj = Controlador.iniciar_reloj()

    Controlador.Inicializar_Titulo()
    Controlador.Inicializar_Subtitulo()
    Controlador.Inicializacion_Final()

    frames_totales = 0

    Devolucion = False

    Termine = False

    delay = 10

    frame = frames_totales

    otros_frames = frames_totales

    Contador = 0

    pygame.mixer.music.load("musica/menu_principal.mp3")
    pygame.mixer.music.play(10, 0)
    pygame.mixer.music.set_volume(0.3)

    while True:

        Controlador.set_fps(reloj, fps)

        if Controlador.buscar_eventos():
            Devolucion = True

        if Devolucion and otros_frames + 4 < frames_totales:
            Termine = True
            Base.sprites_principales.add(Base.fondo[Contador])
            if Contador >= 17:
                Devolucion = False
            Contador += 1
            otros_frames = frames_totales

        if Contador == 18:
            pygame.mixer.music.stop()
            if otros_frames + 90 < frames_totales:
                for sprite in Base.sprites:
                    Base.sprites.remove(sprite)
                for sprite in Base.sprites_principales:
                    Base.sprites_principales.remove(sprite)
                return True

        if not Termine:
            Controlador.mover()
            if frame + delay < frames_totales:
                if len(Base.letras_pasivas) > 0:
                    frame = Controlador.proxima_letra(frames_totales)

        dibujo(fondo, ventana, colores)

        delay += 5

        if delay == 15:
            delay = 5

        frames_totales += 1