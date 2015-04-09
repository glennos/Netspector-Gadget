#!/usr/bin/env python3

import netifaces


def show_ipadresses():

    netifaces.interfaces()

    print("Lijst met interfaces en het IP adress:")
    print()

    # loopt door de interfaces heen en haalt het ip adres op en stop ze in een variabel
    for ifaceName in netifaces.interfaces():
        addresses = [i["addr"] for i in netifaces.ifaddresses(ifaceName).setdefault(netifaces.AF_INET, [{"addr":"Geen IP"}] )]

        # format de print zodat er een interface + ip adres op het scherm komt
        print("%s: %s" % (ifaceName, " ".join(addresses)))