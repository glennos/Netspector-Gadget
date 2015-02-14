__author__ = 'Glenn'
import netifaces

netifaces.interfaces()

print("Lijst met interfaces en het IP adress:")
print()

for ifaceName in netifaces.interfaces():
    addresses = [i['addr'] for i in netifaces.ifaddresses(ifaceName).setdefault(netifaces.AF_INET, [{'addr':'No IP addr'}] )]
    print('%s: %s' % (ifaceName, ', '.join(addresses)))