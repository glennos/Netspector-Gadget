import socket
import sys
from struct import unpack


def sniffer():
    try:
        def eth_addr(a):
            b = "%.2x:%.2x:%.2x:%.2x:%.2x:%.2x" % (a[0], a[1], a[2], a[3], a[4], a[5])
            return b

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


HOST, PORT = "10.0.1.50", 12345

# Create a socket (SOCK_STREAM means a TCP socket)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s = socket.socket()

try:
    # Connect to server and send data
    sock.connect((HOST, PORT))

    while True:
            sock.sendall(sniffer())

    # Receive data from the server and shut down
    # received = str(sock.recv(1024), "utf-8")
finally:
    sock.close()