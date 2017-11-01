from indicaciones.Clases import *

def indicaciones():

    Controlador.iniciar()

    Colores = {'Negro': (0, 0, 0), "Blanco": (255, 255, 255), "Verde": (50, 205, 50),
               "Rojo": (178, 34, 34), "Naranja": (255, 165, 0), "Amarillo": (255, 215, 0),
               "Celeste": (0, 255, 255), "Azul": (0, 0, 255)}
    #(255, 0, 0)}

    ancho, alto = 1360, 720

    FPS = 120

    ventana = Controlador.configurar_pantalla(ancho, alto)

    Controlador.rellenar_pantalla(ventana, Colores)

    reloj = Controlador.iniciar_reloj()

    Lista_Primer_Oracion = ["l", "o", "s", "               ", "r" , "e", "p", "r", "e", "s", "e", "n", "t", "a", "n",
                            "  ", "t", "u", "s", "  ", "v", "i", "d", "a", "s", "."]

    Lista_Segunda_Oracion = ["l","o","s","               ", "t","e","  ","a","g","r","e","g","a","n","  ","u","n"]

    Lista_Tercera_Oracion = ["s", "a", "l", "t", "a", "  ", "d", "e", "b", "a", "j", "o", "  ",
                             "d", "e", "  ", "e", "s", "t", "o", "s", "                ",
                             "p", "a", "r", "a", "  ", "o", "b","t","e","n","e","r","            ", "o"]

    Lista_Cuarta_Oracion = ["c","u","i","d","a","d","o","  ","c","o","n","  ","l","o","s",
                            "               ","q","u","e","  ","t","e","  ","s","a","c","a","n",]

    Ayuda_Texto = "ayuda  a  mario  a  llegar  al  poli"

    Primer_Oracion_texto = ""

    Segunda_Oracion_texto = ""

    Tercera_Oracion_texto = ""

    Cuarta_Oracion_texto = ""

    frames_totales = 0

    Ayuda = Palabra(80, 100, Colores["Blanco"], Ayuda_Texto, 80)

    Primer_Oracion = Palabra(80, 300, Colores["Blanco"], Primer_Oracion_texto, 50)

    Segunda_Oracion = Palabra(80, 400, Colores["Blanco"], Segunda_Oracion_texto, 50)

    Tercera_Oracion = Palabra(80, 500, Colores["Blanco"], Tercera_Oracion_texto, 50)

    Cuarta_Oracion = Palabra(80, 600, Colores["Blanco"], Cuarta_Oracion_texto, 50)

    posicion_h1 = 0

    posicion_h2 = 0

    posicion_h3 = 0

    posicion_h4 = 0

    frames_escritura = 0

    frames_temporales = 0

    frames_entre_escritura = 0

    crecimiento = 0

    Primera = True

    Segunda = False

    Tercera = False

    Cuarta = False

    frames_finales = 6000000000000000

    aux = True

    Enemigo = Sprite(485, 590, 60, 60, "indicaciones/Enemigo.png")

    Corazon = Sprite(190, 290, 60, 60, "indicaciones/Corazon.png")

    Corazon_2 = Sprite(645, 390, 60, 60, "indicaciones/Corazon.png")

    Corazon_3 = Sprite(915, 590, 60, 60, "indicaciones/Corazon.png")

    Moneda = Sprite(1080, 490, 60, 60, "indicaciones/Moneda_1.png")

    Hongo = Sprite(190, 390, 60, 60, "indicaciones/hongo.png")

    Hongo_2 = Sprite(1190, 490, 60, 60, "indicaciones/hongo.png")

    Signo = Sprite(655, 490, 60, 60, "indicaciones/signo.png")

    while True:
        Controlador.set_fps(reloj, FPS)
        Controlador.buscar_eventos()
        Controlador.rellenar_pantalla(ventana, Colores)

        if frames_entre_escritura + 150 < frames_totales:

            if Primera and frames_escritura + 15 < frames_totales:
                frames_escritura = frames_totales
                Primer_Oracion_texto += Lista_Primer_Oracion[posicion_h1]
                Primer_Oracion.Escritura(Colores["Blanco"], Primer_Oracion_texto, False)
                posicion_h1 += 1
                if posicion_h1 == 4:
                    Base.Grupo.add(Corazon)

            if Primera and posicion_h1 >= 26:
                frames_escritura = frames_totales
                frames_entre_escritura = frames_totales
                Segunda = True
                Primera = False

            if Segunda and frames_escritura + 15 < frames_totales:
                frames_escritura = frames_totales
                Segunda_Oracion_texto += Lista_Segunda_Oracion[posicion_h2]
                Segunda_Oracion.Escritura(Colores["Blanco"], Segunda_Oracion_texto, False)
                posicion_h2 += 1
                if posicion_h2 == 4:
                    Base.Grupo.add(Hongo)
                if posicion_h2 == 17:
                    Base.Grupo.add(Corazon_2)

            if Segunda and posicion_h2 >= 17:
                frames_escritura = frames_totales
                frames_entre_escritura = frames_totales
                Segunda = False
                Tercera = True

            if Tercera and frames_escritura + 15 < frames_totales:
                frames_escritura = frames_totales
                Tercera_Oracion_texto += Lista_Tercera_Oracion[posicion_h3]
                Tercera_Oracion.Escritura(Colores["Blanco"], Tercera_Oracion_texto, False)
                posicion_h3 += 1
                if posicion_h3 == 22:
                    Base.Grupo.add(Signo)
                if posicion_h3 == 34:
                    Base.Grupo.add(Moneda)
                if posicion_h3 == 36:
                    Base.Grupo.add(Hongo_2)

            if Tercera and posicion_h3 >= 36:
                frames_escritura = frames_totales
                frames_entre_escritura = frames_totales
                Tercera = False
                Cuarta = True

            if Cuarta and frames_escritura + 15 < frames_totales:
                frames_escritura = frames_totales
                Cuarta_Oracion_texto += Lista_Cuarta_Oracion[posicion_h4]
                Cuarta_Oracion.Escritura(Colores["Blanco"], Cuarta_Oracion_texto, False)
                posicion_h4 += 1
                if posicion_h4 == 15:
                    Base.Grupo.add(Enemigo)
                if posicion_h4 == 28:
                    Base.Grupo.add(Corazon_3)

            if Cuarta and posicion_h4 >= 28:
                frames_escritura = frames_totales
                frames_entre_escritura = frames_totales
                frames_finales = frames_totales
                Cuarta = False

        if frames_finales + 500 < frames_totales:
            return True

        ventana.blit(Ayuda.Palabra, (Ayuda.posX, Ayuda.posY))
        ventana.blit(Primer_Oracion.Palabra, (Primer_Oracion.posX, Primer_Oracion.posY))
        ventana.blit(Segunda_Oracion.Palabra, (Segunda_Oracion.posX, Segunda_Oracion.posY))
        ventana.blit(Tercera_Oracion.Palabra, (Tercera_Oracion.posX, Tercera_Oracion.posY))
        ventana.blit(Cuarta_Oracion.Palabra, (Cuarta_Oracion.posX, Cuarta_Oracion.posY))
        Base.Grupo.draw(ventana)
        pygame.display.update()
        frames_totales += 1