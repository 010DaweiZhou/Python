#!/usr/bin/python3

import socket
import sys

socketInstance = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

hostname = socket.gethostname()
port = 9999

socketInstance.connect((hostname, port))

msg = socketInstance.recv(1024)
print(msg.decode('utf-8'))
socketInstance.close()