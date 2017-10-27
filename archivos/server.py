import socket
import sys
import datetime
import pyautogui
from pyautogui import press, typewrite, hotkey

estado_salto = 0
estado_quieto = 0
estado_derecha = 0
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
            datos=eval(message)

            nuevo = 8000 + datos['AcX']
            if nuevo >= 1000:
                estado_salto += 1
            else:
                
                print()
                estado_salto = 0

            if estado_salto >= 3:
                estado_salto = 0
                print(" --- SALTO --- ")                
                #pyautogui.press('w')

            else:
                if datos['AcX'] > -16000 and datos['AcX'] < -14800:
                    pass
                    #pyautogui.press('u')
                else:
                    pass
                    #pyautogui.press('right')
        else:
            message=message+data
    print ("Desconectado")
    connection.close()
    sock.shutdown(1)
    sock.close()
