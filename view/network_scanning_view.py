from PyQt5.QtCore import QThreadPool

from ui import NetworkScanningUi
from worker import NetworkScanningWorker


class NetworkScanningView(NetworkScanningUi):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Setup
        self.thread_pool = QThreadPool()

        # Data

        # Handlers
        self.ButtonScan.clicked.connect(self.__button_scan_handler)

    def __button_scan_handler(self):
        worker = NetworkScanningWorker()
        self.thread_pool.start(worker)
