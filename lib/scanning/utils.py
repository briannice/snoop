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

    SCAPY_FLAGS = {
        'F': 'FIN',
        'S': 'SYN',
        'R': 'RST',
        'P': 'PSH',
        'A': 'ACK',
        'U': 'URG',
        'E': 'ECE',
        'C': 'CWR',
    }

    def __init__(
        self,
        source_ip: IPv4Address,
        dest_ip: IPv4Address,
        source_port: int,
        dest_port: int,
        scapy_flags: int,
        port_state: PortState
    ):
        self.source_ip = source_ip
        self.dest_ip = dest_ip
        self.source_port = source_port
        self.dest_port = dest_port
        self.flags = self.initialise_flags(scapy_flags)
        self.port_state = port_state

    def __str__(self) -> str:
        return f"[TCP] - {self.port_state} - {self.flags} - {self.get_flags_list()}"

    def get_flags_list(self):
        flags = self.flags
        flags_list = list(self.TCP_FLAGS.keys())
        result = []

        for i in range(len(flags_list)):
            if flags & 1:
                result.append(flags_list[i])
            flags = flags >> 1

        return result

    def initialise_flags(self, scapy_flags):
        result = 0b0
        for f in scapy_flags:
            result |= self.TCP_FLAGS[self.SCAPY_FLAGS[f]]
        return result
