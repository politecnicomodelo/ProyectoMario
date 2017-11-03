from calibrar.clases.Base import Base
import pygame


class cargando(Base):

    def __init__(self):

        Base.__init__(self, 500, 120, 300, 300, "imagenes/cargando/original.png")

        Base.sprites.add(self)

        self.movimiento_original = "imagenes/cargando/original.png"
        self.movimientos = ("imagenes/cargando/1.png", "imagenes/cargando/2.png",
                            "imagenes/cargando/3.png", "imagenes/cargando/4.png",
                            "imagenes/cargando/5.png", "imagenes/cargando/6.png",
                            "imagenes/cargando/7.png", "imagenes/cargando/8.png",
                            "imagenes/cargando/hecho.png", "imagenes/cargando/falla.png",)

        self.estado = 0
        self.frame = 0

    def animacion(self, frames_totales):

        if (frames_totales - self.frame) > 50:

            if self.estado < 7:
                self.cambiar_sprite(self.estado)
                self.estado += 1
                self.frame = frames_totales
            else:
                self.frame = frames_totales
                self.cambiar_sprite(self.estado)
                self.estado = 0

    def cambiar_sprite(self, estado):

        if estado == "imagenes/cargando/original.png":
            self.image = pygame.image.load("imagenes/cargando/original.png")
            self.image = pygame.transform.scale(self.image, (self.ancho, self.alto))
        else:
            self.image = pygame.image.load(self.movimientos[estado])
            self.image = pygame.transform.scale(self.image, (self.ancho, self.alto))