from ipaddress import IPv4Address
from scapy.all import ICMP, IP, sr1, TCP

from models.enums import PortScanMethod, PortState
from models.results import PortScanResult
from models.utils import TCPFlags
from models.packets import TCPPacket, ICMPPacket


def fin_scan(ip: IPv4Address, port: int) -> PortScanResult:
    try:
        flags = TCPFlags.to_bytes(["FIN"])
        packet = IP(dst=str(ip)) / TCP(flags=flags, dport=port)
        res = sr1(packet, timeout=2, verbose=0)

        if res is not None:
            if res.haslayer(TCP):

                tcp_packet = TCPPacket(res)

                if "RST" in tcp_packet.flags:
                    return PortScanResult(
                        ip=ip,
                        port=port,
                        state=PortState.CLOSED,
                        method=PortScanMethod.FIN,
                        icmp=None,
                        tcp=tcp_packet
                    )

            if res.haslayer(ICMP):

                icmp_packet = ICMPPacket(res)

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
