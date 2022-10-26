from lib.sniffing import sniff_packets, format_packet
from PyQt5.QtCore import QRunnable, pyqtSlot
from signals import SniffingSignal


class SniffingWorker(QRunnable):

    def __init__(self, interface: str, protocol: str, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.interface = interface
        self.protocol = protocol
        self.signals = SniffingSignal()
        self.running = True

        # Add stop handler
        self.signals.stop.connect(self.stop)

    @pyqtSlot()
    def run(self):
        match self.protocol:
            case "All":
                sniff_packets(self.interface, self.handle_packet, None)
            case "TCP":
                sniff_packets(self.interface, self.handle_packet, "tcp")
            case "UDP":
                sniff_packets(self.interface, self.handle_packet, "udp")
            case "ICMP":
                sniff_packets(self.interface, self.handle_packet, "icmp")

    def handle_packet(self, packet):
        if self.running:
            result = format_packet(packet)
            self.signals.packet.emit(result)
        else:
            exit()

    def stop(self):
        self.running = False
