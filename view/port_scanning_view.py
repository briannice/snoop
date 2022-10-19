from ipaddress import IPv4Address
import re

from PyQt5.QtCore import QThreadPool

from ui import PortScanningUi


class PortScanningView(PortScanningUi):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Setup
        self.thread_pool = QThreadPool()

        # Data
        self.port_scan_results = []

        # Handlers
        self.ButtonScan.clicked.connect(self.handler_scan_button)

    # ------------- #
    #    HANDLERS   #
    # ------------- #

    def handler_scan_button(self):
        self.validate()

    # ---------------- #
    #    VALIDATION    #
    # ---------------- #

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

    def validate_select_packets(self):
        for cb in self.get_packet_checkboxes():
            if cb.isChecked():
                self.SelectPacketsError.setText("")
                self.SelectPacketsLayout.removeWidget(self.SelectPacketsError)
                return True
        self.SelectPacketsError.setText("At least one packet should be checked")
        self.SelectPacketsLayout.addWidget(self.SelectPacketsError, 2, 0, 1, 4)
        return False
