from archivos.juego import *
from tutorial.tuto import *
from clases.control.Controlador import Controlador
from ingreso_nombre.ingreso import ingreso
from inicio.Main import *

colores = {"Blanco": (255,255,255), "Negro": (0,0,0)}

nombre = None

def main():
    #if inicio():
        #nombre = ingreso()
    if tutorial():
        juego(colores)

main()