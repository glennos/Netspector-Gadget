#!/usr/bin/env python3

import socket

def connect_socket():
    x = True
    while x is True:

        try:
            # Maakt een AF_INET, STREAM socket (TCP)
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        except socket.error as msg:
            print('Het is niet gelukt om een socket op te bouwen. Fout code: ' + str(msg[0]) + ' , Error message : ' + msg[1])


        try:
            host = input("Geef naam op, bijv www.google.com: ")
            port = 80

        except KeyboardInterrupt:
            print('Connectie gesloten')
            x = False
            return x

        try:
            remote_ip = socket.gethostbyname(host)

            print('Ip address van ' + host + ' is ' + remote_ip)

            # Connect to remote server
            s.connect((remote_ip, port))

            print('Socket connectie opgebouwd naar ' + host + ' op ip ' + remote_ip + ':80')
            print()

        except socket.gaierror:
            # resolve error
            print(host +' kon niet worden vertaald')
            print()

        except ConnectionRefusedError:
            print('Connectie geweigerd')
            print()

        except OSError:
            print('Foutieve invoer')
            print()


