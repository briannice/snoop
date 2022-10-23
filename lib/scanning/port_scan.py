from ipaddress import IPv4Address

from .ack_scan import ack_scan
from .connect_scan import connect_scan
from .stealth_scan import stealth_scan
from .utils import PortScanMethod

from utils import SnoopException


def port_scan(ip: IPv4Address, port: int, method: PortScanMethod):
    match method:
        case PortScanMethod.CONNECT:
            return connect_scan(ip, port)
        case PortScanMethod.STEALTH:
            return stealth_scan(ip, port)
        case PortScanMethod.ACK:
            return ack_scan(ip, port)
        case _:
            raise SnoopException("Invalid port scan method")
