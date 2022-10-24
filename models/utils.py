from typing import List


class TCPFlags():
    FLAGS = {
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
        "F": "FIN",
        "S": "SYN",
        "R": "RST",
        "P": "PSH",
        "A": "ACK",
        "U": "URG",
        "E": "ECE",
        "C": "CWR"
    }

    @staticmethod
    def to_bytes(flags: List[str]) -> int:
        result = 0x0
        for f in flags:
            result |= TCPFlags.FLAGS[f]
        return result

    @staticmethod
    def to_list(bytes: int) -> List[str]:
        result = []
        for k, _ in TCPFlags.FLAGS.items():
            if bytes & 1 > 0:
                result.append(k)
            bytes >>= 1
        return result

    @staticmethod
    def to_list(flags: str) -> List[str]:
        result = []
        for f in flags:
            result.append(TCPFlags.SCAPY_FLAGS[f])
        return result
