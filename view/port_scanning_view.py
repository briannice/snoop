from ipaddress import IPv4Address
from typing import List

from PyQt5.QtCore import QThreadPool

from models.results import PortScanConclusion
from ui import PortScanningUi
from utils import port_input_validator
from workers import PortScanningWorker


class PortScanningView(PortScanningUi):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Setup
        self.thread_pool = QThreadPool()

        # Data
        self.results: List[PortScanConclusion] = []
        self.is_scanning: bool = False

        # Handlers
        self.get_button_scan().clicked.connect(self.handler_scan_button)
        self.get_button_clear().clicked.connect(self.handler_clear_button)
        self.get_output().clicked.connect(self.handler_message_box)

    # ------------- #
    #    HANDLERS   #
    # ------------- #

    def handler_scan_button(self):
        if self.is_scanning:
            return
        if not self.validate():
            return

        self.is_scanning = True
        self.results = []
        self.clear_output()
        self.set_loading()

        ip = self.get_host_input()
        ports = self.get_selected_ports()
        packets = self.get_packets_checkboxes()

        # Start worker
        worker = PortScanningWorker(ip, ports, packets)
        worker.signals.data.connect(self.handler_signals_data)
        self.thread_pool.start(worker)

    def handler_clear_button(self):
        self.results = []
        self.clear_output()
        self.clear_errors()

    def handler_signals_data(self, data: List[PortScanConclusion]):
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
        for r in self.results:
            if r.is_important():
                self.add_output_item(r)

    # --------------- #
    #    VALIDATORS   #
    # --------------- #

    def validate(self) -> bool:
        v1 = self.validate_host_input()
        v2 = self.validate_ports_input()
        v3 = self.validate_packets()
        return v1 and v2 and v3

    def validate_host_input(self) -> bool:
        ip = self.get_host_input()
        try:
            IPv4Address(ip)
            self.clear_host_error()
            return True
        except Exception as e:
            error = str(e).replace("Address", "Host")
            self.set_host_error(error)
            return False

    def validate_ports_input(self) -> bool:
        ports = self.get_ports_input()
        error = port_input_validator(ports)

        if error is None:
            self.clear_ports_error()
            return True
        else:
            self.set_ports_error(error)
            return False

    def validate_packets(self) -> bool:
        for _, value in self.get_packets_checkboxes().items():
            if value:
                self.clear_packets_error()
                return True
        self.set_packets_error("At least one packet should be checked")
        return False

    # ------------ #
    #    HELPERS   #
    # ------------ #

    def get_selected_ports(self) -> List[int]:
        result = []
        text = self.get_ports_input()
        for t in text.split(","):
            if "-" in t:
                min = int(t.split("-")[0])
                max = int(t.split("-")[1])
                result.extend(range(min, max + 1))
            else:
                result.append(int(t))
        return result
