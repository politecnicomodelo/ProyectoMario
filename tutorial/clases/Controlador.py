import pygame
from tutorial.clases.Mario_Tuto import Mario_T
from tutorial.clases.Moneda import Moneda
from tutorial.clases.Base import Base
from tutorial.clases.Bloque import Bloque
from tutorial.clases.Fin import *

class Controlador(object):

    @classmethod
    def iniciar(cls):
        pygame.init()
        #pygame.mouse.set_visible(False)

    @classmethod
    def terminar(cls):
        pygame.quit()
        quit()

    @classmethod
    def configurar_pantalla(cls, ancho, alto):

        display = pygame.display.set_mode((ancho, alto)) #, pygame.FULLSCREEN
        pygame.display.set_caption("Super Poli Bros")
        return display

    @classmethod
    def iniciar_reloj(cls):
        return pygame.time.Clock()

    @classmethod
    def set_fps(cls, reloj, frames):
        reloj.tick(frames)

    @classmethod
    def rellenar_pantalla(cls, ventana, colores):
        ventana.fill(colores['Blanco'])

    @classmethod
    def buscar_eventos(cls, mario):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                cls.terminar()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    cls.terminar()
                if evento.key == pygame.K_q:

                    if mario.direccion:
                        mario.permitir_derecha = True
                    if mario.direccion is False:
                        mario.permitir_izquierda = True

                if evento.key == pygame.K_e:
                    if mario.salto is False:
                        mario.permitir_derecha = False
                        mario.permitir_izquierda = False

                if evento.key == pygame.K_x:
                    mario.permitir_salto = True
                if evento.key == pygame.K_p:

                    mario.detenerse()

                    if mario.detenido:

                        mario.permitir_derecha = False
                        mario.permitir_izquierda = False

                        if mario.direccion:
                            mario.direccion = False
                        else:
                            mario.direccion = True

            if evento.type == pygame.KEYUP:
                if mario.bajando is False:
                    mario.detenerse()

    @classmethod
    def salto_mario(cls, mario, frames_totales):

        if mario.salto:
            mario.saltar(frames_totales)

    @classmethod
    def colisiones(cls, mario, frames_totales):

        control = False

        moneda = mario.colision(Base.monedas)
        if moneda is not False:
            moneda.agarrada()
            if moneda.identificador == 1:

                m = Moneda(20,290,2)
                bloque = Bloque(30,450)

                fuente = pygame.font.SysFont("mariokartds", 70)
                mario.estado_texto = 2
                mario.texto = fuente.render("salta para agarrar la moneda", False, (0,0,0))

            if moneda.identificador == 2:
                m = Moneda(550,600,3)

                fuente = pygame.font.SysFont("mariokartds", 70)
                mario.estado_texto = 3
                mario.texto = fuente.render("agarra la ultima moneda", False, (0,0,0))

            if moneda.identificador == 3:

                mario.estado_texto = 4
                fuente = pygame.font.SysFont("mariokartds", 70)
                mario.texto = fuente.render("fin del tutorial", False, (0,0,0))

                for item in Base.bloques:
                    Base.bloques.remove(item)
                    Base.sprites.remove(item)
                mario.permitir = False
                mario.final = True
                mario.frame_permitido = frames_totales

        # Mientras anda a pie
        if mario.salto is False:
            if mario.colision_piso() is False:
                if Controlador.colision_bloques(mario) is False:
                    control = True
                    mario.detenido = False
                    mario.caerse()

                if control is False:
                    if mario.bajando:
                        mario.detenerse()
                        mario.bajando = False

            elif mario.colision_piso():
                if mario.bajando:
                    mario.detenerse()
                    mario.bajando = False

        if mario.frame_permitido + 300 < frames_totales and mario.permitir is False and mario.final:
            mario.final = False
            return True

    @classmethod
    def colision_bloques(cls, mario):
        bloque = mario.colision(Base.bloques)

        if bloque is not False:
            if mario.colision_bloques(bloque) is False:
                return True
        return False

    @classmethod
    def pausa(cls, mario, ventana):

        control = False

        pygame.draw.rect(ventana, (65, 105, 225), (375, 260, 500, 150), 10)
        Base.letras.draw(ventana)
        pygame.display.flip()

        while control is False:

            Controlador.buscar_eventos(mario)

            teclas = Controlador.buscar_teclas()

            if teclas[pygame.K_F2]:
                control = True

    @classmethod
    def buscar_teclas(cls):
        return pygame.key.get_pressed()


    @classmethod
    def Inicializacion_Final(cls):

        c1 = Final(0,0,340,184, "inicios/Transicion_Final/cuadro.png")
        c2 = Final(340,0,340,184, "inicios/Transicion_Final/cuadro.png")
        c3 = Final(680,0,340,184, "inicios/Transicion_Final/cuadro.png")
        c4 = Final(1020,0,360,190, "inicios/Transicion_Final/cuadro.png")
        c5 = Final(1020,184,360,184, "inicios/Transicion_Final/cuadro.png")
        c6 = Final(1020,368,360,184, "inicios/Transicion_Final/cuadro.png")
        c7 = Final(1020,552,360,190, "inicios/Transicion_Final/cuadro.png")
        c8 = Final(680,552,340,190, "inicios/Transicion_Final/cuadro.png")
        c9 = Final(340,552,340,190, "inicios/Transicion_Final/cuadro.png")
        c10 = Final(0,552,340,190, "inicios/Transicion_Final/cuadro.png")
        c11 = Final(0,368,340,184, "inicios/Transicion_Final/cuadro.png")
        c12 = Final(0,184,340,184, "inicios/Transicion_Final/cuadro.png")
        c13 = Final(340,184,340,184, "inicios/Transicion_Final/cuadro.png")
        c14 = Final(680,184,340,184, "inicios/Transicion_Final/cuadro.png")
        c15 = Final(1020,184,360,184, "inicios/Transicion_Final/cuadro.png")
        c16 = Final(1020,368,360,184, "inicios/Transicion_Final/cuadro.png")
        c17 = Final(680,368,340,184, "inicios/Transicion_Final/cuadro.png")
        c18 = Final(340,368,340,184, "inicios/Transicion_Final/cuadro.png")