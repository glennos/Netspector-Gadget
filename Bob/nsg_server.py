#!/usr/bin/env python
__author__ = 'root'


import socket, sys
from struct import *


def sniffer(remote):
    # create an INET, STREAMing socket
    try:
        so = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
    except socket.error as msg:
        print('Socket could not be created. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
        sys.exit()

    # receive a packet
    while True:
        packet = so.recvfrom(65565)

        # packet string from tuple
        packet = packet[0]

        remote.send(packet)

s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

try:
    host = socket.gethostname()
    port = 12345
    s.bind((host, port))

    s.listen(5)
    c, addr = s.accept()

    while True:
        print('Got connection from', addr)
        sniffer(c)
finally:
    s.close()