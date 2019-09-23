#!/usr/bin/python3
import socket
import sys


serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 9999

serverSocket.bind((host, port))
print('listing...')
serverSocket.listen()

while True:
    sock , addr = serverSocket.accept()
    print('client addr = %s ' % str(addr))
    msg = 'welcome!\r\n'
    sock.send((msg.encode('utf-8')))
    sock.close()


