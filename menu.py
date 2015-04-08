__author__ = 'Glenn'
import sys
import socket

from pip._vendor.distlib.compat import raw_input

from library import network_sniffer, client, server, functions, get_ipadresses
from Glenn import connect_socket_test
from Bob import menu_Bob, nsg_client, nsg_server


def menu_server():
    while True:
        print(c + h*86 + c)
        print(" "*28 + "1: Start Server")
        print(" "*28 + "2: List all History")
        print(" "*28 + "3: Read a History File")
        print(" "*28 + "4: ")
        print(" "*28 + "0: Afsluiten")
        print()
        optie_input = raw_input(" "*28 + "Kies een optie: ",)
        print(optie_input)
        print(c + h*86 + c)
        if optie_input == '1':
            server.server()
        if optie_input == '2':
            functions.listhistory()
        if optie_input == '3':
            host = input("Geef de bestandsnaam op (zoals 192.168.0.108_52325): ")
            functions.readfile(host, 'r')
        elif optie_input == '0':
            menu()


def menu():
    while True:
        print(c + h*86 + c)
        print()
        print(" "*28 + "|-+-+-+-+-+-+-+-+-+-+-+-+-+-+-|")
        print(" "*28 + "+   1: Toon IP adres          +")
        print(" "*28 + "|   2: Test Socket connectie  |")
        print(" "*28 + "+   3: Simple Network sniffer |")
        print(" "*28 + "|-+-+-+-+-+-+-+-+-+-+-+-+-+-+-|")
        print(" "*28 + "|   4: Server                 |")
        print(" "*28 + "|   5: Start sniffer          |")
        print(" "*28 + "|-+-+-+-+-+-+-+-+-+-+-+-+-+-+-|")
        print(" "*28 + "|   0: Afsluiten              |")
        print(" "*28 + "|-+-+-+-+-+-+-+-+-+-+-+-+-+-+-|")
        print()
        optie_input = raw_input(" "*28 + "Kies een optie: ",)
        print(optie_input)
        print(c + h*86 + c)
        if optie_input == '1':
            get_ipadresses.show_ipadresses()
            # s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            # s.connect(("google.nl",80))
            # print(s.getsockname()[0])
            # s.close()
        elif optie_input == '2':
            connect_socket_test.connect_socket()
        elif optie_input == '3':
            network_sniffer.sniffer()
        elif optie_input == '4':
            menu_server()
        elif optie_input == '5':
            client.client()
        elif optie_input == '0':
            sys.exit(0)

c = "+"
h = "-"

x = True

print(c + h*86 + c)
print("""|      __     _                       _                 ___          _            _    |
|   /\ \ \___| |_ ___ _ __   ___  ___| |_ ___  _ __    / _ \__ _  __| | __ _  ___| |_  |
|  /  \/ / _ \ __/ __| '_ \ / _ \/ __| __/ _ \| '__|  / /_\/ _` |/ _` |/ _` |/ _ \ __| |
| / /\  /  __/ |_\__ \ |_) |  __/ (__| || (_) | |    / /_\\\ (_| | (_| | (_| |  __/ |_  |
| \_\ \/ \___|\__|___/ .__/ \___|\___|\__\___/|_|    \____/\__,_|\__,_|\__, |\___|\__| |
|                    |_|                                               |___/           |""")


menu()