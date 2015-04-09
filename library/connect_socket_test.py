#!/usr/bin/env python3

import socket
import sys


def connect_socket():
    try:
        # Maakt een AF_INET, STREAM socket (TCP)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as msg:
        print('Het is niet gelukt om een socket op te bouwen. Fout code: ' + str(msg[0]) + ' , Error message : ' + msg[1])
        sys.exit()

    print("Socket Created")

    host = input("Geef naam op (zoals www.google.com: ")
    port = 80

    try:
        remote_ip = socket.gethostbyname(host)

    except socket.gaierror:
        # resolve error
        print('Naam (hostname) kon niet worden vertaald')
        sys.exit()

    print('Ip address van ' + host + ' is ' + remote_ip)

    # Connect to remote server
    s.connect((remote_ip, port))

    print('Socket Connected naar ' + host + ' op ip ' + remote_ip)