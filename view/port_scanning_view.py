from ipaddress import IPv4Address
from typing import List

from PyQt5.QtCore import QThreadPool

from lib.scanning import PortScanConclusion
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
        self.ButtonScan.clicked.connect(self.handler_scan_button)
        self.ButtonClear.clicked.connect(self.handler_clear_button)

    # ------------- #
    #    HANDLERS   #
    # ------------- #

    def handler_scan_button(self):
        # Dont scan if already scanning
        if self.is_scanning:
            return
        self.is_scanning = True

        # Validation
        if not self.validate():
            return

        # Clear current output
        self.OutputList.clear()

        # Start scanning info
        self.ScanningInfoLabel.setText("Scanning...")
        self.ScanningInfoLabel.setType("info")

        # Get data
        ip = self.SelectHostTextInput.text()
        ports = self.get_selected_ports()
        packets = self.get_packet_checkbox_statuses()

        # Start worker
        worker = PortScanningWorker(ip, ports, packets)
        worker.signals.data.connect(self.handler_signals_data)
        self.thread_pool.start(worker)

    def handler_clear_button(self):
        self.results = []
        self.OutputList.clear()

    def handler_signals_data(self, data: List[PortScanConclusion]):
        self.ScanningInfoLabel.setText("Scanning done!")
        self.ScanningInfoLabel.setType("success")
        self.is_scanning = False
        self.results = data
        self.update_output_list()

    # ---------- #
    #    VIEW    #
    # ---------- #

    def update_output_list(self):
        for r in self.results:
            if r.is_important():
                self.OutputList.addItem(str(r))

    # --------------- #
    #    VALIDATORS   #
    # --------------- #

    def validate(self) -> bool:
        v1 = self.validate_select_host_text_input()
        v2 = self.validate_select_port_text_input()
        v3 = self.validate_select_packets()
        return v1 and v2 and v3

    def validate_select_host_text_input(self) -> bool:
        ip = self.SelectHostTextInput.text()
        try:
            IPv4Address(ip)
            self.SelectHostError.setText("")
            self.SelectHostLayout.removeWidget(self.SelectHostError)
            return True
        except Exception as e:
            self.SelectHostError.setText(str(e).replace("Address", "Host"))
            self.SelectHostLayout.addWidget(self.SelectHostError, 1, 0, 1, 2)
            return False

    def validate_select_port_text_input(self) -> bool:
        text = self.SelectPortTextInput.text()
        error = port_input_validator(text)

        if error is None:
            self.SelectPortError.setText("")
            self.SelectHostLayout.removeWidget(self.SelectPortError)
        else:
            self.SelectPortError.setText(error)
            self.SelectHostLayout.addWidget(self.SelectPortError, 3, 0, 1, 2)

    def validate_select_packets(self) -> bool:
        for cb in self.get_packet_checkboxes():
            if cb.isChecked():
                self.SelectPacketsError.setText("")
                self.SelectPacketsLayout.removeWidget(self.SelectPacketsError)
                return True
        self.SelectPacketsError.setText("At least one packet should be checked")
        self.SelectPacketsLayout.addWidget(self.SelectPacketsError, 2, 0, 1, 4)
        return False

    # ------------ #
    #    HELPERS   #
    # ------------ #

    def get_selected_ports(self) -> List[int]:
        result = []
        text = self.SelectPortTextInput.text()
        for t in text.split(","):
            if "-" in t:
                min = int(t.split("-")[0])
                max = int(t.split("-")[1])
                result.extend(range(min, max + 1))
            else:
                result.append(int(t))
        return result
