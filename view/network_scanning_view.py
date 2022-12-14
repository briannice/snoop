from ipaddress import IPv4Network
from typing import List

from PyQt5.QtCore import QThreadPool

from models.results import HostScanConclusion
from ui import NetworkScanningUi
from utils.validators import ipv4_network_validator
from workers import NetworkScanningWorker


class NetworkScanningView(NetworkScanningUi):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Setup
        self.thread_pool = QThreadPool.globalInstance()

        # Data
        self.results: List[HostScanConclusion] = []
        self.is_scanning: bool = False

        # Handlers
        self.get_button_scan().clicked.connect(self.handler_button_scan)
        self.get_button_clear().clicked.connect(self.handler_button_clear)
        self.get_output().clicked.connect(self.handler_message_box)

    # ------------- #
    #    HANDLERS   #
    # ------------- #

    def handler_button_scan(self):
        if self.is_scanning:
            return
        if not self.validate():
            return

        self.is_scanning = True
        self.results = []
        self.clear_output()
        self.set_loading()

        network = IPv4Network(self.get_network_input())
        protocols = self.get_protocols_checkboxes()

        worker = NetworkScanningWorker(network, protocols)
        worker.signals.data.connect(self.handler_signals_data)
        self.thread_pool.start(worker)

    def handler_button_clear(self):
        self.results = []
        self.clear_output()
        self.clear_errors()

    def handler_signals_data(self, data: List[HostScanConclusion]):
        self.is_scanning = False
        self.results = data
        self.set_success()
        self.update_output_list()

    def handler_message_box(self, item):
        important_results = [r for r in self.results if r.is_important()]
        row = item.row()
        port_scan_conclusion = important_results[row]
        self.set_message_box(port_scan_conclusion)

    # ---------- #
    #    VIEW    #
    # ---------- #

    def update_output_list(self):
        important_count = 0
        for r in self.results:
            if r.is_important():
                self.add_output_item(r)
                important_count += 1
        if important_count == 0:
            self.set_error("No hosts were found...")

    # --------------- #
    #    VALIDATORS   #
    # --------------- #

    def validate(self) -> bool:
        v1 = self.validate_network_input()
        v2 = self.validate_protocols()
        return v1 and v2

    def validate_network_input(self) -> bool:
        network = self.get_network_input()
        error = ipv4_network_validator(network)
        if error is None:
            self.clear_network_error()
            return True
        self.set_network_error(error)
        return False

    def validate_protocols(self) -> bool:
        for _, value in self.get_protocols_checkboxes().items():
            if value:
                self.clear_protocols_error()
                return True
        self.set_protocols_error("At least one protocol should be checked")
        return False

    # ------------ #
    #    HELPERS   #
    # ------------ #
