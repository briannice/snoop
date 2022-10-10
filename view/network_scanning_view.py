from typing import List
from PyQt5.QtCore import QThreadPool

from lib.scanning import HostScanResult
from ui import NetworkScanningUi
from workers import NetworkScanningWorker


class NetworkScanningView(NetworkScanningUi):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Setup
        self.thread_pool = QThreadPool()

        # Data
        self.host_scan_results: List[HostScanResult] = []

        # Handlers
        self.ButtonScan.clicked.connect(self.handler_button_scan)
        self.ButtonClear.clicked.connect(self.handler_button_clear)
        self.FilterUpCheckbox.clicked.connect(self.update_output_text)
        self.FilterUnknownCheckbox.clicked.connect(self.update_output_text)
        self.FilterBlockedCheckbox.clicked.connect(self.update_output_text)

    def handler_button_scan(self):
        worker = NetworkScanningWorker()
        worker.signals.data.connect(self.handler_scan_data)
        self.thread_pool.start(worker)

    def handler_button_clear(self):
        self.OutputText.clear()

    def handler_scan_data(self, data):
        self.host_scan_results = data
        self.update_output_text()

    def update_output_text(self):
        self.OutputText.clear()

        for hsr in self.host_scan_results:
            if hsr.is_up() and self.FilterUpCheckbox.isChecked():
                self.OutputText.append(str(hsr))
            if hsr.is_unknown() and self.FilterUnknownCheckbox.isChecked():
                self.OutputText.append(str(hsr))
            if hsr.is_blocked() and self.FilterBlockedCheckbox.isChecked():
                self.OutputText.append(str(hsr))
