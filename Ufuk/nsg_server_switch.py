__author__ = 'Ufuk'

import socket
import sys
from Ufuk import network_sniffer
from pip._vendor.distlib.compat import raw_input


def startsniffer():
    s = socket.socket()
    host = socket.gethostname()
    port = 12345
    s.bind((host, port))
    s.listen(5)

    conn, addr = s.accept()
    print("Got connection from", addr)
    conn.send("Connection Established!".encode('utf-8'))

    try:
        network_sniffer.sniffer(s)
        while network_sniffer.sniffer(s) is True:
            for packet in network_sniffer.sniffer(s):
                conn.send(packet)
    except KeyboardInterrupt:
        s.close()

c = "+"
h = "-"

while True:
    print(c + h*78 + c)
    print(" "*28 + "1: Start Sniffer")
    print(" "*28 + "2: ")
    print(" "*28 + "3: ")
    print(" "*28 + "4: ")
    print(" "*28 + "0: Go back")
    print()
    input = optie_input = raw_input(" "*28 + "Kies een optie: ",)
    print(optie_input)
    print(c + h*78 + c)
    if optie_input == '1':
        startsniffer()
    if optie_input == '2':
        print()
    if optie_input == '3':
        print()
    elif optie_input == '0':
        sys.exit(0)