from ipaddress import IPv4Address
from random import randint
from typing import List
from scapy.all import IP, TCP, sr1

_TCP_FLAGS = {
    "NULL": 0x00,
    "FIN": 0x01,
    "SYN": 0x02,
    "RST": 0x04,
    "PSH": 0x08,
    "ACK": 0x10,
    "URG": 0x20,
    "ECE": 0x40,
    "CWR": 0x80
}

_TCP_SCAPY_FLAGS = {
    'F': 'FIN',
    'S': 'SYN',
    'R': 'RST',
    'P': 'PSH',
    'A': 'ACK',
    'U': 'URG',
    'E': 'ECE',
    'C': 'CWR',
}

_TCP_FLAGS_LIST = [
    "NULL",
    "FIN",
    "SYN",
    "RST",
    "PSH",
    "ACK",
    "URG",
    "ECE",
    "CWR"
]


class PortScanTCPResult():

    def __init__(
        self,
        ip: IPv4Address = IPv4Address("127.0.0.1"),
        port: int = 0,
        flag: int = 0x00,
        flags: List[str] = ["NULL"],
        result: str = "FILTERED",
        scan_type: str = "OPEN"
    ):
        self.ip = ip
        self.port = port
        self.flag = flag
        self.flags = flags
        self.result = result
        self.scan_type = scan_type

    def __str__(self):
        return f"[TCP {self.scan_type}] - {self.ip}:{self.port} - {self.result} - {self.flags} - {hex(self.flag)}"


def _create_flag_list(flag: int) -> List[str]:
    result = []
    for f in flag:
        result.append(_TCP_SCAPY_FLAGS[f])
    if len(result) == 0:
        return [_TCP_FLAGS_LIST[0]]
    return result


def _create_flag_number(flags: List[str]) -> int:
    result = 0b0
    for f in flags:
        result |= _TCP_FLAGS[f]
    return result


def port_scan_tcp_half_open(ip: IPv4Address, port: int) -> PortScanTCPResult:
    """
    Execute a port scan on a target host with the given IP address using a TCP
    SYN request leaving the connection open on the target host.
    """

    src_port = randint(0, 65535)
    dst_port = port
    dst_ip = str(ip)
    flags = 0x02

    segment = IP(dst=dst_ip) / TCP(sport=src_port, dport=dst_port, flags=flags)
    response = sr1(segment, timeout=2, verbose=0)

    # Check if there is a response and if that response has a TCP layer.
    if response is not None and response.haslayer(TCP):
        flags = _create_flag_list(response.getlayer(TCP).flags)
        flag = _create_flag_number(flags)

        #
        if "ACK" in flags and "SYN" in flags:
            return PortScanTCPResult(
                ip=ip,
                port=port,
                flag=flag,
                flags=flags,
                result="OPEN",
                scan_type="OPEN"
            )

        #
        elif "ACK" in flags and "RST" in flags:
            return PortScanTCPResult(
                ip=ip,
                port=port,
                flag=flag,
                flags=flags,
                result="CLOSED",
                scan_type="OPEN"
            )

    return PortScanTCPResult(
        ip=ip,
        port=port,
        result="FILTERED",
        scan_type="OPEN"
    )


def port_scan_tcp_connect(ip: IPv4Address, port: int) -> PortScanTCPResult:
    """
    Execute a port scan on a target host with the given IP address using a TCP
    SYN request closing the connection on the target host.
    """

    tcp_sport = randint(0, 65535)
    tcp_dport = port
    tcp_flags = 0x02
    ip_dst = str(ip)

    # Create a TCP segment
    segment = \
        IP(dst=ip_dst) / \
        TCP(sport=tcp_sport, dport=tcp_dport, flags=tcp_flags)

    response = sr1(segment, timeout=2, verbose=0)

    # Check if there is a response and if that response has a TCP layer.
    if response is not None and response.haslayer(TCP):
        flags = _create_flag_list(response.getlayer(TCP).flags)
        flag = _create_flag_number(flags)

        #
        if "ACK" in flags and "SYN" in flags:
            tcp_flags = 0x10

            segment = \
                IP(dst=ip_dst) / \
                TCP(sport=tcp_sport, dport=tcp_dport, flags=tcp_flags)

            sr1(segment, timeout=2, verbose=0)

            return PortScanTCPResult(
                ip=ip,
                port=port,
                flag=flag,
                flags=flags,
                result="OPEN",
                scan_type="CONNECT"
            )

        elif "ACK" in flags and "RST" in flags:
            return PortScanTCPResult(
                ip=ip,
                port=port,
                flag=flag,
                flags=flags,
                result="CLOSED",
                scan_type="CONNECT"
            )

    return PortScanTCPResult(
        ip=ip,
        port=port,
        result="FILTERED",
        scan_type="CONNECT"
    )
