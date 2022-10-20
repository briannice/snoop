from enum import Enum
from ipaddress import IPv4Address
from typing import List


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
    INTERNAL_ERROR = "INTERNAL ERROR"


class PortScanMethod(Enum):
    CONNECT = "CONNECT"
    STEALTH = "STEALTH"
    XMAS = "XMAS"
    FIN = "FIN"
    ACK = "ACK"

    @staticmethod
    def dict_to_list(dct):
        result = []
        for k, v in dct.items():
            if v:
                match k:
                    case "ack":
                        result.append(PortScanMethod.ACK)
                    case "connect":
                        result.append(PortScanMethod.CONNECT)
                    case "stealth":
                        result.append(PortScanMethod.STEALTH)
                    case "fin":
                        result.append(PortScanMethod.FIN)
                    case "xmas":
                        result.append(PortScanMethod.XMAS)
        return result


class TCPFlags():
    FLAGS = {
        "FIN": 0x01,
        "SYN": 0x02,
        "RST": 0x04,
        "PSH": 0x08,
        "ACK": 0x10,
        "URG": 0x20,
        "ECE": 0x40,
        "CWR": 0x80
    }

    SCAPY_FLAGS = {
        "F": "FIN",
        "S": "SYN",
        "R": "RST",
        "P": "PSH",
        "A": "ACK",
        "U": "URG",
        "E": "ECE",
        "C": "CWR"
    }

    @staticmethod
    def to_bytes(flags: List[str]) -> int:
        result = 0x0
        for f in flags:
            result |= TCPFlags.FLAGS[f]
        return result

    @staticmethod
    def to_list(bytes: int) -> List[str]:
        result = []
        for k, _ in TCPFlags.FLAGS.items():
            if bytes & 1 > 0:
                result.append(k)
            bytes >>= 1
        return result

    @staticmethod
    def to_list(flags: str) -> List[str]:
        result = []
        for f in flags:
            result.append(TCPFlags.SCAPY_FLAGS[f])
        return result


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

    def __str__(self) -> str:
        return f"{self.src_ip}:{self.src_port} -> {self.dst_ip}:{self.dst_port} [ flags={self.flags} ]"


class HostScanResult():

    def __init__(
        self,
        ip: IPv4Address,
        state: HostState,
        icmp: ICMPPacket | None,
        tcp: TCPPacket | None
    ):
        self.ip = ip
        self.state = state
        self.icmp = icmp
        self.tcp = tcp

    def __str__(self) -> str:
        return f"{self.ip}: {self.state}"

    def get_packet(self) -> ICMPPacket | TCPPacket | None:
        if self.icmp:
            return self.icmp
        if self.tcp:
            return self.tcp
        return None

    def is_up(self) -> bool:
        return self.state == HostState.UP

    def is_unknown(self) -> bool:
        return self.state == HostState.UNKNOWN

    def is_blocked(self) -> bool:
        return self.state == HostState.BLOCKED


class PortScanResult():

    def __init__(
        self,
        ip: IPv4Address,
        port: int,
        state: PortState,
        method: PortScanMethod,
        icmp: ICMPPacket | None,
        tcp: TCPPacket | None
    ):
        self.ip = ip
        self.port = port
        self.state = state
        self.method = method
        self.icmp = icmp
        self.tcp = tcp

    def __str__(self) -> str:
        return f"[{self.method}] {self.ip}:{self.port} -> {self.state}"


class PortScanConclusion():

    def __init__(self, port: int, result: List[PortScanResult]):
        self.port = port
        self.result = result

    def __eq__(self, o: PortScanResult) -> bool:
        self.port == o.port

    def __lt__(self, o: PortScanResult) -> bool:
        self.port < o.port

    def __le__(self, o: PortScanResult) -> bool:
        self.port <= o.port

    def __gt__(self, o: PortScanResult) -> bool:
        self.port > o.port

    def __ge__(self, o: PortScanResult) -> bool:
        self.port >= o.port
