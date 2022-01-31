#!/usr/bin/env python

import subprocess

def mac_changer(interface, new_mac):
    subprocess.call(f"ifconfig {interface} down", shell=True)       # disable the MAC address
    subprocess.call(f"ifconfig {interface} hw ether {new_mac}", shell=True)
    subprocess.call(f"ifconfig {interface} up", shell=True)         # enable the mac Address

interface = "eth0"
new_mac = "00:11:22:33:44:88"

interface = input("interface > ")
new_mac = input("new MAC > ")
mac_changer(interface, new_mac)
