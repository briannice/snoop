from scapy.layers.inet import IP, ICMP, TCP, UDP
from scapy.sendrecv import sr1


def send_icmp(source: str, destination: str, type: int, code: int,  interface: str, payload: str):
    return sr1(IP(src=source, dst=destination, ttl=128) / ICMP(type=type, code=code) / payload, iface=interface, timeout=1, verbose=0)


def send_tcp(source: str, destination: str, sport: int, dport: int, interface: str, payload: str):
    return sr1(IP(src=source, dst=destination) / TCP(dport=dport, sport=sport) / payload, iface=interface, timeout=1, verbose=0)


def send_udp(source: str, destination: str, sport: int, dport: int, interface: str, payload: str):
    return sr1(IP(src=source, dst=destination) / UDP(sport=sport, dport=dport) / payload, iface=interface, timeout=1, verbose=0)
