from scapy.layers.inet import TCP, UDP, ICMP
from scapy.all import *
import psutil


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


def check_icmp(pkt):
    if pkt.haslayer(ICMP):
        return True
    else:
        return False


def get_icmp_message(pkt):
    # readable_payload = bytes(pkt[TCP].payload).decode('UTF8', 'replace')
    return pkt[Raw].load
