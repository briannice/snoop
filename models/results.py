from ipaddress import IPv4Address
from typing import List

from .enums import HostState, PortState, PortScanMethod
from .packets import ICMPPacket, TCPPacket


class HostScanResult():

    def __init__(
        self,
        ip: IPv4Address,
        state: HostState,
        icmp: ICMPPacket | None,
        tcp: TCPPacket | None
    ):
        self.ip = ip
        self.state = state
        self.icmp = icmp
        self.tcp = tcp

    def __str__(self) -> str:
        return f"{self.ip}: {self.state}"

    def get_packet(self) -> ICMPPacket | TCPPacket | None:
        if self.icmp:
            return self.icmp
        if self.tcp:
            return self.tcp
        return None

    def is_up(self) -> bool:
        return self.state == HostState.UP

    def is_unknown(self) -> bool:
        return self.state == HostState.UNKNOWN

    def is_blocked(self) -> bool:
        return self.state == HostState.BLOCKED


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

    def __str__(self) -> str:
        return f"{self.method: <10}   →   {self.state}"


class PortScanConclusion():

    def __init__(self, port: int, results: List[PortScanResult]):
        self.port = port
        self.results = results
        self.state = self.get_global_state()

    def __str__(self) -> str:
        result = ""

        result += f"{self.port: <12}   →   {self.state}\n"

        l = len(result)
        result += "-" * l + "\n"

        for i in range(len(self.results)):
            r = self.results[i]
            result += f"★ {r}"
            if i != len(self.results) - 1:
                result += "\n"
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
