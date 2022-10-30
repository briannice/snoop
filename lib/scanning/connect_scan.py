from ipaddress import IPv4Address
from scapy.all import ICMP, IP, send, sr1, TCP

from models.enums import PortScanMethod, PortState
from models.results import PortScanResult
from models.utils import TCPFlags
from models.packets import TCPPacket, ICMPPacket


def connect_scan(ip: IPv4Address, port: int) -> PortScanResult:
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
                        method=PortScanMethod.CONNECT,
                        icmp=None,
                        tcp=tcp_packet
                    )

                    flags = TCPFlags.to_bytes(["ACK"])
                    packet = IP(dst=str(ip)) / TCP(flags=flags, dport=port)
                    send(packet, verbose=0)

                    return result

                if "RST" in tcp_packet.flags:
                    return PortScanResult(
                        ip=ip,
                        port=port,
                        state=PortState.CLOSED,
                        method=PortScanMethod.CONNECT,
                        icmp=None,
                        tcp=tcp_packet
                    )

            if res.haslayer(ICMP):
                icmp_type = res.getlayer(ICMP).type
                icmp_code = res.getlayer(ICMP).code
                if icmp_type == 3 and icmp_code in [1, 2, 3, 9, 10, 13]:
                    icmp_packet = ICMPPacket(res)
                    return PortScanResult(
                        ip=ip,
                        port=port,
                        state=PortState.FILTERED,
                        method=PortScanMethod.CONNECT,
                        icmp=icmp_packet,
                        tcp=None
                    )

        return PortScanResult(
            ip=ip,
            port=port,
            state=PortState.FILTERED,
            method=PortScanMethod.CONNECT,
            icmp=None,
            tcp=None
        )

    except Exception as e:
        print(e)
        return PortScanResult(
            ip=ip,
            port=port,
            state=PortState.INTERNAL_ERROR,
            method=PortScanMethod.CONNECT,
            icmp=None,
            tcp=None
        )
