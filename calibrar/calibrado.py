import pygame
from calibrar.clases.Controlador import Controlador
from calibrar.clases.Piso import Piso
from calibrar.clases.cargando import *

def calibrado():

    x = 0

    for i in range(30):
        piso = Piso(x,695)
        x += 72

    Controlador.iniciar()

    carga = cargando()

    ancho = 1280
    alto = 720

    FPS = 120

    frames_totales = 0

    ventana = Controlador.configurar_pantalla(ancho, alto)

    reloj = Controlador.iniciar_reloj()

    fuente = pygame.font.SysFont("mariokartds", 50)
    texto = fuente.render(" a   calibrar", False, (0,0,0))

    mario = pygame.image.load("imagenes/mario/mario.png")
    mario = pygame.transform.scale(mario, (100, 100))

    animacion = False
    finalizado = False

    while True:

        Controlador.set_fps(reloj, FPS)

        accion = Controlador.buscar_eventos()

        if accion == "empezar":
            carga.cambiar_sprite(0)
            texto = fuente.render("calibrando", False, (0,0,0))
            animacion = True
        elif accion == "terminar":
            animacion = False
            carga.cambiar_sprite(carga.movimiento_original)
            carga.estado = 0
            texto = fuente.render(" a   calibrar", False, (0,0,0))
        elif accion == "hecho":
            texto = fuente.render("     fallido", False, (0,0,0))
            animacion = False
            carga.cambiar_sprite(9)
            carga.estado = 0
        elif accion == "falla":
            texto = fuente.render("  finalizado", False, (0,0,0))
            animacion = False
            carga.cambiar_sprite(8)
            carga.estado = 0
        elif accion == "listo":
            finalizado = True

        Controlador.rellenar_pantalla(ventana)
        ventana.blit(texto, (515,25))
        ventana.blit(mario, (20,600))
        Base.sprites.draw(ventana)
        pygame.display.flip()

        if animacion:
            carga.animacion(frames_totales)

        if finalizado:
            return True

        frames_totales += 1

