from ipaddress import IPv4Address
from scapy.all import ICMP, IP, sr1


class PingScanResult():
    """
    Represents the result of a ping scan.


    Attributes
    ==========

    * ip (IPv4Address): IPv4 address of the target of the ping scan.
        
    * reply_type (int): ICMP type number of the reply.

    * reply_code (int): ICMP code number according to the type number.

    * result (str): result of the ping scan.
    
    """

    RESULTS = {
        0: 'UP',
        1: 'DOWN OR BLOCKED',
        2: 'BLOCKED'
    }

    def __init__(
        self,
        ip: IPv4Address = IPv4Address("127.0.0.1"),
        reply_type: int = -1,
        reply_code: int = -1,
        result: int = 0
    ):
        self.ip = ip
        self.type = reply_type
        self.code = reply_code
        self.result = result

    def __str__(self):
        return f"{str(self.ip)} --> {self.get_result_verbose()}"

    def get_result_verbose(self):
        return self.RESULTS[self.result]


def ping_scan(ip: IPv4Address) -> PingScanResult:
    """
    Execute a ping scan on a target with the given IP address.

    Args
    ====

    * ip (IPv4Address): IPv4 address of the target.

    Returns
    =======

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
        return PingScanResult(
            ip=ip,
            result=1
        )
        
    else:
        reply_type = response.getlayer(ICMP).type
        reply_code = response.getlayer(ICMP).code

        if reply_type == 3 and reply_code in [1, 2, 3, 9, 10, 13]:
            return PingScanResult(
                ip=ip,
                reply_type=reply_type,
                reply_code=reply_code,
                result=2
            )

        else:
            return PingScanResult(
                ip=ip,
                reply_type=reply_type,
                reply_code=reply_code,
                result=0
            )
