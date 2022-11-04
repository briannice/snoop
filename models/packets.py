from models.utils import TCPFlags
from utils.formating import format_grid, format_payload
from scapy.all import ICMP, IP, TCP, UDP, Ether, Raw

def conv(v):
    if v in ['', None]:
        return ''
    else:
        return str(v)


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
        return format_payload(self.payload )

    def to_text_short(self):
        if self.payload == '':
            return ''
        return f"payload={self.payload}"


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
        return f"src={self.src }  dst={self.dst }"

    def to_text_extended(self):
        contents = {
            "src": (conv(self.src), 1),
            "dst": (conv(self.dst), 1),
            "type": (conv(self.type), 1),
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
        return f"src={conv(self.src)}  dst={conv(self.dst)} / " + self.eth.to_text_short()

    def to_text_extended(self):
        contents = {
            "src": (conv(self.src), 1),
            "dst": (conv(self.dst), 1),
            "ttl": (conv(self.ttl), 1),
            "id": (conv(self.id), 1),
        }
        return format_grid(contents, "IP") + self.eth.to_text_extended()


class TCPPacket():

    def __init__(self, packet):

        if packet.haslayer(TCP):
            tcp = packet.getlayer(TCP)
            self.sport = tcp.sport
            self.dport = tcp.dport
            self.seq = tcp.seq
            self.ack = tcp.ack
            self.flags = TCPFlags.to_list(tcp.flags)
        else:
            self.sport = ""
            self.dport = ""
            self.seq = ""
            self.ack = ""
            self.flags = ""
        self.ip = IPPacket(packet)
        self.payload = PayloadPacket(packet)

    def to_text_short(self):
        return f"[TCP]   {conv(self.ip.src)}:{conv(self.sport)} → {conv(self.ip.dst)}:{conv(self.dport)} flags={conv(TCPFlags.to_string(self.flags))} {self.payload.to_text_short()}"

    def to_text_extended(self):
        contents = {
            "flags": (conv(TCPFlags.to_string(self.flags)), 2),
            "sport": (conv(self.sport), 1),
            "dport": (conv(self.dport), 1),
            "seq": (conv(self.seq), 1),
            "ack": (conv(self.ack), 1)
        }
        return format_grid(contents, "TCP") + self.ip.to_text_extended() +  self.payload.to_text_extended()


class UDPPacket():

    def __init__(self, packet):

        if packet.haslayer(UDP):
            udp = packet.getlayer(UDP)
            self.sport = udp.sport
            self.dport = udp.dport
        else:
            self.sport = ""
            self.dport = ""
        self.ip = IPPacket(packet)
        self.payload = PayloadPacket(packet)

    def to_text_short(self):
        return f"[UDP]   {conv(self.ip.src)}:{conv(self.sport)} → {conv(self.ip.dst)}:{conv(self.dport)} {self.payload.to_text_short()}"

    def to_text_extended(self):
        contents = {
            "sport": (conv(self.sport), 1),
            "dport": (conv(self.dport), 1)
        }
        return format_grid(contents, "UDP") + self.ip.to_text_extended() + self.payload.to_text_extended()


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
        self.payload = PayloadPacket(packet)


    def to_text_short(self):
        return f"[ICMP]  {conv(self.ip.src)} → {conv(self.ip.dst)} type={conv(self.type)} code={conv(self.code)} {self.payload.to_text_short()}"

    def to_text_extended(self):
        contents = {
            "type": (conv(self.type), 1),
            "code": (conv(self.code), 1),
            "chksum": (conv(self.chksum), 1),
            "id": (conv(self.id), 1),
            "seq": (conv(self.seq), 1),
        }
        return format_grid(contents, "ICMP") + self.ip.to_text_extended() + self.payload.to_text_extended()
