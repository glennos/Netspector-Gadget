#!/usr/bin/env python
__author__ = 'root'

import socket, sys
from struct import *


def sniffer(packet, user_dest_port):

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
    s_addr = socket.inet_ntoa(iph[8]);
    d_addr = socket.inet_ntoa(iph[9]);
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
        print(tcppacket)
        # file.write(tcppacket)
        writetofile(tcppacket, 'client_history', 'a')


def writetofile(sniffer, file, mode):
    # w = write and replace file content
    # a = append
    # r = read
    # r+ = read and write
    if mode == 'w':
        file = open(file, mode)
        file.write(sniffer)
    elif mode == 'a':
        file = open(file, mode)
        file.write(sniffer)
    elif mode == 'r':
        file = open(file, mode)
        file.read()
    # elif mode == 'r+':
    #     file = open(file, mode)


s = socket.socket()

try:
    host = socket.gethostname()
    port = 12345
    s.connect((host, port))

    while True:
        packets = s.recv(65565)
        if packets:
            sniffer(packets, port)
finally:
    s.close()