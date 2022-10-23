from ipaddress import IPv4Address

from .ack_scan import ack_scan
from .connect_scan import connect_scan
from .fin_scan import fin_scan
from .null_scan import null_scan
from .stealth_scan import stealth_scan
from .utils import PortScanMethod
from .xmas_scan import xmas_scan

from utils import SnoopException


def port_scan(ip: IPv4Address, port: int, method: PortScanMethod):
    match method:
        case PortScanMethod.ACK:
            return ack_scan(ip, port)
        case PortScanMethod.CONNECT:
            return connect_scan(ip, port)
        case PortScanMethod.FIN:
            return fin_scan(ip, port)
        case PortScanMethod.NULL:
            return null_scan(ip, port)
        case PortScanMethod.STEALTH:
            return stealth_scan(ip, port)
        case PortScanMethod.XMAS:
            return xmas_scan(ip, port)
        case _:
            raise SnoopException("Invalid port scan method")
