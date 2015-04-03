#!/usr/bin/env python
__author__ = 'root'

import socket, sys
from struct import *


def sniffer(packet):

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

    tcppacket = ('Source Port \t\t: ' + str(source_port)
                 + 'Dest Port \t\t: ' + str(dest_port)
                 + 'Sequence Number \t: ' + str(sequence)
                 + 'Acknowledgement \t: ' + str(acknowledgement)
                 + 'TCP header length \t: ' + str(tcph_length)
                 + 'Data \t\t\t: ' + data
                 )
    print(tcppacket)


s = socket.socket()

try:
    host = socket.gethostname()
    port = 12345
    s.connect((host, port))

    while True:
            packets = s.recv(65565)
            sniffer(packets)
finally:
    s.close()







