__author__ = 'Glenn'
import netifaces

netifaces.interfaces()

addrs = netifaces.ifaddresses('en0')
print(addrs[netifaces.AF_INET])