from lib.sniffing import *
from PyQt5.QtCore import QRunnable, pyqtSlot
from signals import SniffingSignal


class SniffingWorker(QRunnable):

    def __init__(self, interface, protocol, *args, **kwargs):
        super(SniffingWorker, self).__init__()
        super().__init__(*args, **kwargs)
        self.interface = interface
        self.protocol = protocol
        self.signals = SniffingSignal()
        self.running = True

    @pyqtSlot()
    def run(self):
        match self.protocol:
            # Both
            case 0:
                print("Both (worker)")
                sniffAllPackets(self.interface, self.handlePacket)
            # TCP
            case 1:
                print("TCP (worker)")
                sniff_only_tcp_packets(self.interface, self.handlePacket)
            # UDP
            case 2:
                print("UDP (worker)")
                sniff_only_udp_packets(self.interface, self.handlePacket)

    # WHAT to display
    # Emits signal summary of packet
    @pyqtSlot()
    def handlePacket(self, packet):
        if self.running:
            if check_icmp(packet):
                icmp_message = get_icmp_message(packet)
                self.signals.result.emit("{} : {}".format(packet.summary(), icmp_message))
            else:
                self.signals.result.emit(packet.summary())
        else:
            # Reset variable
            self.running = True
            # Exit thread
            exit()

    def stopPacket(self):
        self.running = False
