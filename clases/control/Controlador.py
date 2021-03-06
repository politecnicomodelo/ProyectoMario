from clases.Goombas import Goomba
from clases.Mastil import Mastil
from clases.Castillo import Castillo
import pygame
from clases.control.Base import *
from clases.control.Conexion import Conexion
from clases.control.Suma_Corazon import Suma
from clases.control.Moneda_Control import Moneda_c

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

        display = pygame.display.set_mode((ancho, alto), pygame.FULLSCREEN) #, pygame.FULLSCREEN
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
        fondo.rect.x -= 8
        for item in Base.sprites:
            if item not in Base.corazon.sprites():
                item.rect.x -= 8
        for item in Base.sprites_principales:
            if item is not mario and isinstance(item, Moneda_c) is False:
                item.rect.x -= 8

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
                    mario.salto_permitido = True

                if evento.key == pygame.K_w:
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
    def buscar_teclas(cls):
        return pygame.key.get_pressed()

    @classmethod
    def eliminar_sprites(cls, mario):
        for item in Base.sprites:
            if item.rect.x < -85:
                if item is not mario and isinstance(item, Castillo) is False:
                    if item in Base.tuberias:
                        if item.rect.x < -150:
                            Base.sprites_principales.remove(item)
                            Base.tuberias.remove(item)
                    elif item in Base.hongos:
                        Base.hongos.remove(item)
                        Base.hongos.remove(item)
                    elif item in Base.escalera:
                        Base.sprites.remove(item)
                        Base.escalera.remove(item)
                        if item in Base.escaleras:
                            Base.escaleras.remove(item)
                        else:
                            Base.escaleras2.remove(item)
                    elif item in Base.goombas:
                        Base.sprites.remove(item)
                        Base.goombas.remove(item)
                    elif item in Base.monedas:
                        Base.sprites.remove(item)
                        Base.monedas.remove(item)
                    else:
                        if item in Base.bloques:
                            Base.bloques.remove(item)
                            if item in Base.ladrillos:
                                Base.sprites.remove(item)
                                Base.ladrillos.remove(item)
                            elif item in Base.ladrillos2:
                                Base.sprites.remove(item)
                                Base.ladrillos2.remove(item)
                            else:
                                Base.sprites_principales.remove(item)
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

        mario.colision_piso_caida()

        control = False

        hongo = mario.colision(Base.hongos)
        if hongo is not False:
            mario.agarrar_hongo(hongo, frames_totales)

        moneda = mario.colision(Base.monedas)
        if moneda is not False:
            moneda.agarrada()
            mario.monedas += 1

        goomba = mario.colision(Base.goombas)
        if goomba is not False and mario.salto is False and mario.bajando is False:
            if mario.inmune is False:
                mario.perder_vida(frames_totales, 345)
        if goomba is not False and mario.bajando:
            if goomba.muerto is False:
                goomba.morir(frames_totales, mario)
                mario.colision_goomba(goomba)

        if mario.prohibir_mastil is False:
            mastil = mario.colision(Base.mastil)
            if mastil is not False:
                if isinstance(mastil, Mastil):
                    mario.mastil_tocado(mastil)

        #Mientras anda a pie
        if mario.salto is False:
            if mario.colision_piso() is False:
                if Controlador.colision_escaleras(mario) is False:
                    if Controlador.colision_tuberias(mario) is False:
                        if Controlador.colision_bloques(mario) is False:
                            control = True
                            mario.detenido = False
                            mario.caerse()
                            if mario.bajo_tierra() and mario.flanco is False:
                                mario.perder_vida(frames_totales, 645)

                if control is False:
                    if mario.bajando:
                        mario.detenerse()
                        mario.bajando = False

            elif mario.colision_piso():
                tuberia = mario.colision(Base.tuberias)
                if tuberia is not False:
                    mario.colision_tuberia(tuberia)

                escalera = mario.colision(Base.escalera)
                if escalera is not False:
                    if escalera.rect.x > mario.rect.x:
                        mario.rect.x = escalera.rect.x - 100
                    else:
                        mario.rect.x = escalera.rect.x + 70

                if mario.bajando:
                    mario.detenerse()
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
    def actualizar_secundarios(cls, frames_totales, mario, fondo):
        for hongo in Base.hongos:
            hongo.movimiento(frames_totales)
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
        for item in Base.sprites_principales:
            if isinstance(item, Suma):
                item.desaparecer(frames_totales)
        mario.verificar_inmunidad(frames_totales)
        mario.animacion_muerte()
        mario.verificar_flanco(frames_totales)
        if mario.animacion_final(frames_totales, fondo):
            return True
        return False

    @classmethod
    def actualizar_monedas(cls, mario, fuentes, textos):
        textos[1] = fuentes[0].render(str(mario.monedas), False, (0,0,0))

    @classmethod
    def colision_escaleras(cls, mario):
        escalera = mario.colision(Base.escalera)
        if escalera is not False:
            if mario.colision_escalera(escalera):
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

    @classmethod
    def pausa(cls, mario, ventana):

        control = False

        pygame.draw.rect(ventana, (65,105,225), (375,260, 500, 150), 10)
        Base.letras.draw(ventana)
        pygame.display.flip()


        while control is False:

            Controlador.buscar_eventos(mario)

            teclas = Controlador.buscar_teclas()

            if teclas[pygame.K_F2]:
                control = True

    @classmethod
    def iniciar_database(cls):
        base = Conexion()
        return base

    @classmethod
    def cargar_nivel(cls, base):
        base.cargar_nivel()

    @classmethod
    def cargar_datos(cls, db, mario, nombre, puntuacion):
        db.insertar_datos(mario, nombre, puntuacion)

    @classmethod
    def buscar_posicion(cls, db, puntos):
        return db.buscar_posicion(puntos)

    @classmethod
    def eliminacion_estatica(cls):
        for item in Base.sprites:
            Base.sprites.remove(item)
            if item in Base.hongos:
                Base.hongos.remove(item)
            if item in Base.mastil:
                Base.mastil.remove(item)
            if item in Base.bandera:
                Base.bandera.remove(item)
            if Base.colegio is not None:
                Base.colegio = None
            if item in Base.tuberias:
                Base.sprites_principales.remove(item)
                Base.tuberias.remove(item)
            if item == Base.texto:
                Base.sprites_principales.remove(item)
            if item in Base.hongos:
                Base.hongos.remove(item)
                Base.hongos.remove(item)
            if item in Base.escalera:
                Base.escalera.remove(item)
                if item in Base.escaleras:
                    Base.escaleras.remove(item)
                else:
                    Base.escaleras2.remove(item)
            if item in Base.goombas:
                Base.goombas.remove(item)
            if item in Base.monedas:
                Base.monedas.remove(item)
            if item in Base.piso:
                Base.piso.remove(item)
            else:
                if item in Base.bloques:
                    Base.bloques.remove(item)
                    if item in Base.ladrillos:
                        Base.ladrillos.remove(item)
                    elif item in Base.ladrillos2:
                        Base.ladrillos2.remove(item)
                    else:
                        Base.sprites_principales.remove(item)
                        Base.signos.remove(item)
