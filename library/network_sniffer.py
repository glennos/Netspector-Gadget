#!/usr/bin/env python3

from struct import *
import socket
import sys


def sniffer():
    try:
        # formatting voor het mac adress
        def eth_addr(a):
            b = "%.2x:%.2x:%.2x:%.2x:%.2x:%.2x" % (a[0], a[1], a[2], a[3], a[4], a[5])
            return b

        # Maakt AF_PACKET type raw socket (packet niveau)
        # ETH_P_ALL    0x0003 (alle paketten)
        try:
            s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(0x0003))
        except socket.error as msg:
            msg = list(msg)
            print('Socket kon niet worden opgebouwd. Fout Code : ' + str(msg[0]) + ' bericht ' + msg[1])
            sys.exit()

        # Pakketjes ontvangen
        while True:
            packet = s.recvfrom(65565)

            # Van een tuple naar een string
            packet = packet[0]

            # parse ethernet header
            eth_length = 14

            eth_header = packet[:eth_length]
            eth = unpack('!6s6sH', eth_header)
            eth_protocol = socket.ntohs(eth[2])
            print(
                'Destination MAC : ' + eth_addr(packet[0:6]) + ' Source MAC : ' + eth_addr(packet[6:12]) + ' Protocol : ' + str(
                    eth_protocol))
    except KeyboardInterrupt:
        print("End")