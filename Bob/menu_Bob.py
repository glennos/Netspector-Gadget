__author__ = 'Bob'
import sys

from pip._vendor.distlib.compat import raw_input

from Bob import Sniffer2_Bob

c = "+"
h = "-"

def menu_bob():
    while True:
        print(c + h*78 + c)
        print(" "*28 + "1: Sniffer2_Bob")
        print(" "*28 + "2: ")
        print(" "*28 + "3: ")
        print(" "*28 + "4: ")
        print(" "*28 + "5: ")
        print(" "*28 + "0: Afsluiten")
        print()
        input = optie_input = raw_input(" "*28 + "Kies een optie: ",)
        print(optie_input)
        print(c + h*78 + c)
        if optie_input == '1':
            print(Sniffer2_Bob.Sniffer2_Bob())
        elif optie_input == '0':
            sys.exit(0)