__author__ = 'Glenn'
import curses
from pip._vendor.distlib.compat import raw_input
import get_ipadresses
import Glenn.connect_socket_test
import sys

c = "+"
h = "-"

while True:
    print(c + h*78 + c)
    print(" "*32 + "1: Toon IP adressen")
    print(" "*32 + "2: Test Socket connectie")
    print(" "*32 + "3: ")
    print(" "*32 + "4: ")
    print(" "*32 + "0: Afsluiten")
    print()
    input = optie_input = raw_input(" "*32 + "Kies een optie: ",)
    print(optie_input)
    print(c + h*78 + c)
    if optie_input == '1':
        print(get_ipadresses.show_ipadresses())
    elif optie_input == '2':
        print(Glenn.connect_socket_test.connect_socket())
    elif optie_input == '0':
        sys.exit(0)