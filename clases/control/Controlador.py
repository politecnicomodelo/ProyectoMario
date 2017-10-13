from clases import *
import pygame.locals
from clases.control.Base import *
from clases.Goombas import Goomba

class Controlador(object):

    @classmethod
    def iniciar(cls):
        pygame.init()

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
    def rellenar_pantalla(cls, ventana, fondo, colores):
        ventana.fill(colores["Negro"])
        ventana.blit(fondo.image, fondo.rect)

    @classmethod
    def mover_pantalla(cls, fondo, mario):
        fondo.rect.x -= 20
        for item in Base.sprites:
            if item is not mario:
                if item not in Base.corazon.sprites():
                    item.rect.x -= 20


    @classmethod
    def buscar_eventos(cls, mario):
        for evento in pygame.event.get():

            if evento.type == pygame.QUIT:
                cls.terminar()
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
                cls.terminar()
            if evento.type == pygame.KEYUP:
                if mario.bajando is False and mario.muerto is False:
                    mario.terminar_caida()

    @classmethod
    def buscar_teclas(cls):
        return pygame.key.get_pressed()

    @classmethod
    def eliminar_sprites(cls, mario):
        for item in Base.sprites:
            if item.rect.x < -85:
                if item is not mario:

                    if item in Base.tuberias:
                        if item.rect.x < -85:
                            Base.sprites.remove(item)
                            Base.tuberias.remove(item)
                    else:
                        Base.sprites.remove(item)
                        if item in Base.bloques:

                            Base.bloques.remove(item)
                            if item in Base.ladrillos:
                                Base.ladrillos.remove(item)
                            elif item in Base.ladrillos2:
                                Base.ladrillos2.remove(item)
                            else:
                                Base.signos.remove(item)

                        elif item in Base.piso:
                            Base.piso.remove(item)

    @classmethod
    def salto_mario(cls, mario, frames_totales):

        if mario.salto:
            mario.saltar(frames_totales)
        if mario.rebote:
            mario.rebote = False
            mario.terminar_salto()
            mario.activar_salto(200)

    @classmethod
    def colisiones(cls, mario, frames_totales):

        control = False
        moneda = mario.colision(Base.monedas)
        if moneda is not False:
            moneda.agarrada()

        goomba = mario.colision(Base.goombas)
        if goomba is not False and mario.salto is False and mario.bajando is False:
            if mario.inmune is False:
                mario.perder_vida(frames_totales, 345)
        if goomba is not False and mario.bajando:
            if goomba.muerto is False:
                goomba.morir(frames_totales)
                mario.colision_goomba(goomba)

        #Mientras anda a pie
        if mario.salto is False:
            if mario.colision_piso() is False:
                if Controlador.colision_escaleras(mario) is False:
                    if Controlador.colision_tuberias(mario) is False:
                        if Controlador.colision_bloques(mario) is False:
                            control = True
                            mario.detenido = False
                            mario.caerse()
                            if mario.bajo_tierra():
                                mario.perder_vida(frames_totales, 495)

                if control is False:
                    if mario.bajando:
                        mario.terminar_caida()
                        mario.bajando = False

            elif mario.colision_piso():
                tuberia = mario.colision(Base.tuberias)
                if tuberia is not False:
                    mario.colision_tuberia(tuberia)

                escalera = mario.colision(Base.escalera)
                if escalera is not False:
                    mario.colision_escalera(escalera)

                if mario.bajando:
                    mario.terminar_caida()
                    mario.bajando = False

    @classmethod
    def buscar_objetos(cls, mario):
        bloque = mario.colision(Base.bloques)
        bloque2 = False

        if bloque in Base.signos:
            bloque2 = mario.colision(Base.ladrillos)
            if bloque2 is False:
                bloque2 = mario.colision(Base.ladrillos2)
        else:
            if bloque in Base.ladrillos:
                bloque2 = mario.colision(Base.ladrillos2)
            elif bloque in Base.ladrillos2:
                bloque2 = mario.colision(Base.ladrillos)
            if bloque2 is False:
                bloque2 = mario.colision(Base.signos)
        return bloque, bloque2

    @classmethod
    def actualizar_secundarios(cls, frames_totales, mario):
        for moneda in Base.monedas:
            if moneda.movible:
                moneda.movimiento()
                moneda.animacion(frames_totales)
        for item in Base.signos:
            if item.proceso:
                item.tocado()

        for goomba in Base.sprites:
            if isinstance(goomba, Goomba):
                goomba.movimiento(frames_totales)
                goomba.verificar_muerte(frames_totales)
        mario.verificar_inmunidad(frames_totales)
        mario.animacion_muerte()

    @classmethod
    def colision_escaleras(cls, mario):
        escalera = mario.colision(Base.escalera)

        if escalera is not False:
            if mario.colision_escalera(escalera) is False:
                return True
        return False

    @classmethod
    def colision_tuberias(cls, mario):
        tuberia = mario.colision(Base.tuberias)

        if tuberia is not False:
            if mario.colision_tuberia_caida(tuberia) is False:
                return True
        return False

    @classmethod
    def colision_bloques(cls, mario):
        bloque = mario.colision(Base.bloques)

        if bloque is not False:
            if mario.colision_bloques(bloque) is False:
                return True
        return False

    @classmethod
    def verificar_muerte(cls, mario):

        if mario.muerto and mario.bajo_tierra and mario.animacion is False:
            return True
        return False

    @classmethod
    def quitar_corazones(cls):
        maximo = 0
        for corazon in Base.corazon:
            if corazon.rect.x > maximo:
                maximo = corazon.rect.x

        for corazon in Base.corazon:
            if corazon.rect.x == maximo:
                Base.corazon.remove(corazon)
                Base.sprites.remove(corazon)
