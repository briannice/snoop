import psutil
from scapy.all import *


# Get every interface from host
def getInterfaces():
    adr = psutil.net_if_addrs()
    return list(adr.keys())


def sniffAllPackets(interface, prn):
    sniff(iface=interface, prn=prn, store=0)


def sniff_only_tcp_packets(interface, prn):
    sniff(iface=interface, prn=prn, store=0, filter="tcp")


def sniff_only_udp_packets(interface, prn):
    sniff(iface=interface, prn=prn, store=0, filter="udp")
