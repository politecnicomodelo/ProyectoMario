from archivos.juego import *
from tutorial.tuto import *
from clases.control.Controlador import Controlador
from ingreso_nombre.ingreso import ingreso
from inicio.Main import *
from instrucciones_1.instrucciones import *

colores = {"Blanco": (255,255,255), "Negro": (0,0,0)}

nombre = None

def main():
    #if inicio():
        #nombre = ingreso()
        #if tutorial():
            #if instrucciones():
                juego(colores)

main()