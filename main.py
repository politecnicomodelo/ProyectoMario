from archivos.juego import *
from clases.Mario import *

colores = {"Blanco": (255,255,255), "Negro": (0,0,0)}

mario = Mario()

def main():

    juego(colores, mario)

main()

# TODO: Hacer que pueda saltar y moverse a la vez
# TODO: Mejorar las transiciones cuando pasa de pantalla
# TODO: Sacar los sprites del grupo cuando la pantalla avanza?
# TODO: Caerse y reaparecer
# TODO: Cómo hacer la devolucion de las colisiones?