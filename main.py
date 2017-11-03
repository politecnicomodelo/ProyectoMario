from archivos.juego import *
from tutorial.tuto import *
from clases.control.Controlador import Controlador
from ingreso_nombre.ingreso import ingreso
from inicios.Main import *
from instrucciones_1.instrucciones import *
from indicaciones.indic import *
from perder.perder import *
from listo.listorti import *
from calibrar.calibrado import *
from final.finalisimo import *

colores = {"Blanco": (255,255,255), "Negro": (0,0,0)}

nombre = None
pygame.mixer.init()


def main():
    #if inicio():
        #pygame.mixer.music.load("musica/tranquilidad.mp3")
        #pygame.mixer.music.play(10,0)
        #pygame.mixer.music.set_volume(0.5)
        # nombre = ingreso()
        #calibrado()
        #if tutorial():
        #      if instrucciones():
        #          if indicaciones():
                     #if listo():
                        #pygame.mixer.music.stop()
                        #mario = juego(colores)
                        # if mario is False:
                            #pygame.mixer.music.stop()
                            #perdiste()
                        # else:
                        #     pass
                            finalizar(5, 16, 290, 350, 1, False)
                            main()

main()