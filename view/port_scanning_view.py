from ipaddress import IPv4Address
from typing import List

from PyQt5.QtCore import QThreadPool

from lib.scanning import PortScanConclusion
from ui import PortScanningUi
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

    # ------------- #
    #    HANDLERS   #
    # ------------- #

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
        chars = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "-", ","]
        max = 65535
        min = 1

        text = self.SelectPortTextInput.text()

        if text == "":
            self.SelectPortError.setText("Ports can not be empty")
            self.SelectHostLayout.addWidget(self.SelectPortError, 3, 0, 1, 2)
            return False

        for c in text:
            if c not in chars:
                self.SelectPortError.setText("Ports can only contain numbers, '-' and ','")
                self.SelectHostLayout.addWidget(self.SelectPortError, 3, 0, 1, 2)
                return False

        for t in text.split(","):
            if t == "":
                self.SelectPortError.setText("Port range can not be empty")
                self.SelectHostLayout.addWidget(self.SelectPortError, 3, 0, 1, 2)
                return False

            if "," in t:
                self.SelectPortError.setText("Port range can not contain ','")
                self.SelectHostLayout.addWidget(self.SelectPortError, 3, 0, 1, 2)
                return False

            count = t.count("-")
            if count == 0:
                p = int(t)
                if p < min or p > max:
                    self.SelectPortError.setText("Port range can not contain ','")
                    self.SelectHostLayout.addWidget(self.SelectPortError, 3, 0, 1, 2)
                    return False
            elif count == 1:
                ps = t.split("-")
                for p in ps:
                    p = int(p)
                    if p < min or p > max:
                        self.SelectPortError.setText("Port range can not contain ','")
                        self.SelectHostLayout.addWidget(self.SelectPortError, 3, 0, 1, 2)
                        return False
            else:
                self.SelectPortError.setText("Port range can only contain one '-'")
                self.SelectHostLayout.addWidget(self.SelectPortError, 3, 0, 1, 2)
                return False

        self.SelectPortError.setText("")
        self.SelectHostLayout.removeWidget(self.SelectPortError)
        return True

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
