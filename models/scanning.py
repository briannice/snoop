from models.utils import TCPFlags
from scapy.layers.inet import ICMP, IP, TCP, UDP
from scapy.layers.l2 import Ether
from typing import List
from utils.formating import format_grid


class EthPacket():

    def __init__(self, packet):
        if packet.haslayer(Ether):
            ether = packet.getlayer(Ether)
            self.src = ether.src
            self.dst = ether.dst
        else:
            self.src = ""
            self.dst = ""

    def to_text_short(self):
        return "[Eth]"

    def to_text_extended(self):
        contents = {
            "src": (self.src, 1),
            "dst": (self.dst, 1),
        }
        return format_grid(contents, "Eth")


class IPPacket():

    def __init__(self, packet):
        if packet.haslayer(IP):
            ip = packet.getlayer(IP)
            self.src = ip.src
            self.dst = ip.dst
        else:
            self.src = "unknown"
            self.dst = "unknown"

        self.eth = EthPacket(packet)

    def to_text_short(self):
        return "[IP]"

    def to_text_extended(self):
        contents = {
            "src": (self.src, 1),
            "dst": (self.dst, 1),
        }
        return format_grid(contents, "IP") + self.eth.to_text_extended()


class TCPPacket():

    def __init__(self, packet):

        if packet.haslayer(TCP):
            tcp = packet.getlayer(TCP)
            self.sport = tcp.sport
            self.dport = tcp.dport
            self.flags = TCPFlags.to_list(tcp.flags)
        else:
            self.sport = "unknown"
            self.dport = "unknown"
            self.flags = "unknown"

        self.ip = IPPacket(packet)

    def to_text_short(self):
        return "[TCP]"

    def to_text_extended(self):
        contents = {
            "flags": (TCPFlags.to_string(self.flags), 2),
            "sport": (self.sport, 1),
            "dport": (self.dport, 1)
        }
        return format_grid(contents, "TCP") + self.ip.to_text_extended()


class UDPPacket():

    def __init__(self, packet):

        if packet.haslayer(UDP):
            udp = packet.getlayer(UDP)
            self.sport = udp.sport
            self.dport = udp.dport
        else:
            self.type = "unknown"
            self.code = "unknown"

        self.ip = IPPacket(packet)

    def to_text_short(self):
        return "[UDP]"

    def to_text_extended(self):
        contents = {
            "sport": (self.sport, 1),
            "dport": (self.dport, 1)
        }
        return format_grid(contents, "UDP") + self.ip.to_text_extended()


class ICMPPacket():

    def __init__(self, packet):

        if packet.haslayer(ICMP):
            icmp = packet.getlayer(ICMP)
            self.type = icmp.type
            self.code = icmp.code
        else:
            self.type = "unknown"
            self.code = "unknown"

        self.ip = IPPacket(packet)

    def to_text_short(self):
        return "[ICMP]"

    def to_text_extended(self):
        contents = {
            "type": (self.type, 1),
            "code": (self.code, 1)
        }
        return format_grid(contents, "ICMP") + self.ip.to_text_extended()