#!/usr/bin/env python

import subprocess

# call ifconfig and call the Shell Linux command to this function
# disable the MAC address
subprocess.call("ifconfig eth0 down", shell=True)
# Change it here
subprocess.call("ifconfig eth0 hw ether 66:55:44:33:22:11", shell=True)
# enable the mac Address
subprocess.call("ifconfig eth0 up", shell=True)
# Check it again
