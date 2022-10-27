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

            icmp_packet = ICMPPacket(res)

            if icmp_packet.type == 0:
                return HostScanResult(
                    ip=ip,
                    state=HostState.UP,
                    method=HostScanMethod.PING,
                    icmp=icmp_packet,
                    tcp=None
                )

            if icmp_packet.type == 3:
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
