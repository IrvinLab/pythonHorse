# -*- coding: utf-8 -*-
import socket
from time import sleep

UDP_PORT = 5005
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.connect(('localhost', UDP_PORT))

try:
    sock.send(b'ifconfig')
    data = sock.recv(4098)
    print(data)

except KeyboardInterrupt:
    print("Exit")
    sock.close()