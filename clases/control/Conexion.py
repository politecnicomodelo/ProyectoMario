import pymysql
from clases.Ladrillos import Ladrillo
from clases.Signos import Signo
from clases.Monedas import Moneda
from clases.Goombas import Goomba
from clases.Escaleras import Escalera
from clases.Tuberia import Tuberia
from clases.Mastil import Mastil

class Conexion(object):

    db = None
    cursor_bloques = None
    cursor_tuberias = None

    def __init__(self):
        self.db = pymysql.connect(host ="172.16.2.250", user = "root", passwd = "alumno", autocommit = True)
        self.cursor_bloques = self.db.cursor(pymysql.cursors.DictCursor)
        self.cursor_tuberias = self.db.cursor(pymysql.cursors.DictCursor)
        self.c = self.db.cursor(pymysql.cursors.DictCursor)
        self.cursor_tuberias.execute("Use Mario")

    def cargar_nivel(self):

        self.cursor_bloques.execute("SELECT * FROM Bloque")

        for bloque in self.cursor_bloques.fetchall():
            if bloque["tipo"] == "Ladrillo1":
                l = Ladrillo(bloque["x"], bloque["y"], False)
            if bloque["tipo"] == "Ladrillo2":
                l = Ladrillo(bloque["x"], bloque["y"], True)
            if bloque["tipo"] == "SignoH":
                s = Signo(bloque["x"], bloque["y"], True)
            if bloque["tipo"] == "SignoM":
                s = Signo(bloque["x"], bloque["y"], False)
            if bloque["tipo"] == "Moneda":
                m = Moneda(bloque["x"], bloque["y"], False)
            if bloque["tipo"] == "Goomba":
                g = Goomba(bloque["x"], bloque["y"])
            if bloque["tipo"] == "Escalera":
                e = Escalera(bloque["x"], bloque["y"], True)
            if bloque["tipo"] == "Escalera2":
                e = Escalera(bloque["x"], bloque["y"], False)
            if bloque["tipo"] == "Mastil":
                e = Mastil(bloque["x"])

        self.cursor_tuberias.execute("SELECT * FROM Tuberia")

        for tuberia in self.cursor_tuberias.fetchall():
            t = Tuberia(tuberia["x"], tuberia["altura"])

    def insertar_datos(self, mario, nombre, puntuacion):
        self.c.execute("insert into Partida values(NULL, '"+nombre+"', '"+str(puntuacion)+"', '"+str(mario.tiempo)+"', '"+str(mario.monedas)+"', '"+str(mario.vidas)+"', 8, 6)")
        self.c.execute("use expo_modelo_2017_computacion")
        self.c.execute("insert into Score values(NULL, 1, '"+nombre+"', '"+str(puntuacion)+"')")
        self.c.execute("use Mario")

    def buscar_posicion(self, puntos):

        self.cursor_bloques.execute("SELECT * FROM Partida ORDER BY puntuacion")
        i = 0
        for partida in self.cursor_bloques.fetchall():
            i += 1
            if int(partida["puntuacion"]) == int(puntos):
                return i
