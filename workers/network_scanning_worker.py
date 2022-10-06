from ipaddress import IPv4Address, IPv4Network
from multiprocessing import Manager, Process, Pool
from typing import List

from PyQt5.QtCore import QRunnable, pyqtSlot

from lib.scanning import ping_scan, PingScanResult
from .worker_signals import WorkerSignals


class NetworkScanningWorker(QRunnable):
    """
    Worker to perform a network scan in a separate thread.


    Attributes
    ==========

    * network (IPv4Network): network on which the scan should be performed.

    * signals (WorkerSignals): signals to communicate with main thread.

    """

    def __init__(
        self,
        network: IPv4Network = IPv4Network("192.168.1.0/24")
    ):
        super().__init__()
        self.network = network
        self.signals = WorkerSignals()

    @pyqtSlot()
    def run(self):
        """
        Perform a ping scan on each possible host in the network using
        multiprocessing.
        """

        pool = Pool(processes=100)
        manager = Manager()
        result = manager.list()
        tasks = []
        hosts = self.network.hosts()

        for host in hosts:
            # task = Process(
            #     target=NetworkScanningWorker.run_task,
            #     args=(host, result)
            # )
            # tasks.append(task)
            pool.apply_async(NetworkScanningWorker.run_task,
                             args=(host, result))
            # task.start()

        # for task in tasks:
        #     task.join()

        pool.close()
        pool.join()

        self.signals.progress.emit(100)
        self.signals.finished.emit(True)
        self.signals.result.emit(result)

    @staticmethod
    def run_task(host: IPv4Address, result: List[PingScanResult]):
        ping_scan_result = ping_scan(host)
        result.append(ping_scan_result)
        del ping_scan_result
