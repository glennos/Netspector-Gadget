#!/usr/bin/env python
__author__ = 'root'

import socket, sys
from Bob import sniffer_test

def client():
    x = True
    while x is True:
        try:
            s = socket.socket()

            addr = input("Geef ip adres op (zoals 192.168.0.1): ")
            port = 12345
            s.connect((addr, port))

            while True:
                packets = s.recv(65565)
                if packets:
                    sniffer_test.snifferformat(packets)
        except KeyboardInterrupt:
            print('\nConnection Closed to', addr, '\n')
            x = False
            return x
        finally:
            s.close()