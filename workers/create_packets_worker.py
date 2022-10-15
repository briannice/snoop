from lib.custom_packets import SendUDP, SendTCP, SendICMP
from PyQt5.QtCore import QRunnable, pyqtSlot
from signals import CreatePacketSignal


class CreatePacketsWorker(QRunnable):

    def __init__(self, *args, **kwargs):
        super(CreatePacketsWorker, self).__init__()
        super().__init__(*args, **kwargs)
        self.signals = CreatePacketSignal()

    @pyqtSlot()
    def SendICMP_worker(self, source, destination, interface, count=1, message="Hello World"):
        SendICMP(source=source, destination=destination, interface=interface, message=message, count=count)

    @pyqtSlot()
    def SendTCP_worker(self, source, destination, dstport, srcport, interface, count=1):
        SendTCP(source=source, destination=destination, interface=interface, count=count, dstport=dstport,
                srcport=srcport)

    @pyqtSlot()
    def SendUDP_worker(self, source, destination, dstport, srcport, interface, count=1):
        SendUDP(source=source, destination=destination, interface=interface, count=count, dstport=dstport,
                srcport=srcport)
