from scapy.layers.inet import TCP, UDP, ICMP
from scapy.all import *
import psutil


# Get every interface from host
def getInterfaces():
    adr = psutil.net_if_addrs()
    # Sniffing Pseudo Loopback interfaces in Windows can cause crashes
    loopback = 'Loopback Pseudo-Interface 1'
    if loopback in adr.keys():
        adr.pop(loopback)
    return list(adr.keys())


def sniffAllPackets(interface, prn):
    sniff(iface=interface, prn=prn, store=0)


def sniff_only_tcp_packets(interface, prn):
    sniff(iface=interface, prn=prn, store=0, filter="tcp")


def sniff_only_udp_packets(interface, prn):
    sniff(iface=interface, prn=prn, store=0, filter="udp")


def sniff_only_icmp_packets(interface, prn):
    sniff(iface=interface, prn=prn, store=0, filter="icmp")


def check_icmp(pkt):
    return ICMP in pkt


def get_icmp_message(pkt):
    # readable_payload = bytes(pkt[TCP].payload).decode('UTF8', 'replace')
    return pkt[Raw].load
