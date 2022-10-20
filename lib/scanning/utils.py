from enum import Enum
from ipaddress import IPv4Address
from typing import List


class HostState(Enum):
    UP = "UP"
    BLOCKED = "BLOCKED"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return self.value


class PortState(Enum):
    OPEN = "OPEN"
    CLOSED = "CLOSED"
    FILTERED = "FILTERED"
    UNFILTERED = "UNFILTERED"
    OPEN_FILTERED = "OPEN | FILTERED"
    CLOSED_FILTERED = "CLOSED | FILTERED"
    INTERNAL_ERROR = "INTERNAL ERROR"

    def __str__(self) -> str:
        return self.value


class PortScanMethod(Enum):
    CONNECT = "CONNECT"
    STEALTH = "STEALTH"
    XMAS = "XMAS"
    FIN = "FIN"
    ACK = "ACK"

    def __str__(self) -> str:
        return self.value

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
        return f"{self.method}   →   {self.state}"


class PortScanConclusion():

    def __init__(self, port: int, results: List[PortScanResult]):
        self.port = port
        self.results = results
        self.state = self.get_global_state()

    def __str__(self) -> str:
        result = ""

        result += f"{self.port}   →   {self.state}\n"

        l = len(result)
        result += "-" * l + "\n"

        for i in range(len(self.results)):
            r = self.results[i]
            result += f"★ {r}"
            if i != len(self.results) - 1:
                result += "\n"
        return result

    def get_global_state(self):
        for r in self.results:
            if r.state == PortState.OPEN:
                return PortState.OPEN
        for r in self.results:
            if r.state == PortState.CLOSED:
                return PortState.CLOSED
        return PortState.FILTERED

    def is_important(self):
        if self.state == PortState.FILTERED:
            return False
        return True
