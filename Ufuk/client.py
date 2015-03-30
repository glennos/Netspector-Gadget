__author__ = 'Ufuk'

import socket
import sys
from pip._vendor.distlib.compat import raw_input
import network_sniffer


def localclient():
    s = socket.socket()
    host = socket.gethostname()
    port = 12345

    s.connect((host, port))
    while True:
        print(s.recv(1024))
        network_sniffer.sniffer(s)
    s.close


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
    print(" "*28 + "1: Sniffer Local Client")
    print(" "*28 + "2: Sniffer Remote Client")
    print(" "*28 + "3: ")
    print(" "*28 + "4: ")
    print(" "*28 + "0: Go back")
    print()
    input = optie_input = raw_input(" "*28 + "Kies een optie: ",)
    print(optie_input)
    print(c + h*78 + c)
    if optie_input == '1':
        print(localclient())
    if optie_input == '2':
        print(remoteclient())
    if optie_input == '3':
        print()
    elif optie_input == '0':
        sys.exit(0)

# s = socket.socket()
# host = socket.gethostname()
# port = 12345

# s.connect((host, port))
# print(s.recv(1024))
# s.close