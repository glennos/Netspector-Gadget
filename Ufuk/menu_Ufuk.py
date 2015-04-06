__author__ = 'Ufuk'

import sys
from pip._vendor.distlib.compat import raw_input
from Ufuk import network_sniffer, nsg_server, nsg_client

c = "+"
h = "-"


def menu_ufuk():
    while True:
        print(c + h*78 + c)
        print(" "*28 + "1: Start Server")
        print(" "*28 + "2: Start Client")
        print(" "*28 + "3: ")
        print(" "*28 + "4: ")
        print(" "*28 + "0: Afsluiten")
        print()
        optie_input = raw_input(" "*28 + "Kies een optie: ",)
        print(optie_input)
        print(c + h*78 + c)
        if optie_input == '1':
            nsg_server.menu_server()
        if optie_input == '2':
            nsg_client.client()
        elif optie_input == '0':
            sys.exit(0)