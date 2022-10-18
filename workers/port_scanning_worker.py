from PyQt5.QtCore import QRunnable, pyqtSlot

from signals import PortScanningSignal


class PortScanningWorker(QRunnable):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.signals = PortScanningSignal()

    @pyqtSlot()
    def run(self):
        pass
