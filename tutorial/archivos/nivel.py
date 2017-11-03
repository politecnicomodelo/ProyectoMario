from tutorial.archivos.dibujo import *
from tutorial.archivos.procesos import *
from tutorial.clases.Piso import *
from tutorial.clases.Letras import Letra
from tutorial.clases.Bloque import Bloque
from tutorial.clases.Moneda import Moneda
from tutorial.clases.Base import Base
from tutorial.clases.Mario_Tuto import Mario_T

def nivel(reloj, mario, ventana, colores):

    FPS = 120

    frames_totales = 0

    #pygame.mixer.music.load("musica/juego.wav")
    #pygame.mixer.music.play(10,0)
    #pygame.mixer.music.set_volume(0.5)

    m = Moneda(700,600,1)

    P = Letra(400, 300, "imagenes/letras/P.png")
    A = Letra(500, 300, "imagenes/letras/A.png")
    U = Letra(600, 300, "imagenes/letras/U.png")
    S = Letra(700, 300, "imagenes/letras/S.png")
    A = Letra(800, 300, "imagenes/letras/A.png")

    x = 0

    animacion = False
    otros_frames = frames_totales
    contador = 0

    for i in range(40):
        piso = Piso(x,695)
        x += 72

    mario.estado_texto = 0
    fuente = pygame.font.SysFont("mariokartdsregular", 70)
    mario.texto = fuente.render("tutorial", False, colores["Negro"])
    mario.permitir = False

    Controlador.Inicializacion_Final()

    while True:

        if procesos(reloj, mario, FPS, frames_totales, ventana):
            animacion = True

        dibujo(ventana, colores, mario)

        frames_totales += 1

        if frames_totales == 300:
            mario.estado_texto = 1
            mario.texto = fuente.render("agarra la moneda", False, colores["Negro"])
            mario.permitir = True

        if animacion and otros_frames + 4 < frames_totales:
            Base.sprites_principales.add(Base.fondo[contador])
            if contador == 17:
                animacion = False
            contador += 1
            otros_frames = frames_totales

        if contador == 18:
            if otros_frames + 60 < frames_totales:
                for item in Base.sprites_principales:
                    Base.sprites_principales.remove(item)
                for item in Base.sprites:
                    Base.sprites_principales.remove(item)
                return True