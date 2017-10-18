from clases.control import Base

class Tuberia(Base):

    def __init__(self, x, alto):

        if alto == 1:
            ruta = "imagenes/tuberias/chica.png"
            altura = 156
            y = 540
        elif alto == 2:
            ruta = "imagenes/tuberias/media.png"
            altura = 220
            y = 475
        elif alto == 3:
            ruta = "imagenes/tuberias/alto.png"
            altura = 290
            y = 405

        Base.__init__(self, x, y, 156, altura, ruta)
        Base.sprites.add(self)
        Base.tuberias.add(self)
        self.alto = alto