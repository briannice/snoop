from enum import Enum
from ipaddress import IPv4Address


class HostState(Enum):
    UP = "UP"
    BLOCKED = "BLOCKED"
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
        self.__type = type
        self.__code = code
        self.__src_ip = src_ip
        self.__dst_ip = dst_ip


class TCPPacket():

    def __init__(
        self,
        src_ip: IPv4Address,
        dst_ip: IPv4Address,
        src_port: int,
        dst_port: int,
        flags: int,
    ):
        self.__src_ip = src_ip
        self.__dst_ip = dst_ip
        self.__src_port = src_port
        self.__dst_port = dst_port
        self.__flags = flags


class HostScanResult():

    def __init__(
        self,
        dst_ip: IPv4Address,
        host_state: HostState,
        icmp_packet: ICMPPacket,
        tcp_packet: TCPPacket
    ):
        self.__host_state = host_state
        self.__dst_ip = dst_ip
        self.__icmp_packet = icmp_packet
        self.__tcp_packet = tcp_packet

    def __str__(self) -> str:
        return f"{self.__dst_ip}: {self.__host_state}"

    def get_packet(self) -> ICMPPacket | TCPPacket | None:
        if self.__icmp_packet:
            return self.__icmp_packet
        if self.__tcp_packet:
            return self.__tcp_packet
        return None

    def is_up(self):
        return self.__host_state == HostState.UP

    def is_unknown(self):
        return self.__host_state == HostState.UNKNOWN

    def is_blocked(self):
        return self.__host_state == HostState.BLOCKED
