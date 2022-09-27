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
        result: str = "FILTERED"
    ):
        self.ip = ip
        self.port = port
        self.flag = flag
        self.flags = flags
        self.result = result

    def __str__(self):
        return f"[TCP OPEN] - {self.ip}:{self.port} - {self.result} - {self.flags} - {hex(self.flag)}"


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
        if "ACK" in flags:
            return PortScanTCPResult(
                ip=ip,
                port=port,
                flag=flag,
                flags=flags,
                result="OPEN"
            )

        #
        elif "RST" in flags:
            return PortScanTCPResult(
                ip=ip,
                port=port,
                flag=flag,
                flags=flags,
                result="CLOSED"
            )

    return PortScanTCPResult(
        ip=ip,
        port=port,
        result="FILTERED"
    )


def port_scan_tcp_connect():
    pass


if __name__ == "__main__":
    ports = [20, 21, 22, 80, 443]
    ip = IPv4Address("192.168.56.90")

    for port in ports:
        print(port_scan_tcp_half_open(ip=ip, port=port))
