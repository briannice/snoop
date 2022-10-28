from concurrent.futures import ThreadPoolExecutor, wait
from ipaddress import IPv4Address, IPv4Network
from time import sleep
from typing import Dict, List

from PyQt5.QtCore import QRunnable, pyqtSlot

from lib.scanning import network_scan
from models.enums import HostScanMethod
from models.results import HostScanResult, HostScanConclusion
from signals import NetworkScanningSignal


class NetworkScanningWorker(QRunnable):

    def __init__(self, network: IPv4Network, protocols: Dict[str, bool], * args, **kwargs):
        super().__init__(*args, **kwargs)

        self.signals = NetworkScanningSignal()

        self.network = network
        self.protocols = HostScanMethod.dict_to_list(protocols)

    @pyqtSlot()
    def run(self):
        with ThreadPoolExecutor(100) as executor:
            result: List[HostScanResult] = []
            futures = []
            for host in self.network.hosts():
                for protocol in self.protocols:
                    sleep(0.1)
                    futures.append(executor.submit(
                        self.task,
                        host,
                        protocol,
                        result
                    ))
            wait(futures)
            rdicts = {}
            for r in result:
                if r.ip in rdicts.keys():
                    rdicts[r.ip].append(r)
                else:
                    rdicts[r.ip] = [r, ]
            data = [HostScanConclusion(k, v) for k, v in rdicts.items()]
            self.signals.data.emit(data)

    @staticmethod
    def task(host: IPv4Address, protocol: HostScanMethod, result: List[HostScanResult]):
        r = network_scan(host, protocol)
        result.append(r)
