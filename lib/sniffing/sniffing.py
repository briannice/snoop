from models.packets import ICMPPacket, TCPPacket, UDPPacket
from psutil import net_if_addrs
from scapy.layers.inet import TCP, UDP, ICMP
from scapy.all import sniff, Raw
from typing import Any


def get_interfaces():
    adr = net_if_addrs()

    # Sniffing Pseudo Loopback interfaces in Windows can cause crashes
    loopback = 'Loopback Pseudo-Interface 1'
    if loopback in adr.keys():
        adr.pop(loopback)
    return list(adr.keys())


def sniff_packets(interface: str, prn: Any, filter: str | None):
    sniff(iface=interface, prn=prn, store=0)


def format_packet(packet):
    if packet.haslayer(ICMP):
        return ICMPPacket(packet)
    if packet.haslayer(TCP):
        return TCPPacket(packet)
    if packet.haslayer(UDP):
        return UDPPacket(packet)
