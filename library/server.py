#!/usr/bin/env python3
__author__ = 'Bob Korthals, Ufuk Celebi'


import socket
import sys
from library import functions


def sniffer(remote, address):
    # create a AF_PACKET type raw socket (thats basically packet level)
    # define ETH_P_ALL    0x0003          /* Every packet (be careful!!!) */
    try:
        so = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(0x0003))
    except socket.error as msg:
        print('Socket could not be created. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
        sys.exit()

    # receive a packet
    packet = so.recvfrom(65565)

    # create string
    packet = packet[0]

    # Als er een packet in zit, dan versturen
    if packet:
        remote.send(packet)
        functions.snifferformattofile(packet, address)


def server():
    x = True
    while x is True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

            host = '0.0.0.0'        # Bind to any address
            port = 12345
            s.bind((host, port))

            s.listen(5)
            c, addr = s.accept()
            print('Got connection from', addr)

            while True:
                sniffer(c, addr)
        except KeyboardInterrupt:
            x = False
            return x
        except BrokenPipeError:
            print('Connection Closed from', addr)
        except ConnectionResetError:
            print('Connection Closed from', addr)
        finally:
            s.close()




