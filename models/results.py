from ipaddress import IPv4Address
from typing import List
from utils.formating import format_key_value

from .enums import HostState, PortState, PortScanMethod, HostScanMethod
from .scanning import ICMPPacket, TCPPacket


class HostScanResult():

    def __init__(
        self,
        ip: IPv4Address,
        state: HostState,
        method: HostScanMethod,
        icmp: ICMPPacket | None,
        tcp: TCPPacket | None
    ):
        self.ip = ip
        self.state = state
        self.method = method
        self.icmp = icmp
        self.tcp = tcp

    def to_text_short(self):
        return format_key_value(key=self.method, value=self.state, list=True)

    def to_text_extended(self) -> str:
        result = ""
        result += format_key_value(key=self.method, value=self.state, sep="=", nl=True)
        if self.icmp is not None:
            result += self.icmp.to_text_extended()
        elif self.tcp is not None:
            result += self.tcp.to_text_extended()
        elif self.state.value == "INTERNAL ERROR":
            result += "INTERNAL ERROR\n"
        else:
            result += "NO RESPONSE\n"
        return result


class HostScanConclusion():

    def __init__(self, host: IPv4Address, results: List[PortScanMethod]):
        self.host = host
        self.results = results
        self.state = self.get_global_state()

    def to_text_short(self) -> str:
        result = ""
        result += format_key_value(key=str(self.host), value=self.state, sep="-")
        for r in self.results:
            result += r.to_text_short()
        return result

    def to_text_extended(self) -> str:
        result = ""
        for r in self.results:
            result += r.to_text_extended()
            result += "\n\n"
        return result

    def get_global_state(self):
        for r in self.results:
            if r.state.value == "UP":
                return "UP"
        for r in self.results:
            if r.state.value == "BLOCKED":
                return "BLOCKED"
        return "UNKNOWN"

    def is_important(self) -> bool:
        if "UNKNOWN" in self.state:
            return False
        return True


class PortScanResult():

    def __init__(
        self,
        ip: IPv4Address,
        port: int,
        state: PortState,
        method: PortScanMethod,
        icmp: ICMPPacket | None,
        tcp: TCPPacket | None
    ):
        self.ip = ip
        self.port = port
        self.state = state
        self.method = method
        self.icmp = icmp
        self.tcp = tcp

    def to_text_short(self) -> str:
        return format_key_value(key=self.method, value=self.state, list=True)

    def to_text_extended(self) -> str:
        result = ""
        result += format_key_value(key=self.method, value=self.state, sep="=", nl=True)
        if self.icmp is not None:
            result += self.icmp.to_text_extended()
        elif self.tcp is not None:
            result += self.tcp.to_text_extended()
        elif self.state.value == "INTERNAL ERROR":
            result += "INTERNAL ERROR\n"
        else:
            result += "NO RESPONSE\n"
        return result


class PortScanConclusion():

    def __init__(self, port: int, results: List[PortScanResult]):
        self.port = port
        self.results = results
        self.state = self.get_global_state()

    def to_text_short(self) -> str:
        result = ""
        result += format_key_value(key=self.port, value=self.state, sep="-")
        for r in self.results:
            result += r.to_text_short()
        return result

    def to_text_extended(self) -> str:
        result = ""
        for r in self.results:
            result += r.to_text_extended()
            result += "\n\n"
        return result

    def get_global_state(self) -> List[str]:
        result = set(["OPEN", "CLOSED", "FILTERED"])
        for r in self.results:
            match r.state.value:
                case "OPEN":
                    return "OPEN"
                case "CLOSED":
                    return "CLOSED"
                case "UNFILTERED":
                    result = result.intersection(["OPEN", "CLOSED"])
                case "OPEN | FILTERED":
                    result = result.intersection(["OPEN", "FILTERED"])
                case "CLOSED | FILTERED":
                    result = result.intersection(["CLOSED", "FILTERED"])

        if len(result) == 3:
            result = set(["FILTERED"])

        result_str = ""
        for r in result:
            result_str += r
            result_str += " | "
        if len(result_str) > 0:
            result_str = result_str[:len(result_str) - 2]
        return result_str

    def is_important(self):
        if "FILTERED" in self.state:
            return False
        return True
