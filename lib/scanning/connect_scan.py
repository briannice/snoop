from ipaddress import IPv4Address

from .utils import PortScanResult, PortState


def connect_scan(ip: IPv4Address, port: int) -> PortScanResult:

    return PortScanResult(
        dst_ip=ip,
        dst_port=port,
        port_state=PortState.FILTERED,
        icmp_packet=None,
        tcp_packet=None
    )
