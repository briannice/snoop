from ipaddress import IPv4Address, IPv4Network
from multiprocessing import Manager, Process
from scapy.all import ICMP, IP, sr1
from typing import List


class PortScanICMPResult():

    def __init__(
        self,
        ip: IPv4Address = IPv4Address("127.0.0.1"),
        reply_type: int = 0,
        reply_code: int = 0,
        message: str = "Not responding"
    ):
        self.ip = ip
        self.type = reply_type
        self.code = reply_code
        self.message = message

    def __str__(self):
        return f"{str(self.ip)} --> {self.message}"


def _port_scan_ping(ip: IPv4Address, result_list: List[PortScanICMPResult]):
    """
    Executa port scan on a target host with the given IP address using an
    ICMP echo request.

    Args:
        ip (IPv4Address): IPv4 address of the target host.

    Returns:
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
        result = PortScanICMPResult(
            ip=ip,
        )

    elif (
        int(response.getlayer(ICMP).type) == 3 and
        int(response.getlayer(ICMP).code) in [1, 2, 3, 9, 10, 13]
    ):
        reply_type = response.getlayer(ICMP).type
        reply_code = response.getlayer(ICMP).code

        result = PortScanICMPResult(
            ip=ip,
            reply_type=reply_type,
            reply_code=reply_code,
            message="Not responding"
        )

    else:
        reply_type = response.getlayer(ICMP).type
        reply_code = response.getlayer(ICMP).code

        result = PortScanICMPResult(
            ip=ip,
            reply_type=reply_type,
            reply_code=reply_code,
            message="Up"
        )

    result_list.append(result)


def port_scan_ping(network: IPv4Network) -> List[PortScanICMPResult]:
    manager = Manager()
    result = manager.list()
    tasks = []

    for ip_address in network.hosts():
        task = Process(target=_port_scan_ping, args=(ip_address, result))
        tasks.append(task)
        task.start()

    for task in tasks:
        task.join()

    return result
