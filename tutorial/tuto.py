from tutorial.archivos.juegos import *
from tutorial.clases.Mario_Tuto import *

colores = {"Blanco": (255,255,255), "Negro": (0,0,0)}

mario = Mario_T()

def tutorial():

    if juegos(colores, mario):
        return True