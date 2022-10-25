from ipaddress import IPv4Address
from scapy.all import ICMP, IP, sr1

from models.enums import HostState, HostScanMethod
from models.results import HostScanResult
from models.packets import ICMPPacket


def ping_scan(ip: IPv4Address) -> HostScanResult:
    try:
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
                    ip=ip,
                    state=HostState.UP,
                    method=HostScanMethod.PING,
                    icmp=icmp_packet,
                    tcp=None
                )

            if icmp_type == 3 and icmp_code in []:
                return HostScanResult(
                    ip=ip,
                    state=HostState.BLOCKED,
                    method=HostScanMethod.PING,
                    icmp=icmp_packet,
                    tcp=None
                )

        return HostScanResult(
            ip=ip,
            state=HostState.UNKNOWN,
            method=HostScanMethod.PING,
            icmp=None,
            tcp=None
        )
    except Exception as e:
        print(e)
        return HostScanResult(
            ip=ip,
            state=HostState.INTERNAL_ERROR,
            method=HostScanMethod.PING,
            icmp=None,
            tcp=None
        )
