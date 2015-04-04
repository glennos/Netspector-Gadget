__author__ = 'Ufuk'

import socket
import sys
from Ufuk import network_sniffer
from pip._vendor.distlib.compat import raw_input


def startsniffer():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
    except socket.error as msg:
        print('Socket could not be created. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
        sys.exit()

    try:
        host = socket.gethostname()
        port = 12345
        s.bind((host, port))

        s.listen(5)
        connection, address = s.accept()
        print("Got connection from", address)
        connection.send("Connection Established!".encode('utf-8'))

        network_sniffer.sniffer(s)
        while network_sniffer.sniffer(s) is True:
            for packet in network_sniffer.sniffer(s):
                connection.send(packet.encode('utf-8'))
    except KeyboardInterrupt:
        s.close()
    finally:
        s.shutdown(1)
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