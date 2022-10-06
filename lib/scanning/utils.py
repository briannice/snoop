from ipaddress import IPv4Address
from utils import SnoopException


class HostState():
    HOST_STATES = {
        0: "UP",
        1: "DOWN",
        2: "UNKOWN"
    }

    def __init__(self, state: int = 0):
        if state < 0 or state > len(self.HOST_STATES):
            raise SnoopException("Invalid state number for host.")
        self.state = state

    def __str__(self) -> str:
        return self.get_state_name()

    def get_state_name(self) -> str:
        for key, value in self.HOST_STATES.items():
            if key == self.state:
                return value


class PortState():

    PORT_STATES = {
        0: "OPEN",
        1: "CLOSED",
        2: "FILTERED",
        3: "UNFILTERED",
        4: "OPEN | FILTERED",
        5: "CLOSED | FILTERED",
    }

    def __init__(self, state: int = 0):
        if state < 0 or state > len(self.PORT_STATES):
            raise SnoopException("Invalid state number for port.")
        self.state = state

    def __str__(self) -> str:
        return self.get_state_name()

    def get_state_name(self) -> str:
        for key, value in self.PORT_STATES.items():
            if key == self.state:
                return value


class TCPScanResult():

    TCP_FLAGS = {
        "FIN": 0x01,
        "SYN": 0x02,
        "RST": 0x04,
        "PSH": 0x08,
        "ACK": 0x10,
        "URG": 0x20,
        "ECE": 0x40,
        "CWR": 0x80
    }

    def __init__(
        self,
        dest_ip: IPv4Address,
        dest_port: int,
        flags: int,
        port_state: PortState,
        scan_type: str
    ):
        self.dest_ip = dest_ip
        self.dest_port = dest_port
        self.port_state = port_state
        self.flags = flags
        self.scan_type = scan_type

    def __str__(self) -> str:
        return f"[TCP {self.scan_type}] {self.dest_ip}:{self.dest_port} - {self.port_state}"

    def get_flags_list(self):
        flags = self.flags
        result = []
        for key in self.TCP_FLAGS.keys():
            if flags & 1:
                result.append(key)
            flags = flags >> 1
        return result


def ICMPScanResult():

    def __init__(
        self,
        dest_ip: IPv4Address,
        icmp_type: int,
        icmp_code: int,
    ):
        pass

    def __str__(self):
        pass
