__author__ = 'Ufuk'

import socket
import sys
from Ufuk import nsg_server_switch
from pip._vendor.distlib.compat import raw_input


def localclient():
    s = socket.socket()
    try:
        host = socket.gethostname()
        port = 12345
        s.connect((host, port))

        packet = s.recv(1024)

        while packet() is True:
            s.send(packet.decode('utf-8'))
    except KeyboardInterrupt:
        s.close()
    finally:
        s.shutdown(1)
        s.close()


def remoteclient():
    host = raw_input(" "*28 + "Please give the IP address of the remote client :  ",)
    print(host)
    port = raw_input(" "*28 + "Please give the Port address of the socket :  ",)
    print(port)

    s = socket.socket()
    s.connect(host, port)

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
        nsg_server_switch()
    if optie_input == '2':
        print()
    if optie_input == '3':
        print()
    elif optie_input == '0':
        sys.exit(0)