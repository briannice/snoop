from scapy.layers.inet import IP, ICMP, TCP, UDP
from scapy.sendrecv import send


def SendICMP(source, destination, interface, ttl=128, count=1, message="Hello World"):
    send(IP(src=source, dst=destination, ttl=ttl) / ICMP() / message, iface=interface, count=count)


def SendTCP(source, destination, dstport, interface, count=1):
    send(IP(src=source, dst=destination) / TCP(dport=dstport), iface=interface, count=count)


def SendUDP(source, destination, dstport, interface, count=1):
    send(IP(src=source, dst=destination) / UDP(dport=dstport), iface=interface, count=count)
