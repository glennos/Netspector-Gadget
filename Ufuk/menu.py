__author__ = 'Ufuk'
import sys

from pip._vendor.distlib.compat import raw_input

from Ufuk import network_sniffer
from Ufuk import nsg_server_switch
from Ufuk import nsg_client_prime

c = "+"
h = "-"

while True:
    print(c + h*78 + c)
    print(" "*28 + "1: Network Sniffer Ufuk")
    print(" "*28 + "2: Start Server")
    print(" "*28 + "3: Start Client")
    print(" "*28 + "4: ")
    print(" "*28 + "0: Afsluiten")
    print()
    input = optie_input = raw_input(" "*28 + "Kies een optie: ",)
    print(optie_input)
    print(c + h*78 + c)
    if optie_input == '1':
        network_sniffer.sniffer()
    if optie_input == '2':
        nsg_server_switch()
    if optie_input == '3':
        nsg_client_prime()
    elif optie_input == '0':
        sys.exit(0)