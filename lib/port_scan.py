from ipaddress import IPv4Address
import random
from scapy.all import ICMP, IP, sr1, TCP, ls


class PortScanResult():

    def __init__(
        self,
        ip: IPv4Address = IPv4Address("127.0.0.1"),
        type: str = "",
        port: int = -1,
        message: str = ""
    ):
        self.port = port
        self.ip = ip
        self.message = message
        self.type = type

    def __str__(self):
        if self.port != -1:
            return f"{str(self.ip)}:{self.port} --> {self.message}"
        else:
            return f"{str(self.ip)} --> {self.message}"


def port_scan_ping(ip: IPv4Address) -> PortScanResult:
    """
    Execute a port scan on a target host using an ICMP echo request.

    First an ICMP packet should be created. Because the ICMP message is an echo
    request, the type of the ICMP packet should be 8. The ICMP packet must be
    encapsulated by an IPv4 packet. The source IPv4 address of the IP packet
    must be the address of the host that is sending the echo request. The
    destination IPv4 address of the IP packet must be the address of the target
    host.

    The result of the port scan can be determined by the response of the echo
    request.

    - If the response does not exist, the target host can be down, or it is
      blocking the ICMP echo request.

    - 

    Args:
        ip (IPv4Address): IPv4 address of the target host.

    Returns:
        PortScanResult: Result of the port scan.
    """

    # IPv4Address of the target host
    ip_dst = str(ip)
    icmp_type = 8
    packet = IP(dst=ip_dst) / ICMP(type=icmp_type)
    response = sr1(packet, timeout=2, verbose=0)

    if response is None:
        return PortScanResult(
            ip=ip,
            type="PING",
            message="down or not responding"
        )
    elif (
        int(response.getlayer(ICMP).type) == 3 and
        int(response.getlayer(ICMP).code) in [1, 2, 3, 9, 10, 13]
    ):
        return PortScanResult(ip=ip, type="PING", message="not responding")
    else:
        return PortScanResult(ip=ip, type="PING", message="responding")


def port_scan_tcp_half_open():
    pass


def port_scan_tcp_connect():
    pass


def port_scan():
    pass


if __name__ == '__main__':
    psr = port_scan_ping(IPv4Address("192.168.1.1"))
