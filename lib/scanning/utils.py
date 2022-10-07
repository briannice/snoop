from enum import Enum
from ipaddress import IPv4Address


class HostState(Enum):
    UP = "UP"
    DOWN = "DOWN"
    UNKNOWN = "UNKNOWN"


class PortState(Enum):
    OPEN = "OPEN"
    CLOSED = "CLOSED"
    FILTERED = "FILTERED"
    UNFILTERED = "UNFILTERED"
    OPEN_FILTERED = "OPEN | FILTERED"
    CLOSED_FILTERED = "CLOSED | FILTERED"


class ICMPPacket():

    def __init__(
        self,
        src_ip: IPv4Address,
        dst_ip: IPv4Address,
        type: int,
        code: int,
    ):
        self.type = type
        self.code = code
        self.src_ip = src_ip
        self.dst_ip = dst_ip


class TCPPacket():

    def __init__(
        self,
        src_ip: IPv4Address,
        dst_ip: IPv4Address,
        src_port: int,
        dst_port: int,
        flags: int,
    ):
        self.src_ip = src_ip
        self.dst_ip = dst_ip
        self.src_port = src_port
        self.dst_port = dst_port
        self.flags = flags


class ICMPHostScanResult():

    def __init__(
        self,
        state: HostState,
        src_ip: IPv4Address,
        dst_ip: IPv4Address,
        type: int,
        code: int,
    ):
        pkt = ICMPPacket(src_ip, dst_ip, type, code)

        self.pkt = pkt
        self.state = state


class ICMPPortScanResult():

    def __init__(
        self,
        state: PortState,
        src_ip: IPv4Address,
        dst_ip: IPv4Address,
        type: int,
        code: int,
    ):
        pkt = ICMPPacket(src_ip, dst_ip, type, code)

        self.pkt = pkt
        self.state = state


class TCPHostScanResult():
    def __init__(
        self,
        state: HostState,
        src_ip: IPv4Address,
        dst_ip: IPv4Address,
        src_port: int,
        dst_port: int,
        flags: int,
    ):
        pkt = TCPPacket(src_ip, dst_ip, src_port, dst_port, flags)

        self.pkt = pkt
        self.state = state


class TCPPortScanResult():

    def __init__(
        self,
        state: PortState,
        src_ip: IPv4Address,
        dst_ip: IPv4Address,
        src_port: int,
        dst_port: int,
        flags: int,
    ):
        pkt = TCPPacket(src_ip, dst_ip, src_port, dst_port, flags)

        self.pkt = pkt
        self.state = state
