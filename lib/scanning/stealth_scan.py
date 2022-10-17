from ipaddress import IPv4Address
from scapy.all import ICMP, IP, sr1, TCP

from .utils import ICMPPacket, PortScanResult, PortState, TCPFlags, TCPPacket


def stealth_scan(ip: IPv4Address, port: int) -> PortScanResult:
    flags = TCPFlags.to_bytes(["SYN"])
    packet = IP(dst=str(ip)) / TCP(flags=flags, dport=port)
    res = sr1(packet, timeout=2, verbose=0)

    if res is not None:
        src_ip = res.getlayer(IP).src
        dst_ip = res.getlayer(IP).dst
        if res.haslayer(TCP):
            flags = res.getlayer(TCP).flags
            flags = TCPFlags.to_list(flags)
            dst_port = res.getlayer(TCP).dport
            src_port = res.getlayer(TCP).sport

            tcp_packet = TCPPacket(
                dst_ip=dst_ip,
                src_ip=src_ip,
                dst_port=dst_port,
                flags=flags,
                src_port=src_port,
            )

            if "SYN" in flags:
                print(flags)
                return PortScanResult(
                    dst_ip=ip,
                    dst_port=port,
                    port_state=PortState.OPEN,
                    icmp_packet=None,
                    tcp_packet=tcp_packet
                )

            if "RST" in flags:
                return PortScanResult(
                    dst_ip=ip,
                    dst_port=port,
                    port_state=PortState.CLOSED,
                    icmp_packet=None,
                    tcp_packet=tcp_packet
                )

        if res.haslayer(ICMP):
            type = res.getlayer(ICMP).type
            code = res.getlayer(ICMP).code

            icmp_packet = ICMPPacket(
                code=code,
                dst_ip=dst_ip,
                src_ip=src_ip,
                type=type
            )

            return PortScanResult(
                dst_ip=ip,
                dst_port=port,
                port_state=PortState.FILTERED,
                icmp_packet=icmp_packet,
                tcp_packet=None
            )

    return PortScanResult(
        dst_ip=ip,
        dst_port=port,
        port_state=PortState.FILTERED,
        icmp_packet=None,
        tcp_packet=None
    )
