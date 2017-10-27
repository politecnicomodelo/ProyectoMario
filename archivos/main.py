import micropython
import socket
import sys
from machine import I2C, Pin
import mpu6050
import utime

i2c = I2C(sda=Pin(12),scl=Pin(13))
accelerometer = mpu6050.accel(i2c)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('172.16.0.20', 10000)

connected = False
print ("Conectando a Socket...")
while not connected:
    try:
        sock.connect(server_address)
        connected = True
    except Exception as e:
        pass
print ("Conectado a Socket!")
while True:
    sock.sendall("|"+str(accelerometer.get_values())+"$")
    utime.sleep(0.15)
    
sock.close()
         

