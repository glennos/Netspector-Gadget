#!/usr/bin/env python
__author__ = 'root'

import socket

s = socket.socket()
host = "localhost"
port = 12345

s.connect((host, port))
print(s.recv(1025))
s.close

