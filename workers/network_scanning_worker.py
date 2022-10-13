from concurrent.futures import ThreadPoolExecutor, wait
from ipaddress import IPv4Address, IPv4Network
from typing import List

from PyQt5.QtCore import QRunnable, pyqtSlot

from lib.scanning import HostScanResult, ping_scan
from signals import NetworkScanningSignal


class NetworkScanningWorker(QRunnable):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.signals = NetworkScanningSignal()

    @pyqtSlot()
    def run(self):
        with ThreadPoolExecutor(100) as executor:
            network = IPv4Network("192.168.56.0/24")
            result = []
            print("Network scanning")
            futures = [executor.submit(self.task, host, result) for host in network.hosts()]
            wait(futures)
            print("Scanning done!")
            self.signals.data.emit(result)

    @staticmethod
    def task(host: IPv4Address, result: List[HostScanResult]):
        r = ping_scan(host)
        result.append(r)
