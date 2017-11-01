from archivos.juego import *
from tutorial.tuto import *
from clases.control.Controlador import Controlador
from inicio.Main import *

colores = {"Blanco": (255,255,255), "Negro": (0,0,0)}

def main():
    if inicio():
        if tutorial():
            juego(colores)

main()