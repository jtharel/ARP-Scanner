#!/usr/bin/python3

from scapy.all import *

for X in range(1,255):
    ip = "192.168.1." + str(X)
    arpRequest = Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=ip, hwdst="ff:ff:ff:ff:ff:ff")
    arpResponse = srp1(arpRequest, timeout=1, verbose=0)
    if arpResponse:
        print("IP: " + arpResponse.psrc + " MAC: " + arpResponse.hwsrc)






