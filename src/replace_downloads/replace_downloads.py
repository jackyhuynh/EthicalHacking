#!/usr/bin/env python
import netfilterqueue
import scapy.all as scapy

"""
+ process packet take a packet as parameter
+ 
"""


def process_packet(packet):
    scapy_packet = scapy.IP(packet.get_payload())

    if scapy_packet.haslayer(scapy.DNSRR):
        


    packet.accept()


queue = netfilterqueue.NetfilterQueue()
# call back function use in every single packet in the queue
# process_packet will be executed in every packet that trapped in the netfilter queue
queue.bind(0, process_packet)
queue.run()

"""
using flush in the terminal to flush the program
"""

