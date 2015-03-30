#!/usr/bin/env python
__author__ = 'root'


import socket, sys
from struct import *

def sniffer(remote):
    # create an INET, STREAMing socket
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
    except socket.error as msg:
        print('Socket could not be created. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
        sys.exit()

    while True:
        packet = s.recvfrom(65565)

        # packet string from tuple
        packet = packet[0]
        remote.sendall(packet)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 12345
s.bind((host, port))

s.listen(5)
while True:
    try:
        c, addr = s.accept()
        print('Got connection from', addr)
        while 1:
            sniffer(c)
    except KeyboardInterrupt:
        s.send("End")
    finally:
        s.close()

