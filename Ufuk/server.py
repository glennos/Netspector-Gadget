__author__ = 'Ufuk'

import socket

s = socket.socket()
host = socket.gethostname()
port = 12345
s.bind((host, port))

s.listen(5)
while True:
    conn, addr = s.accept()
    print("Got connection from", addr)
    conn.send("Connection Established!".encode('utf-8'))
    while True:
        data = conn.recv(1024)
        print(data)