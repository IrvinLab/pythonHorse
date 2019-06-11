# -*- coding: utf-8 -*-
import socket, os

cmd = ''
UDP_PORT = 5005
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) 
sock.bind(('', UDP_PORT))
try:
    while True:
        data = sock.recv(4098)
        if not data:
            break
        if data == b'ifconfig':
            cmd = os.system('ipconfig')
            sock.send(cmd)
except KeyboardInterrupt:
    sock.close()