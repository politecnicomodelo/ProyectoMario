from archivos.juego import *
from clases.Mario import *
from clases.control.Controlador import Controlador
from inicio.Main import *

colores = {"Blanco": (255,255,255), "Negro": (0,0,0)}

mario = Mario()

def main():

    if inicio():
        juego(colores, mario)

main()