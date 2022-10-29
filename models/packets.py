from models.utils import TCPFlags
from utils.formating import format_grid, format_payload
from scapy.all import ICMP, IP, TCP, UDP, Ether, Raw


class PayloadPacket():

    def __init__(self, packet):
        if packet.haslayer(Raw):
            try:
                self.payload = packet.getlayer(Raw).load.decode("utf-8")
            except Exception:
                self.payload = ""
        else:
            self.payload = ""

    def to_text_extended(self):
        return format_payload(self.payload or '')

    def to_text_short(self):
        return self.payload or ''


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
        self.payload = PayloadPacket(packet)

    def to_text_short(self):
        return f"src={self.src or ''}  dst={self.dst or ''} / " + self.payload.to_text_short()

    def to_text_extended(self):
        contents = {
            "src": (str(self.src or ''), 1),
            "dst": (str(self.dst or ''), 1),
            "type": (str(self.type or ''), 1),
        }
        return format_grid(contents, "Eth") + self.payload.to_text_extended()


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
        return f"src={self.src or ''}  dst={self.dst or ''} / " + self.eth.to_text_short()

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

        self.ip = IPPacket(packet)

    def to_text_short(self):
        return f"[TCP]   sport={self.sport or ''}  dport={self.dport or ''}  flags={TCPFlags.to_string(self.flags) or ''} / " + self.ip.to_text_short()

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

        self.ip = IPPacket(packet)

    def to_text_short(self):
        return f"[UDP]   sport={self.sport or ''}  dport={self.dport or ''} / " + self.ip.to_text_short()

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

        self.ip = IPPacket(packet)

    def to_text_short(self):
        return f"[ICMP]  type={self.type or ''}  dport={self.code or ''} / " + self.ip.to_text_short()

    def to_text_extended(self):
        contents = {
            "type": (str(self.type or ''), 1),
            "code": (str(self.code or ''), 1),
            "chksum": (str(self.chksum or ''), 1),
            "id": (str(self.id or ''), 1),
            "seq": (str(self.seq or ''), 1),
        }
        return format_grid(contents, "ICMP") + self.ip.to_text_extended()
