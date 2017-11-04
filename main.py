from archivos.juego import *
from tutorial.tuto import *
from ingreso_nombre.ingreso import ingreso
from inicios.Main import *
from instrucciones_1.instrucciones import *
from indicaciones.indic import *
from perder.perder import *
from listo.listorti import *
from calibrar.calibrado import *
from final.finalisimox import *
from clases.control.Controlador import Controlador

colores = {"Blanco": (255,255,255), "Negro": (0,0,0)}

nombre = None

pygame.mixer.init()

def main():
    pygame.mixer.music.stop()
    if inicio():
        pygame.mixer.music.load("musica/tranquilidad.mp3")
        pygame.mixer.music.play(10,0)
        pygame.mixer.music.set_volume(0.5)
        nombre = ingreso()
        if calibrado():
            if tutorial():
                if instrucciones():
                    if indicaciones():
                        if listo():
                            pygame.mixer.music.stop()
                            mario, i, total = juego(colores, nombre)
                            if mario is False:
                                perdiste()
                            else:
                                pygame.mixer.music.stop()
                                final(mario.vidas, mario.monedas, mario.tiempo, mario.puntos_mastil * 4 + 100 * mario.cantidad_signo + 50 * mario.cantidad_goombas, total, i)
    main()

main()
