#!/usr/bin/python3
# -*- coding: utf-8 -*

import socket
import binascii

def mgpk_send(ip_bc,port_bc,macs):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
         s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST,1)
    
         macs = macs.translate({ord(c): None for c in ':-'})
         data_sent = b'\xff' * 6 + binascii.unhexlify(macs) * 16
         s.sendto(data_sent, (ip_bc, port_bc))
         
if __name__ == "__main__":
    mgpk_send('192.168.100.255',8019,"AB:AB:AB:AB:AB:AB")
