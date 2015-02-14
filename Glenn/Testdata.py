__author__ = 'Glenn'
import netifaces
import socket
import sys

netifaces.interfaces()

addrs = netifaces.ifaddresses('en0')
print(addrs[netifaces.AF_INET])