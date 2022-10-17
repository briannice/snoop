from ipaddress import IPv4Address
from scapy.all import ICMP, IP, sr1

from .utils import HostScanResult, HostState, ICMPPacket


def ping_scan(ip: IPv4Address) -> HostScanResult:

    packet = IP(dst=str(ip)) / ICMP(type=8)
    res = sr1(packet, timeout=2, verbose=0)

    if res is not None and res.haslayer(ICMP):
        ip_src_ip = res.getlayer(IP).src
        ip_dst_ip = res.getlayer(IP).dst
        icmp_type = res.getlayer(ICMP).type
        icmp_code = res.getlayer(ICMP).code

        icmp_packet = ICMPPacket(
            src_ip=ip_src_ip,
            dst_ip=ip_dst_ip,
            type=icmp_type,
            code=icmp_code
        )

        if icmp_type == 0:
            return HostScanResult(
                dst_ip=ip,
                host_state=HostState.UP,
                icmp_packet=icmp_packet,
                tcp_packet=None
            )

        if icmp_type == 3 and icmp_code in []:
            return HostScanResult(
                dst_ip=ip,
                host_state=HostState.BLOCKED,
                icmp_packet=icmp_packet,
                tcp_packet=None
            )

    return HostScanResult(
        dst_ip=ip,
        host_state=HostState.UNKNOWN,
        icmp_packet=None,
        tcp_packet=None
    )
