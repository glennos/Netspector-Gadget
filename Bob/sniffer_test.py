from struct import *
import socket
import sys


def sniffer(remote):
    try:
        # create a AF_PACKET type raw socket (thats basically packet level)
        # define ETH_P_ALL    0x0003          /* Every packet (be careful!!!) */
        try:
            s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(0x0003))
        except socket.error as msg:
            msg = list(msg)
            print('Socket could not be created. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
            sys.exit()

        # receive a packet
        while True:
            packet = s.recvfrom(65565)
            # packet string from tuple
            packet = packet[0]

            remote.send(packet)
    except KeyboardInterrupt:
        print("End")
