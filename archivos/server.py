import socket
import sys
import datetime
import pyautogui
from pyautogui import press, typewrite, hotkey

quieto = True
salto = False
vuelta = True
ultima = 0
estado = 0
frames = 0
lista = []
promedio = []
girx = False
agachado = False
basura = 0
nogires = False
bien = False

while True:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_address = ('0.0.0.0', 10000)
    sock.bind(server_address)
    sock.listen(1)

    print ("Escuchando")
    connection, client_address = sock.accept()
    connection.settimeout(2.0)
    print ("Conectado")

    message=""
    while True:
        try:
            data = connection.recv(1)
        except:
            break
        data=data.decode('utf-8')
        if data=="|":
            message=""
        elif data=="$":
            datos=eval(message.split("@")[0])
            distancia=message.split("@")[1]

            frames += 1
            if frames == 1:
                pyautogui.press('b')
            if frames > 15:

                lista = lista[-7:]
                giro = lista[-5:]

                nogires = False
                for i in giro:
                    if i == "w":
                        nogires = True

                if datos['GyX'] < 0:
                    datos['GyX'] = datos['GyX'] * -1
                if datos['GyX'] > 24500 and vuelta is True and nogires is False:
                    vuelta = False
                    pyautogui.press('p')
                    lista.append("p")
                elif datos['GyX'] > 24500 and vuelta is False and nogires is False:
                    lista.append("p")
                else:
                    lista.append("r")
                    vuelta = True
                lista = lista[-7:]
                giro = lista[-3:]
                girx = False
                for i in giro:
                    if i == "p":
                        girx = True

                distancia = float (distancia)

                if frames < 40:
                    if distancia > 100 or distancia < 75:
                        basura += 1
                    else:
                        promedio.append(distancia)

                if basura >= 3 and frames == 40:
                    pyautogui.press('n')
                    print("Mal calibrado")
                    frames = -15
                    basura = 0
                elif frames == 40:
                    pyautogui.press('m')
                    bien = True
                    print("Bien calibrado")
                if bien and frames == 50:
                    pyautogui.press('c')

                if frames == 40:
                    avg = sum(promedio)/len(promedio)

                if frames > 40:
                    if distancia > avg + 40:
                        distancia = avg
                    elif distancia < avg - 25:
                        distancia = avg

                if frames > 40:
                    salto = False
                    for i in lista:
                        if i == "w":
                            salto = True
                    if distancia < avg - 6 and estado == 0:
                        estado = 1
                        girx = True
                    elif distancia > avg + 12 and estado == 1:
                        if salto is False:
                            lista.append("w")
                            pyautogui.press('x')
                    elif distancia > avg - 6 and estado == 1:
                        estado = 2
                    elif distancia > avg + 12 and estado == 2:
                        if salto is False:
                            lista.append("w")
                            pyautogui.press('x')
                    elif estado == 1:
                        estado = 0

                    if frames > 40 and distancia > avg + 12:
                        girx = False

                    ultima = distancia
                    if datos['AcX'] > -17500 and datos['AcX'] < -13800:
                        #print("quieto")
                        pyautogui.press('e')
                        lista.append("e")
                    elif girx is False and salto is False:
                        #print("mueve")
                        pyautogui.press('q')
                        lista.append("q")
                    else:
                        pyautogui.press('e')
        else:
            message=message+data
    print ("Desconectado")
    connection.close()
    sock.shutdown(1)
    sock.close()
