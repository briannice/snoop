from ipaddress import IPv4Address
from scapy.all import ICMP, IP, send, sr1, TCP

from models.enums import PortScanMethod, PortState, HostState, HostScanMethod
from models.results import PortScanResult, HostScanResult
from models.utils import TCPFlags
from models.packets import TCPPacket, ICMPPacket


def stealth_scan(ip: IPv4Address, port: int) -> PortScanResult:
    try:
        flags = TCPFlags.to_bytes(["SYN"])
        packet = IP(dst=str(ip)) / TCP(flags=flags, dport=port)
        res = sr1(packet, timeout=2, verbose=0)

        if res is not None:
            if res.haslayer(TCP):
                tcp_packet = TCPPacket(res)
                if 'SYN' in tcp_packet.flags:
                    result = PortScanResult(
                        ip=ip,
                        port=port,
                        state=PortState.OPEN,
                        method=PortScanMethod.STEALTH,
                        icmp=None,
                        tcp=tcp_packet
                    )

                    flags = TCPFlags.to_bytes(["RST"])
                    packet = IP(dst=str(ip)) / TCP(flags=flags, dport=port)
                    send(packet, verbose=0)

                    return result

                if "RST" in tcp_packet.flags:
                    return PortScanResult(
                        ip=ip,
                        port=port,
                        state=PortState.CLOSED,
                        method=PortScanMethod.STEALTH,
                        icmp=None,
                        tcp=tcp_packet
                    )
            if res.haslayer(ICMP):
                icmp_packet = ICMPPacket(res)
                return PortScanResult(
                    ip=ip,
                    port=port,
                    state=PortState.FILTERED,
                    method=PortScanMethod.STEALTH,
                    icmp=icmp_packet,
                    tcp=None
                )

        return PortScanResult(
            ip=ip,
            port=port,
            state=PortState.FILTERED,
            method=PortScanMethod.STEALTH,
            icmp=None,
            tcp=None
        )

    except Exception as e:
        print(e)
        return PortScanResult(
            ip=ip,
            port=port,
            state=PortState.INTERNAL_ERROR,
            method=PortScanMethod.STEALTH,
            icmp=None,
            tcp=None
        )


def host_stealth_scan(ip: IPv4Address, port: int, method: HostScanMethod):
    scan = stealth_scan(ip, port)

    if scan.state.value == "OPEN" or scan.state.value == "CLOSED":
        return HostScanResult(
            ip=ip,
            state=HostState.UP,
            method=method,
            icmp=scan.icmp,
            tcp=scan.tcp
        )
    elif scan.state.value == "INTERNAL ERROR":
        return HostScanResult(
            ip=ip,
            state=HostState.INTERNAL_ERROR,
            method=method,
            icmp=scan.icmp,
            tcp=scan.tcp
        )
    elif scan.icmp is not None:
        return HostScanResult(
            ip=ip,
            state=HostState.BLOCKED,
            method=method,
            icmp=scan.icmp,
            tcp=scan.tcp
        )
    else:
        return HostScanResult(
            ip=ip,
            state=HostState.UNKNOWN,
            method=method,
            icmp=scan.icmp,
            tcp=scan.tcp
        )
