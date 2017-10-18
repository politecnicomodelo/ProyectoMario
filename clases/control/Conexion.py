import pymysql
from clases.Ladrillos import Ladrillo
from clases.Signos import Signo
from clases.Monedas import Moneda
from clases.Goombas import Goomba
from clases.Escaleras import Escalera
from clases.Tuberia import Tuberia

class Conexion(object):

    db = None
    cursor_bloques = None
    cursor_tuberias = None

    def __init__(self):
        self.db = pymysql.connect(host ="172.16.2.250", user = "root", passwd = "alumno", autocommit = True)
        self.cursor_bloques = self.db.cursor(pymysql.cursors.DictCursor)
        self.cursor_tuberias = self.db.cursor(pymysql.cursors.DictCursor)
        self.cursor_tuberias.execute("Use Mario")

    def cargar_nivel(self):

        self.cursor_bloques.execute("SELECT * FROM Bloque")

        for bloque in self.cursor_bloques.fetchall():
            if bloque["tipo"] == "Ladrillo1":
                l = Ladrillo(bloque["x"], bloque["y"], False)
            if bloque["tipo"] == "Ladrillo2":
                l = Ladrillo(bloque["x"], bloque["y"], True)
            if bloque["tipo"] == "Signo":
                s = Signo(bloque["x"], bloque["y"])
            if bloque["tipo"] == "Moneda":
                m = Moneda(bloque["x"], bloque["y"], False)
            if bloque["tipo"] == "Goomba":
                m = Goomba(bloque["x"], bloque["y"])
            if bloque["tipo"] == "Escalera":
                m = Escalera(bloque["x"], bloque["y"], False)
            if bloque["tipo"] == "Escalera2":
                m = Escalera(bloque["x"], bloque["y"], True)

        self.cursor_tuberias.execute("SELECT * FROM Tuberia")

        for tuberia in self.cursor_tuberias.fetchall():
            t = Tuberia(tuberia["x"], tuberia["altura"])