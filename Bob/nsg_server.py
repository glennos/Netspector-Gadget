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
    packet = so.recvfrom(65565)

    # create string
    packet = packet[0]

    if packet:
        remote.send(packet)


def server():
    x = True
    while x is True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

            host = '0.0.0.0'
            port = 12345
            s.bind((host, port))

            s.listen(5)
            c, addr = s.accept()
            print('Got connection from', addr)

            while True:
                sniffer(c)
        # except KeyboardInterrupt:
        #     x = False
        #     return x
        except BrokenPipeError:
            print('Connection Closed from', addr)
        except ConnectionResetError:
            print('Connection Closed from', addr)
        except:
            x = False
            return x
        finally:
            s.close()



