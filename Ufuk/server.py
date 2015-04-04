__author__ = 'Ufuk'

import socket
import sys
from Ufuk import nsg_server_switch
from pip._vendor.distlib.compat import raw_input

def startServer():
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
            packet = ""
            data = conn.recv(1024)
            for packet in data:
                print(packet)
            else:
                print("No more packets!")

c = "+"
h = "-"

while True:
    print(c + h*78 + c)
    print(" "*28 + "1: Start Server")
    print(" "*28 + "2: ")
    print(" "*28 + "3: ")
    print(" "*28 + "4: ")
    print(" "*28 + "0: Go back")
    print()
    input = optie_input = raw_input(" "*28 + "Kies een optie: ",)
    print(optie_input)
    print(c + h*78 + c)
    if optie_input == '1':
        startServer()
    if optie_input == '2':
        print()
    if optie_input == '3':
        print()
    elif optie_input == '0':
        sys.exit(0)