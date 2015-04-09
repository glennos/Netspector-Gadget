#!/usr/bin/env python3

import socket
import sys
from library import functions


def sniffer(remote, address):
    # Maakt AF_PACKET type raw socket (packet niveau)
    # ETH_P_ALL    0x0003 (alle paketten)
    try:
        so = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(0x0003))
    except socket.error as msg:
        print('Socket kon niet worden opgebouwd. Fout Code : ' + str(msg[0]) + ' Bericht ' + msg[1])
        sys.exit()

    # Pakketjes ontvangen
    packet = so.recvfrom(65565)

    # Van een tuple naar een string
    packet = packet[0]

    # Als er een packet in zit, dan versturen
    if packet:
        remote.send(packet)
        functions.snifferformattofile(packet, address)


def server():
    x = True
    while x is True:
        print('Server is aan het luisteren')
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

            host = '0.0.0.0'        # Koppelen aan een adres
            port = 12345            # Poort waarop de socket bereikbaar is
            s.bind((host, port))

            s.listen(5)
            c, addr = s.accept()
            print('Heeft connectie vanaf', addr)

            while True:
                sniffer(c, addr)

        # Aantal error handlers
        except KeyboardInterrupt:
            x = False
            return x
        except BrokenPipeError:
            print('Connectie gesloten vanaf', addr)
        except ConnectionResetError:
            print('Connectie gesloten vanaf', addr)
        finally:
            s.close()