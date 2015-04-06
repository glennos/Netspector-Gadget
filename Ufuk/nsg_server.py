#!/usr/bin/env python
from __future__ import print_function
__author__ = 'root'

from pip._vendor.distlib.compat import raw_input
from struct import *
import socket, sys
import os


def sniffer(remote, user_dest_port, address):
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

    # take first 20 characters for the ip header
    ip_header = packet[0:20]

    # now unpack them :)
    iph = unpack('!BBHHHBBH4s4s' , ip_header)

    version_ihl = iph[0]
    version = version_ihl >> 4
    ihl = version_ihl & 0xF
    iph_length = ihl * 4
    ttl = iph[5]
    protocol = iph[6]
    s_addr = socket.inet_ntoa(iph[8])
    d_addr = socket.inet_ntoa(iph[9])
    tcp_header = packet[iph_length:iph_length+20]

    # now unpack them :)
    tcph = unpack('!HHLLBBHHH' , tcp_header)

    source_port = tcph[0]
    dest_port = tcph[1]
    sequence = tcph[2]
    acknowledgement = tcph[3]
    doff_reserved = tcph[4]
    tcph_length = doff_reserved >> 4

    h_size = iph_length + tcph_length * 4
    data_size = len(packet) - h_size

    # get data from the packet
    data = str(packet[h_size:])

    # file = open('client_history', 'a')
    if dest_port != user_dest_port:
        tcppacket = (''
                     + 'Source Port : ' + str(source_port)
                     + '\tDest Port : ' + str(dest_port)
                     + '\tSequence Number : ' + str(sequence)
                     + '\tAcknowledgement : ' + str(acknowledgement)
                     + '\tIp header length : ' + str(tcph_length)
                     + '\tData : ' + data[0:20] + '\n'
                     )
        hostipaddress = address[0]
        hostipport = address[1]
        writeorreadfile(tcppacket, ('History/{0}_{1}'.format(hostipaddress, hostipport)), 'a')


def writeorreadfile(sniffer, file, mode):
    # w = write and replace file content
    # a = append
    # r = read
    if mode == 'w':
        file = open(file, mode)
        file.write(sniffer)
    elif mode == 'a':
        file = open(file, mode)
        file.write(sniffer)
    # elif mode == 'r':
    #     file = open(file, mode)
    #     file.read()
    file.close()


def readfile(file, mode):
    filepath = ('History/{0}').format(file)
    if mode == 'r':
        file = open(filepath, mode)
        for line in file:
            print(line)


def listhistory():
    for file in os.listdir("History/"):
        print(file)


def history():
    c = "+"
    h = "-"
    x = True

    while True:
        print(c + h*86 + c)
        print()
        print(" "*28 + "1: Show list of files")
        print(" "*28 + "2: Read History")
        print(" "*28 + "0: Afsluiten")
        print()
        optie_input = raw_input(" "*28 + "Kies een optie: ",)
        print(optie_input)
        print(c + h*86 + c)
        if optie_input == '1':
            listhistory()
        elif optie_input == '2':
            print("")
        elif optie_input == '0':
            sys.exit(0)


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
                sniffer(c, port, addr)
        except KeyboardInterrupt:
            x = False
            return x
        except BrokenPipeError:
            print('Connection Closed from', addr)
        except ConnectionResetError:
            print('Connection Closed from', addr)
        # except:
        #     x = False
        #     return x
        finally:
            s.close()

c = "+"
h = "-"


def menu_server():
    while True:
        print(c + h*78 + c)
        print(" "*28 + "1: Start Server")
        print(" "*28 + "2: List all History")
        print(" "*28 + "3: Read a History File")
        print(" "*28 + "4: ")
        print(" "*28 + "0: Afsluiten")
        print()
        optie_input = raw_input(" "*28 + "Kies een optie: ",)
        print(optie_input)
        print(c + h*78 + c)
        if optie_input == '1':
            server()
        if optie_input == '2':
            listhistory()
        if optie_input == '3':
            host = input("Geef de bestandsnaam op (zoals 192.168.0.108_52325): ")
            readfile(host, 'r')
        elif optie_input == '0':
            sys.exit(0)
