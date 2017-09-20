from clases.control.Controlador import *
from archivos.dibujo import *
from archivos.procesos import *
from clases import *

# Separacion entre bloques: 72

def nivel(reloj, mario, ventana, colores, fondo):

    FPS = 120

    frames_totales = 0

    segundo = 0

    x = 0

    for i in range(15):
        piso = Piso(x,695,"imagenes/piso_bloque.png")
        x += 72

    while True:

        procesos(reloj, mario, FPS, frames_totales)

        if frames_totales % (FPS / 4) == 0:

            segundo += 0.25

        dibujo(fondo, ventana, colores, mario)

        frames_totales += 1