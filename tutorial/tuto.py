from tutorial.archivos.juegos import *
from tutorial.clases.Mario_Tuto import *
from tutorial.clases.Base import Base


def tutorial():

    colores = {"Blanco": (255,255,255), "Negro": (0,0,0)}

    for i in Base.sprites:
        Base.sprites.remove(i)

    mario = Mario_T()

    if juegos(colores, mario):
        return True