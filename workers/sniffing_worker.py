# Standard lib
from lib.sniffing import *
from PyQt5.QtCore import QRunnable, pyqtSlot

from lib.scanning import ping_scan, PingScanResult
from .worker_signals import WorkerSignals


class SniffingWorker(QRunnable):

    def __init__(self, interface, *args, **kwargs):
        super(SniffingWorker, self).__init__()
        super().__init__(*args, **kwargs)
        self.interface = interface
        self.signals = WorkerSignals()

    @pyqtSlot()
    def run(self):
        sniffAllPackets(self.interface, self.handlePacket)

    def handlePacket(self, packet):
        self.signals.result.emit(packet.summary())
