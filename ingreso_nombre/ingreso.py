from ingreso_nombre.Clases import *

def ingreso():

    Controlador.iniciar()

    Colores = {'Negro': (0, 0, 0), "Blanco": (255, 255, 255), "Verde": (50, 205, 50),
               "Rojo": (178, 34, 34), "Naranja": (255, 165, 0), "Amarillo": (255, 215, 0),
               "Celeste": (0, 255, 255), "Azul": (0, 0, 255)}

    ancho, alto = 1360, 720

    FPS = 120

    ventana = Controlador.configurar_pantalla(ancho, alto)

    Controlador.rellenar_pantalla(ventana, Colores)

    reloj = Controlador.iniciar_reloj()

    Nombre_Texto = ""

    Letras = ""

    frames_totales = 0

    frames_aux = 0

    posicion_texto = 0

    frames_escritura = 0

    crecimiento = 0

    Titulo = Palabra(30, 20, Colores["Blanco"], "ingrese  su  nombre", 90)

    aux = 0

    posx = 280

    x = posx

    posy = 280

    y = posy

    frame_termino = None
    termino = False

    Lista_Letras = []

    Nombre = " "

    Controlador.Inicializacion_Final()

    animacion = False
    otros_frames = frames_totales
    contador = 0
    final = False

    while True:
        Controlador.set_fps(reloj, FPS)

        if termino is False:
            Letras = Controlador.buscar_eventos(Colores)
            if Letras is False:
                for letra in Lista_Letras:
                    Nombre += str(letra.texto)
                frame_termino = frames_totales
                termino = True
            elif Letras is not None and Letras is not True:
                if len(Lista_Letras) <= 7:
                    Letras.posX = posx
                    Letras.posY = posy
                    if Letras.texto != " ":
                        Lista_Letras.append(Letras)
                        aux += 1
                        posx += 100
                if Letras.texto == " " and len(Lista_Letras):
                    Lista_Letras.remove(Lista_Letras[aux-1])
                    aux -= 1
                    posx -= 100

            Controlador.rellenar_pantalla(ventana, Colores)
            for letra in Lista_Letras:
                ventana.blit(letra.Palabra, (letra.posX, letra.posY))

            ventana.blit(Titulo.Palabra, (Titulo.posX, Titulo.posY))
            pygame.draw.rect(ventana, Colores["Blanco"], (x, y + 95, 50, 20))
            pygame.draw.rect(ventana, Colores["Blanco"], (x + 100, y + 95, 50, 20))
            pygame.draw.rect(ventana, Colores["Blanco"], (x + 200, y + 95, 50, 20))
            pygame.draw.rect(ventana, Colores["Blanco"], (x + 300, y + 95, 50, 20))
            pygame.draw.rect(ventana, Colores["Blanco"], (x + 400, y + 95, 50, 20))
            pygame.draw.rect(ventana, Colores["Blanco"], (x + 500, y + 95, 50, 20))
            pygame.draw.rect(ventana, Colores["Blanco"], (x + 600, y + 95, 50, 20))
            pygame.draw.rect(ventana, Colores["Blanco"], (x + 700, y + 95, 50, 20))
        else:
            if frame_termino + 350 < frames_totales and final is False:
                final = True
                animacion = True

        if animacion and otros_frames + 6 < frames_totales:
            Base.sprites.add(Base.fondo[contador])
            if contador == 17:
                animacion = False
            contador += 1
            otros_frames = frames_totales

        if contador == 18:
            if otros_frames + 100 < frames_totales:
                for item in Base.sprites:
                    Base.sprites.remove(item)
                return True

        Base.sprites.draw(ventana)

        pygame.display.update()
        frames_totales += 1