#!/usr/bin/env python
__author__ = 'root'


import socket, sys
from struct import *

def sniffer():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as msg:
        print('Socket could not be created. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
        sys.exit()

    host = socket.gethostname()
    port = 12345
    s.bind((host, port))

    s.listen(5)

    while 1:
        try:
            c, addr = s.accept()
            print('Got connection from', addr)

            # create an INET, STREAMing socket
            try:
                so = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
            except socket.error as msg:
                print('Socket could not be created. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
                sys.exit()
            while 1:
                packet = so.recvfrom(65565)
                # packet string from tuple
                packet = packet[0]
                if packet:
                    c.send(packet)
        except socket.error:
            break
        except KeyboardInterrupt:
            s.close()
            break

while 1:
    try:
        sniffer()
    except socket.error:
        break

