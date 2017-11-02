from archivos.juego import *
from tutorial.tuto import *
from clases.control.Controlador import Controlador
from ingreso_nombre.ingreso import ingreso
from inicios.Main import *
from instrucciones_1.instrucciones import *
from indicaciones.indic import *
from perder.perder import *
from listo.listorti import *

colores = {"Blanco": (255,255,255), "Negro": (0,0,0)}

nombre = None


def main():
    #if inicio():
        # pygame.mixer.music.load("musica/tranquilidad.mp3")
        # pygame.mixer.music.play(10,0)
        # pygame.mixer.music.set_volume(0.5)
        # nombre = ingreso()
        # if tutorial():
        #      if instrucciones():
        #          if indicaciones():
        #              if listo():
        #                 pygame.mixer.music.stop()
                        mario = juego(colores)
                        # if mario is False:
                        #     perdiste()
                        # else:
                        #     pass
                        main()

main()