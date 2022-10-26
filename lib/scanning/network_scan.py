from ipaddress import IPv4Address

from .ping_scan import ping_scan
from .stealth_scan import host_stealth_scan

from models.enums import HostScanMethod
from utils import SnoopException


def network_scan(ip: IPv4Address, method: HostScanMethod):
    match method:
        case HostScanMethod.PING:
            return ping_scan(ip)
        case HostScanMethod.SSH:
            return host_stealth_scan(ip, 22, HostScanMethod.SSH)
        case HostScanMethod.HTTP:
            return host_stealth_scan(ip, 80, HostScanMethod.HTTP)
        case HostScanMethod.HTTPS:
            return host_stealth_scan(ip, 443, HostScanMethod.HTTPS)
        case _:
            raise SnoopException("Invalid host scan method")
