#!/usr/bin/env python
__author__ = 'root'


import socket, sys
from struct import *

def sniffer():
    try:
        # create an INET, STREAMing socket
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
        except socket.error as msg:
            print('Socket could not be created. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
            sys.exit()

        # receive a packet
        while True:
            packet = s.recvfrom(65565)

            # packet string from tuple
            packet = packet[0]

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


            print('Source Port \t\t: ' + str(source_port))
            print('Dest Port \t\t: ' + str(dest_port))
            print('Sequence Number \t: ' + str(sequence))
            print('Acknowledgement \t: ' + str(acknowledgement))
            print('TCP header length \t: ' + str(tcph_length))

            h_size = iph_length + tcph_length * 4
            data_size = len(packet) - h_size

            # get data from the packet
            data = str(packet[h_size:])

            if data != """b''""":
                print('Data \t\t\t: ' + data)

            print("\n")
    except KeyboardInterrupt:
        print("End")

s = socket.socket()
host = "localhost"
port = 12345
s.bind((host, port))

s.listen(5)
while True:
    c, addr = s.accept()
    print('Got connection from', addr)
    c.send(sniffer())
    c.close()
