from concurrent.futures import ThreadPoolExecutor, wait

from PyQt5.QtCore import QRunnable, pyqtSlot

from lib.scanning import port_scan
from signals import PortScanningSignal


class PortScanningWorker(QRunnable):

    def __init__(self, ip, ports, packets, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.signals = PortScanningSignal()

        self.ip = ip
        self.ports = ports
        self.scan_methods = []

    @pyqtSlot()
    def run(self):
        with ThreadPoolExecutor(100) as executor:
            result = {}
            for port in self.ports:
                port_result = []
                futures = [
                    executor.submit(
                        self.task,
                        self.ip,
                        port,
                        scan_method,
                        result
                    ) for scan_method in self.scan_methods
                ]
                wait(futures)
                result[port] = port_result
            self.signals.data.emit(result)

    @staticmethod
    def task(host, port, scan_method, result):
        port_scan_result = port_scan(host, port, scan_method)
        result.append(port_scan_result)
