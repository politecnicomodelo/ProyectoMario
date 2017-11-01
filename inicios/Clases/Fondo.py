from .Base import *

class Fondo(Base):

    def __init__(self):

        Base.__init__(self, 0, 0, 1366, 768, "inicios/Fondos/Primera.jpg")
        self.activo = True