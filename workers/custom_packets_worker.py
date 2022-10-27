from lib.custom_packets import send_udp, send_icmp, send_tcp
from PyQt5.QtCore import QRunnable, pyqtSlot
from signals import CustomPacketSignal
from utils import SnoopException


class CustomPacketsWorker(QRunnable):

    def __init__(
        self,
        protocol: str,
        interface: str,
        source_ip: str,
        dest_ip: str,
        payload: str,
        source_port: int | None,
        dest_port: int | None,
        icmp_type: int | None,
        icmp_code: int | None,
        * args,
        **kwargs
    ):
        super().__init__(*args, **kwargs)

        self.protocol = protocol
        self.interface = interface
        self.source_ip = source_ip
        self.dest_ip = dest_ip
        self.payload = payload
        self.source_port = source_port
        self.dest_port = dest_port
        self.icmp_type = icmp_type
        self.icmp_code = icmp_code

        self.signals = CustomPacketSignal()

    @pyqtSlot()
    def run(self):
        result = None
        match self.protocol:
            case "TCP":
                result = send_tcp(
                    interface=self.interface,
                    source=self.source_ip,
                    destination=self.dest_ip,
                    sport=self.source_port,
                    dport=self.dest_port,
                    payload=self.payload
                )
            case "UDP":
                result = send_udp(
                    interface=self.interface,
                    source=self.source_ip,
                    destination=self.dest_ip,
                    sport=self.source_port,
                    dport=self.dest_port,
                    payload=self.payload
                )
            case "ICMP":
                result = send_icmp(
                    interface=self.interface,
                    source=self.source_ip,
                    destination=self.dest_ip,
                    type=self.icmp_type,
                    code=self.icmp_code,
                    payload=self.payload
                )
            case _:
                raise SnoopException("Invalid custom packet protocol")
        self.signals.packet.emit(result)
