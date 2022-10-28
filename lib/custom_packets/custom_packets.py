from scapy.layers.inet import IP, ICMP, TCP, UDP
from scapy.sendrecv import sr1
from models.packets import ICMPPacket, TCPPacket, UDPPacket


def send_icmp(
    source: str,
    destination: str,
    type: str,
    code: int,
    interface: str,
    payload: str
):
    packet = IP(src=source, dst=destination) / ICMP(type=int(type), code=int(code)) / payload
    res = sr1(packet, iface=interface, timeout=2, verbose=0)
    if res is None:
        return None
    else:
        return ICMPPacket(packet)


def send_tcp(
    source: str,
    destination: str,
    sport: int,
    dport: int,
    interface: str,
    payload: str
):
    packet = IP(src=source, dst=destination) / TCP(dport=int(dport), sport=int(sport)) / payload
    res = sr1(packet, iface=interface, timeout=2, verbose=0)
    if res is None:
        return None
    else:
        return TCPPacket(packet)


def send_udp(
    source: str,
    destination: str,
    sport: int,
    dport: int,
    interface: str,
    payload: str
):
    packet = IP(src=source, dst=destination) / UDP(sport=int(sport), dport=int(dport)) / payload
    res = sr1(packet, iface=interface, timeout=2, verbose=0)
    if res is None:
        return None
    else:
        return UDPPacket(packet)
