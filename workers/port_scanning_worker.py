from concurrent.futures import ThreadPoolExecutor, wait
from typing import List

from PyQt5.QtCore import QRunnable, pyqtSlot

from lib.scanning import port_scan, PortScanMethod, PortScanResult, PortScanConclusion
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
        with ThreadPoolExecutor(100) as executor:
            result: List[PortScanResult] = []
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
            rdicts = {}
            for r in result:
                if r.port in rdicts.keys():
                    rdicts[r.port].append(r)
                else:
                    rdicts[r.port] = [r, ]
            data = [PortScanConclusion(k, v) for k, v in rdicts.items()]
            self.signals.data.emit(data)

    @staticmethod
    def task(host, port, scan_method, result):
        r = port_scan(host, port, scan_method)
        result.append(r)
