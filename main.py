from archivos.juego import *
from clases.Mario import *

colores = {"Blanco": (255,255,255), "Negro": (0,0,0)}

ancho = 1280
alto = 720

mario = Mario()

def main():

    juego(colores, ancho, alto, mario)

main()