from archivos.juego import *
from tutorial.tuto import *
from clases.control.Controlador import Controlador
from ingreso_nombre.ingreso import ingreso
from inicios.Main import *
from instrucciones_1.instrucciones import *
from indicaciones.indic import *

colores = {"Blanco": (255,255,255), "Negro": (0,0,0)}

nombre = None

def main():
    #if inicio():
        #nombre = ingreso()
        #if tutorial():
            #if instrucciones():
                #if indicaciones():
                    mario = juego(colores)
                    Controlador.terminar()

main()