import socket
import sys
import datetime
import pyautogui
from pyautogui import press, typewrite, hotkey

quieto = True
salto = False
vuelta = True
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

    ultima = 0
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
            if datos['GyX'] < 0:
                datos['GyX'] = datos['GyX'] * -1
            if datos['GyX'] > 17000 and vuelta is True:
                vuelta = False
                pyautogui.press('p')
            elif datos['GyX'] > 17000 and vuelta is False:
                pass
            else:
                vuelta = True

            ultima = str (ultima)
            print (ultima)
            ultima = float (ultima)
            print (distancia)
            distancia = float(distancia)
            if ultima < distancia + 35.0:
                salto = True
            ultima = distancia
            if salto:
                pass
                #print ("--------------SALTO---------------")
            else:
                salto = False
                if datos['AcX'] > -16400 and datos['AcX'] < -14200:
                    pyautogui.press('e')
                else:
                    if vuelta:
                        pyautogui.press('q')
        else:
            message=message+data
    print ("Desconectado")
    connection.close()
    sock.shutdown(1)
    sock.close()
