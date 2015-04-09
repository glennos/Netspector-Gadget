#!/usr/bin/env python3

from os import error
from library import functions
import socket


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
                    functions.snifferformat(packets)

        except KeyboardInterrupt:
            print('Connectie gesloten')
            x = False
            return x

        except error:
            print('Foutieve invoer')
        finally:
            s.close()