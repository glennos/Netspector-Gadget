from struct import *
import socket
import sys


def snifferformat(packet):

    # Convert a string of 6 characters of ethernet address into a dash separated hex string
    def eth_addr(a):
        b = "%.2x:%.2x:%.2x:%.2x:%.2x:%.2x" % (a[0], a[1], a[2], a[3], a[4], a[5])
        return b

    # parse ethernet header
    eth_length = 14

    eth_header = packet[:eth_length]
    eth = unpack('!6s6sH', eth_header)
    eth_protocol = socket.ntohs(eth[2])
    print('Destination MAC : ' + eth_addr(packet[0:6]) + ' Source MAC : ' + eth_addr(packet[6:12]) + ' Protocol : ' + str(eth_protocol))

    if eth_protocol != 8:
        print()

    # Parse IP packets, IP Protocol number = 8
    if eth_protocol == 8:
        # Parse IP header
        # take first 20 characters for the ip header
        ip_header = packet[eth_length:20+eth_length]

        # now unpack them
        iph = unpack('!BBHHHBBH4s4s', ip_header)

        # To the the ip version we have to shift the first element 4 bits right. Because in the first element
        # is stored the ip version and the header lenght in this way first four bits are ip version
        # and the last 4 bites are the header lenght
        version_ihl = iph[0]
        ip_version = version_ihl >> 4
        version = version_ihl >> 4
        ihl = version_ihl & 0xF

        iph_length = ihl * 4

        ttl = iph[5]
        protocol = iph[6]
        s_addr = socket.inet_ntoa(iph[8])
        d_addr = socket.inet_ntoa(iph[9])

        if ip_version == 4:

            # Now to get the header lenght we use "and" operation to make the
            # Ip versional bits equal to zero, in order to the desired data
            ip_headerlength = version_ihl & 0xF  # 0xF is 15
            ip_tos = iph[1]
            ip_tot_len = iph[2]
            ip_id = iph[3]

            # The "Flags" and Fragment Offset are situated in a single
            # element from the forth element of the tuple.
            # Flag is 3 bits (Most significant), so we make "and" with 1110 0000 0000 0000(=0xE000)
            # to leave 3 most significant bits and then shift them right 13 positions
            ip_flags = iph[4] & 0xE000 >> 13
            ip_frag_off = iph[4] & 0x3f28cb7157158 >> 3  # Zelf berekend: 1111111111111000(=0x3f28cb7157158)

            # The next elements
            ip_ttl = iph[5]
            ip_proto = iph[6]
            ip_checksum = iph[7]
            ip_s_addr = socket.inet_ntoa(iph[8])
            ip_d_addr = socket.inet_ntoa(iph[9])

            # Options en padding zijn niet altijd aanwezig, hoe te extracten??
            # ip_options = iph[]
            # ip_padding = iph[]
            data = ('Version : ' + str(ip_version)
                  + ' IP Header Length : ' + str(ip_headerlength)
                  + ' Type of Service : ' + str(ip_tos)
                  + ' Total length : ' + str(ip_tot_len)
                  + ' ID : ' + str(ip_id)
                  + ' Flags : ' + str(ip_flags)
                  + ' Fragment Offset : ' + str(ip_frag_off)
                  + ' TTL : ' + str(ip_ttl)
                  + ' Protocol : ' + str(ip_proto)
                  + ' \nHeader Checksum : ' + str(ip_checksum)
                  + ' Source Address : ' + str(ip_s_addr)
                  + ' Destination Address : ' + str(ip_d_addr)
                  # + ' Options : ' + str(ip_options)
                  # + ' Padding : ' + str(ip_padding)
                  )
            print(data)

        # TCP protocol
        if protocol == 6:
            t = iph_length + eth_length
            tcp_header = packet[t:t+20]

            # now unpack them :)
            tcph = unpack('!HHLLBBHHH', tcp_header)

            source_port = tcph[0]
            dest_port = tcph[1]
            sequence = tcph[2]
            acknowledgement = tcph[3]
            doff_reserved = tcph[4]
            tcph_length = doff_reserved >> 4

            print('Source Port : ' + str(source_port) + ' Dest Port : ' + str(dest_port) + ' Sequence Number : ' + str(sequence) + ' Acknowledgement : ' + str(acknowledgement) + ' TCP header length : ' + str(tcph_length))

        # ICMP Packets
        elif protocol == 1:
            u = iph_length + eth_length
            icmph_length = 4
            icmp_header = packet[u:u+4]

            # now unpack them :)
            icmph = unpack('!BBH', icmp_header)

            icmp_type = icmph[0]
            code = icmph[1]
            checksum = icmph[2]

            print('Type : ' + str(icmp_type) + ' Code : ' + str(code) + ' Checksum : ' + str(checksum))

        # UDP packets
        elif protocol == 17:
            u = iph_length + eth_length
            udph_length = 8
            udp_header = packet[u:u+8]

            # now unpack them :)
            udph = unpack('!HHHH', udp_header)

            source_port = udph[0]
            dest_port = udph[1]
            length = udph[2]
            checksum = udph[3]

            print('Source Port : ' + str(source_port) + ' Dest Port : ' + str(dest_port) + ' Length : ' + str(length) + ' Checksum : ' + str(checksum))

        elif ip_version == 6:
            ip_trafficclass = iph[1]
            ip_flowlabel = iph[2]
            ip_payloadlength = iph[3]
            ip_nextheader = iph[4]
            ip_hoplimit = iph[5]
            ip_s_addr = iph[6]
            ip_d_addr = iph[7]

            print('Version : ' + str(ip_version)
                  + ' Traffic Class ' + str(ip_trafficclass)
                  + ' Flow Label : ' + str(ip_flowlabel)
                  + ' Payload Length : ' + str(ip_payloadlength)
                  + ' Next Header : ' + str(ip_nextheader)
                  + ' Hop Limit : ' + str(ip_hoplimit)
                  + ' Source Address : ' + str(ip_s_addr)
                  + ' Destination Address : ' + str(ip_d_addr)
                  )
        print()
