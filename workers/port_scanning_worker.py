from concurrent.futures import ThreadPoolExecutor, wait
import logging

from PyQt5.QtCore import QRunnable, pyqtSlot

from lib.scanning import port_scan, PortScanMethod
from signals import PortScanningSignal


class PortScanningWorker(QRunnable):

    def __init__(self, ip, ports, packets, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.signals = PortScanningSignal()

        self.ip = ip
        self.ports = ports
        self.scan_methods = PortScanMethod.dict_to_list(packets)

    @pyqtSlot()
    def run(self):
        logging.basicConfig(level=logging.DEBUG)
        with ThreadPoolExecutor(100) as executor:
            result = {}
            futures = []
            for port in self.ports:
                for scan_method in self.scan_methods:
                    futures.append(executor.submit(
                        self.task,
                        self.ip,
                        port,
                        scan_method,
                        result
                    ))
            wait(futures)
            self.signals.data.emit(result)

    @staticmethod
    def task(host, port, scan_method, result):
        r = port_scan(host, port, scan_method)
        if str(port) in result.keys():
            result[port].append(r)
        else:
            result[port] = [r]
