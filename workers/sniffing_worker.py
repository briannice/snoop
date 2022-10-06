from lib.sniffing import *
from PyQt5.QtCore import QRunnable, pyqtSlot
from .signals.sniffing_signals import WorkerSignals


class SniffingWorker(QRunnable):

    def __init__(self, interface, *args, **kwargs):
        super(SniffingWorker, self).__init__()
        super().__init__(*args, **kwargs)
        self.interface = interface
        self.signals = WorkerSignals()
        self.running = True

    @pyqtSlot()
    def run(self):
        sniffAllPackets(self.interface, self.handlePacket)

    # WHAT to display
    # Emits signal summary of packet
    @pyqtSlot()
    def handlePacket(self, packet):
        if self.running:
            self.signals.result.emit(packet.summary())
        else:
            # Reset variable
            self.running = True
            # Exit thread
            exit()

    def stopPacket(self):
        self.running = False
