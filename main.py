import pygame
from clases.Mario import Mario
from clases.Bloques import Bloque
from clases.Signos import Signo
from clases.Piso import Piso

ancho = 1280
alto = 720

Monedas=0
Vidas=0

Activos=pygame.sprite.Group()
Marios=pygame.sprite.Group()
Pisos=pygame.sprite.Group()

mario = Mario()
mario.add(Marios)

piso1=Piso(0, 695,"imagenes/piso1.png")
piso2=Piso(4297,695,"imagenes/piso2.png")
piso3=Piso(5736,695,"imagenes/piso3.jpg")
piso4=Piso(10819,695,"imagenes/piso4.png")
piso1.add(Pisos)
piso2.add(Pisos)
piso3.add(Pisos)
piso4.add(Pisos)

bloque1=Bloque(582, 444)
bloque1.add(Activos)

bloque2=Bloque(728, 444)
bloque2.add(Activos)

bloque3=Bloque(874, 444)
bloque3.add(Activos)

bloque4=Bloque(4862, 444)
bloque4.add(Activos)

bloque5=Bloque(4935, 444)
bloque5.add(Activos)

bloque6=Bloque(5008, 444)
bloque6.add(Activos)

bloque7=Bloque(5081, 252)
bloque7.add(Activos)

bloque8=Bloque(5154, 252)
bloque8.add(Activos)

bloque9=Bloque(5227, 252)
bloque9.add(Activos)

bloque10=Bloque(5300, 252)
bloque10.add(Activos)

bloque11=Bloque(5373, 252)
bloque11.add(Activos)

bloque12=Bloque(5446, 252)
bloque12.add(Activos)

bloque13=Bloque(5519, 252)
bloque13.add(Activos)

bloque14=Bloque(5592, 252)
bloque14.add(Activos)

bloque15=Bloque(5665, 252)
bloque15.add(Activos)

bloque16=Bloque(5929, 252)
bloque16.add(Activos)

bloque17=Bloque(6002, 252)
bloque17.add(Activos)

bloque18=Bloque(6075, 252)
bloque18.add(Activos)

bloque19=Bloque(6603, 444)
bloque19.add(Activos)

bloque20=Bloque(6676, 444)
bloque20.add(Activos)

bloque21=Bloque(6749, 444)
bloque21.add(Activos)

bloque22=Bloque(8119, 444)
bloque22.add(Activos)

bloque23=Bloque(8365, 252)
bloque23.add(Activos)

bloque24=Bloque(8438, 252)
bloque24.add(Activos)

bloque25=Bloque(8511, 252)
bloque25.add(Activos)

bloque23=Bloque(8822, 252)
bloque23.add(Activos)

bloque23=Bloque(9041, 252)
bloque23.add(Activos)

bloque24=Bloque(8895, 444)
bloque24.add(Activos)

bloque25=Bloque(8968, 444)
bloque25.add(Activos)

bloque26=Bloque(11995, 444)#roberto2
bloque26.add(Activos)

bloque27=Bloque(12068, 444)
bloque27.add(Activos)

bloque28=Bloque(12214, 444)
bloque28.add(Activos)

signo9=Signo(8895, 252)
signo9.devuelve(mario, False, True, Activos, Monedas)
signo9.add(Activos)

signo10=Signo(8968, 252)
signo10.devuelve(mario, False, True, Activos, Monedas)
signo10.add(Activos)

signo11=Signo(12141, 444)
signo11.devuelve(mario, False, True, Activos, Monedas)
signo11.add(Activos)

signo4=Signo(6148, 252)
signo4.devuelve(mario, False, True, Activos, Monedas)
signo4.add(Activos)

signo5=Signo(7210, 444)
signo5.devuelve(mario, False, True, Activos, Monedas)
signo5.add(Activos)

signo6=Signo(7435, 444)
signo6.devuelve(mario, False, True, Activos, Monedas)
signo6.add(Activos)

signo7=Signo(7663, 444)
signo7.devuelve(mario, False, True, Activos, Monedas)
signo7.add(Activos)

signo8=Signo(7435, 252)
signo8.devuelve(mario, False, True, Activos, Monedas)
signo8.add(Activos)

signo1=Signo(801, 444)
signo1.devuelve(mario, False, True, Activos, Monedas)
signo1.add(Activos)

signo2=Signo(725, 252)
signo2.devuelve(mario, False, True, Activos, Monedas)
signo2.add(Activos)

signo3=Signo(655, 444)
signo3.devuelve(mario, False, True, Activos, Monedas)
signo3.add(Activos)

listaSignos=[signo1, signo2, signo3, signo4, signo5, signo6, signo7, signo8, signo9, signo10, signo11]
listaBloques=[bloque1, bloque2, bloque3, bloque4, bloque5,bloque6,bloque7,bloque8,bloque9,bloque10,bloque11,bloque12,
bloque13,bloque14,bloque15,bloque16,bloque17,bloque18,bloque19,bloque20,bloque21,bloque22,bloque23,bloque24,bloque25,
bloque26,bloque27,bloque28]


def main():

    reloj=pygame.time.Clock()
    fondo = pygame.image.load("imagenes/fondo.jpg")
    screen = pygame.display.set_mode((ancho, alto), pygame.FULLSCREEN)
    pygame.display.set_caption("Super Mega Mario Bros")
    x = 0
    y = 0
    muevePantalla = False

    while True:
        for eventos in pygame.event.get():
            if eventos.type == pygame.K_ESCAPE:
                quit()

        teclas = pygame.key.get_pressed()

        if muevePantalla == True:
            x -= 30
            for item in Activos:
                item.rect.x -= 30
            for item in Pisos:
                item.rect.x -= 30

        muevePantalla = mario.mover(teclas, muevePantalla, Activos, Pisos)

        for item in listaSignos:
            item.devuelve(mario, False, True, Activos, Monedas)
        for item in listaBloques:
            item.devuelveBloque(mario)

        if mario.rect.x == 10000:
            ganarJuego(mario)
        screen.blit(fondo, (x, y))
        Activos.draw(screen)
        Marios.draw(screen)
        Pisos.draw(screen)
        pygame.display.flip()
        reloj.tick(60)

def ganarJuego(mario):
    x=0
    #Animacion de victoria

if __name__ == '__main__':
    pygame.init()
    main()