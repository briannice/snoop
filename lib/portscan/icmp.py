from ipaddress import IPv4Address
from scapy.all import ICMP, IP, sr1


class PortScanICMPResult():

    def __init__(
        self,
        ip: IPv4Address = IPv4Address("127.0.0.1"),
        reply_type: int = 0,
        reply_code: int = 0,
    ):
        self.ip = ip
        self.type = reply_type
        self.code = reply_code

    def __str__(self):
        return f"{str(self.ip)}:{self.port} --> {self.message}"


def port_scan_ping(ip: IPv4Address) -> PortScanICMPResult:
    """
    Executa port scan on a target host with the given IP address using an
    ICMP echo request.

    Args:
        ip (IPv4Address): IPv4 address of the target host.

    Returns:
        PortScanResult: Result of the port scan.
    """

    # IPv4Address of the target host.
    ip_dst = str(ip)

    # Type of the ICMP packet.
    # Echo request has type 8.
    icmp_type = 8

    # Create ICMP packet.
    packet = IP(dst=ip_dst) / ICMP(type=icmp_type)

    # Send packet and wait for first response.
    response = sr1(packet, timeout=2, verbose=0)

    #
    if response is None:
        return PortScanICMPResult(
            ip=ip,
            type="PING",
            message="down or not responding"
        )
    elif (
        int(response.getlayer(ICMP).type) == 3 and
        int(response.getlayer(ICMP).code) in [1, 2, 3, 9, 10, 13]
    ):
        return PortScanICMPResult(ip=ip, type="PING", message="not responding")
    else:
        return PortScanICMPResult(ip=ip, type="PING", message="responding")
