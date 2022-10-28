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
        self.summary = packet.summary()

    def to_text_short(self):
        return self.summary

    def to_text_extended(self):
        contents = {
            "src": (str(self.src or ''), 1),
            "dst": (str(self.dst or ''), 1),
            "type": (str(self.type or ''), 1),
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
        self.summary = packet.summary()

        self.eth = EthPacket(packet)

    def to_text_short(self):
        return self.summary

    def to_text_extended(self):
        contents = {
            "src": (str(self.src or ''), 1),
            "dst": (str(self.dst or ''), 1),
            "ttl": (str(self.ttl or ''), 1),
            "id": (str(self.id or ''), 1),
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
        self.summary = packet.summary()

        self.ip = IPPacket(packet)

    def to_text_short(self):
        return self.summary

    def to_text_extended(self):
        contents = {
            "flags": (str(TCPFlags.to_string(self.flags) or ''), 2),
            "sport": (str(self.sport or ''), 1),
            "dport": (str(self.dport or ''), 1)
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
        self.summary = packet.summary()

        self.ip = IPPacket(packet)

    def to_text_short(self):
        return self.summary

    def to_text_extended(self):
        contents = {
            "sport": (str(self.sport or ''), 1),
            "dport": (str(self.dport or ''), 1)
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
        self.summary = packet.summary()

        self.ip = IPPacket(packet)

    def to_text_short(self):
        return self.summary

    def to_text_extended(self):
        contents = {
            "type": (str(self.type or ''), 1),
            "code": (str(self.code or ''), 1),
            "chksum": (str(self.chksum or ''), 1),
            "id": (str(self.id or ''), 1),
            "seq": (str(self.seq or ''), 1),
        }
        return format_grid(contents, "ICMP") + self.ip.to_text_extended()
