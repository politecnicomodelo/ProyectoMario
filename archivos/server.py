import socket
import sys
import datetime
import pyautogui
from pyautogui import press, typewrite, hotkey

quieto = True
estado_salto = 0
vuelta = True
while True:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_address = ('0.0.0.0', 10000)
    sock.bind(server_address)
    sock.listen(1)

    print ("Escuchando xd")
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
            datos=eval(message)

            if datos['GyX'] < 0:
                datos['GyX'] = datos['GyX'] * -1
            print(datos['GyX'])
            if datos['GyX'] > 17000 and vuelta is True:
                vuelta = False
                pyautogui.press('p')
            elif datos['GyX'] > 17000 and vuelta is False:
                pass
            else:
                vuelta = True

            nuevo = 8000 + datos['AcX']
            if nuevo >= 5000:
              estado_salto += 1
            else:
               estado_salto = 0
               salto = False
            #print(nuevo)

            if estado_salto >= 2:
               estado_salto = 0
               #print(" --- SALTO --- ")
               pyautogui.press('w')
            else:

                if datos['AcX'] > -16400 and datos['AcX'] < -14200:
                    pyautogui.press('u')
                    #print("quieto")
                else:
                    if vuelta:
                        pyautogui.press('right')
                        #print("muevo")
        else:
            message=message+data
    print ("Desconectado")
    connection.close()
    sock.shutdown(1)
    sock.close()
