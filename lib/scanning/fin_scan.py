from ipaddress import IPv4Address
from scapy.all import ICMP, IP, sr1, TCP

from .utils import ICMPPacket, PortScanMethod, PortScanResult, PortState, TCPFlags, TCPPacket


def fin_scan(ip: IPv4Address, port: int) -> PortScanResult:
    try:
        flags = TCPFlags.to_bytes(["FIN"])
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

                if "RST" in flags:
                    return PortScanResult(
                        ip=ip,
                        port=port,
                        state=PortState.CLOSED,
                        method=PortScanMethod.FIN,
                        icmp=None,
                        tcp=tcp_packet
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
                    ip=ip,
                    port=port,
                    state=PortState.FILTERED,
                    method=PortScanMethod.FIN,
                    icmp=icmp_packet,
                    tcp=None
                )

        return PortScanResult(
            ip=ip,
            port=port,
            state=PortState.OPEN_FILTERED,
            method=PortScanMethod.FIN,
            icmp=None,
            tcp=None
        )

    except Exception as e:
        print(e)
        return PortScanResult(
            ip=ip,
            port=port,
            state=PortState.INTERNAL_ERROR,
            method=PortScanMethod.FIN,
            icmp=None,
            tcp=None
        )
