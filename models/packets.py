from ipaddress import IPv4Address
from models.utils import TCPFlags
from utils import format_key, format_key_value
from typing import List


class ICMPPacket():

    def __init__(
        self,
        src_ip: IPv4Address,
        dst_ip: IPv4Address,
        type: int,
        code: int,
    ):
        self.type = type
        self.code = code
        self.src_ip = src_ip
        self.dst_ip = dst_ip

    def to_text_extended(self):
        result = ""
        result += format_key(key="ICMP", type="title")
        result += format_key_value(key="Src IP", value=str(self.src_ip), type="item")
        result += format_key_value(key="Dst IP", value=str(self.dst_ip), type="item")
        result += format_key_value(key="Type", value=str(self.type), type="item")
        result += format_key_value(key="Code", value=str(self.code), type="item")
        return result


class TCPPacket():

    def __init__(
        self,
        src_ip: IPv4Address,
        dst_ip: IPv4Address,
        src_port: int,
        dst_port: int,
        flags: List[str],
    ):
        self.src_ip = src_ip
        self.dst_ip = dst_ip
        self.src_port = src_port
        self.dst_port = dst_port
        self.flags = flags

    def to_text_extended(self):
        result = ""
        result += format_key(key="TCP", type="title")
        result += format_key_value(key="Src IP", value=str(self.src_ip), type="item")
        result += format_key_value(key="Dst IP", value=str(self.dst_ip), type="item")
        result += format_key_value(key="Src Port", value=self.src_port, type="item")
        result += format_key_value(key="Dst Port", value=self.dst_port, type="item")
        result += format_key_value(key="Type", value=TCPFlags.to_string(self.flags), type="item")
        return result
