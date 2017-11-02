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

            # if datos['GyX'] < 0:
            #     datos['GyX'] = datos['GyX'] * -1
            # if datos['GyX'] > 17000 and vuelta is True:
            #     vuelta = False
            #     pyautogui.press('p')
            # elif datos['GyX'] > 17000 and vuelta is False:
            #     pass
            # else:
            #     vuelta = True

            distancia = float (distancia)
            if distancia > 150:
                distancia = 85

            print ("ultimo valor: " + str(ultima))
            print ("valor actual: " + str(distancia))

            if estado == 0 and ultima - 10 >= distancia:
                estado = 1
            elif estado == 1 and ultima + 20 <= distancia:
                salto = True
                estado = 0

            ultima = distancia

            if salto:
                print ("--------------SALTO---------------")

            else:
                salto = False
                estado = 0
                #if datos > -16400 and datos < -14200:
            #         pass
            #         #pyautogui.press('e')
                #else:
            #         if vuelta:
            #             pass
            #             #pyautogui.press('q')

        else:
            message=message+data
    print ("Desconectado")
    connection.close()
    sock.shutdown(1)
    sock.close()
