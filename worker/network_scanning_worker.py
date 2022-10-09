from concurrent.futures import ThreadPoolExecutor
from ipaddress import IPv4Address, IPv4Network
from typing import List

from PyQt5.QtCore import QRunnable, pyqtSlot

from lib.scanning import HostScanResult, ping_scan
from signal import NetworkScanningSignal


class NetworkScanningWorker(QRunnable):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.signals = NetworkScanningSignal()

    @pyqtSlot()
    def run(self):
        network = IPv4Network("192.168.1.0/24")
        result = []
        executor = ThreadPoolExecutor(max_workers=20)

        for host in network.hosts():
            executor.submit(self.task, host, result)

        print(result)

    @staticmethod
    def task(host: IPv4Address, result: List[HostScanResult]):
        r = ping_scan(host)
        result.append(r)
