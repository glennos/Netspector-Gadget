__author__ = 'root'


#Packet sniffer in python
#For Linux

import socket

#create an INET, raw socket
s = socket.socket( socket.AF_PACKET , socket.SOCK_RAW , socket.ntohs(0x0003))

# receive a packet
while True:
  packet = s.recvfrom(65565)

  packet = packet[::len(packet)]

  print(packet)