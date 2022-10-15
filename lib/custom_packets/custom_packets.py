from scapy.layers.inet import IP, ICMP, TCP, UDP
from scapy.sendrecv import send


def SendICMP(source, destination, interface, message, count):
    send(IP(src=source, dst=destination, ttl=128) / ICMP() / message, iface=interface, count=count)


def SendTCP(source, destination, dstport, srcport, interface, count=1):
    send(IP(src=source, dst=destination) / TCP(dport=dstport, sport=srcport), iface=interface, count=count)


def SendUDP(source, destination, dstport, srcport, interface, count=1):
    send(IP(src=source, dst=destination) / UDP(dport=dstport, sport=srcport), iface=interface, count=count)
