from archivos.juego import *
from clases.Mario import *

colores = {"Blanco": (255,255,255), "Negro": (0,0,0)}

mario = Mario()

def main():

    juego(colores, mario)

main()