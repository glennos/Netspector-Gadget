__author__ = 'Glenn'
import sys

from pip._vendor.distlib.compat import raw_input

from library import network_sniffer
from Glenn import connect_socket_test
from Bob import menu_Bob, nsg_client, nsg_server


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

while True:
    print(c + h*86 + c)
    print()
    print(" "*28 + "1: Toon IP adressen")
    print(" "*28 + "2: Test Socket connectie")
    print(" "*28 + "3: Simple Network sniffer")
    print(" "*28 + "4: ")
    print(" "*28 + "5: Menu Bob")
    print(" "*28 + "6: Start server")
    print(" "*28 + "7: Start sniffer")

    print(" "*28 + "0: Afsluiten")
    print()
    optie_input = raw_input(" "*28 + "Kies een optie: ",)
    print(optie_input)
    print(c + h*86 + c)
    if optie_input == '1':
        print("hoi")
    elif optie_input == '2':
        connect_socket_test.connect_socket()
    elif optie_input == '3':
        network_sniffer.sniffer()
    elif optie_input == '5':
        menu_Bob.menu_bob()
    elif optie_input == '6':
        while x is True:
            try:
                nsg_server.server()
            except KeyboardInterrupt:
                break
    elif optie_input == '7':
        while True:
            nsg_client.client()
    elif optie_input == '0':
        sys.exit(0)