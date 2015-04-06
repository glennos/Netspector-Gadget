__author__ = 'Bob'

import sys

from Bob import Sniffer_Bob, Sniffer2_Bob, Sniffer3_Bob, server_test, client_test
from pip._vendor.distlib.compat import raw_input

c = "+"
h = "-"

def menu_bob():
    while True:
        print(c + h*78 + c)
        print(" "*28 + "1: Sniffer1_Bob")
        print(" "*28 + "2: Sniffer2_Bob")
        print(" "*28 + "3: Sniffer3_Bob")
        print(" "*28 + "4: Server")
        print(" "*28 + "5: Client")
        print(" "*28 + "0: Afsluiten")
        print()
        optie_input = raw_input(" "*28 + "Kies een optie: ",)
        print(optie_input)
        print(c + h*78 + c)
        if optie_input == '1':
            Sniffer_Bob.sniffer_Bob()
        elif optie_input == '2':
            Sniffer2_Bob.Sniffer2_Bob()
        elif optie_input == '3':
            Sniffer3_Bob.Sniffer3_Bob()
        elif optie_input == '4':
            server_test.server()
        elif optie_input == '5':
            client_test.client()
        elif optie_input == '0':
            sys.exit(0)