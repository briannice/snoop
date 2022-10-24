from enum import Enum


class HostState(Enum):
    UP = "UP"
    BLOCKED = "BLOCKED"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return self.value


class PortState(Enum):
    OPEN = "OPEN"
    CLOSED = "CLOSED"
    FILTERED = "FILTERED"
    UNFILTERED = "UNFILTERED"
    OPEN_FILTERED = "OPEN | FILTERED"
    CLOSED_FILTERED = "CLOSED | FILTERED"
    INTERNAL_ERROR = "INTERNAL ERROR"

    def __str__(self) -> str:
        return self.value


class PortScanMethod(Enum):
    CONNECT = "CONNECT"
    STEALTH = "STEALTH"
    XMAS = "XMAS"
    FIN = "FIN"
    ACK = "ACK"
    NULL = "NULL"

    def __str__(self) -> str:
        return self.value

    @staticmethod
    def dict_to_list(dct):
        result = []
        for k, v in dct.items():
            if v:
                match k:
                    case "ack":
                        result.append(PortScanMethod.ACK)
                    case "connect":
                        result.append(PortScanMethod.CONNECT)
                    case "stealth":
                        result.append(PortScanMethod.STEALTH)
                    case "fin":
                        result.append(PortScanMethod.FIN)
                    case "xmas":
                        result.append(PortScanMethod.XMAS)
                    case "null":
                        result.append(PortScanMethod.NULL)
        return result
