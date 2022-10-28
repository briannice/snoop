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
            self.type = ether.type
        else:
            self.src = ""
            self.dst = ""
            self.type = ""

    def to_text_short(self):
        return "[Eth]"

    def to_text_extended(self):
        contents = {
            "src": (self.src, 1),
            "dst": (self.dst, 1),
            "type": (self.type, 1),
        }
        return format_grid(contents, "Eth")


class IPPacket():

    def __init__(self, packet):
        if packet.haslayer(IP):
            ip = packet.getlayer(IP)
            self.src = ip.src
            self.dst = ip.dst
            self.ttl = ip.ttl
            self.id = ip.id
        else:
            self.src = ""
            self.dst = ""
            self.ttl = ""
            self.id = ""

        self.eth = EthPacket(packet)

    def to_text_short(self):
        return "[IP]"

    def to_text_extended(self):
        contents = {
            "src": (self.src, 1),
            "dst": (self.dst, 1),
            "ttl": (self.ttl, 1),
            "id": (self.id, 1),
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
            self.sport = ""
            self.dport = ""
            self.flags = ""

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
            self.type = ""
            self.code = ""

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
            self.chksum = icmp.chksum
            self.id = icmp.id
            self.seq = icmp.seq
        else:
            self.type = ""
            self.code = ""
            self.chksum = ""
            self.id = ""
            self.seq = ""

        self.ip = IPPacket(packet)

    def to_text_short(self):
        return "[ICMP]"

    def to_text_extended(self):
        contents = {
            "type": (self.type, 1),
            "code": (self.code, 1),
            "chksum": (self.chksum, 1),
            "id": (self.id, 1),
            "seq": (self.seq, 1),
        }
        return format_grid(contents, "ICMP") + self.ip.to_text_extended()
