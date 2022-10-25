from typing import Dict
from models.results import PortScanConclusion
from widgets.base import BaseGridLayoutWidget, BaseLabelWidget, BaseListWidget, BaseMessageBoxWidget, BasePushButtonWidget, BaseTabWidget
from widgets.custom import CustomCheckBoxGroupWidget, CustomPortScanDialogWidget, CustomTextInputWidget


class PortScanningUi(BaseTabWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Widgets
        self.title = BaseLabelWidget(type="title", text="Port scanning")
        self.info = BaseLabelWidget(type="info")
        self.host = CustomTextInputWidget("Host", "Example: 192.168.56.1")
        self.ports = CustomTextInputWidget("Ports", "Using individual ports: 22,23,80\nUsing ranges: 22-24,80")
        self.packets = CustomCheckBoxGroupWidget("Packets", ["Stealth", "Connect", "Xmas", "FIN", "Null", "ACK"])
        self.output = BaseListWidget()
        self.button_scan = BasePushButtonWidget("Start scan")
        self.button_clear = BasePushButtonWidget("Clear output")

        # Layout
        self.grid = BaseGridLayoutWidget(h_spacing="lg", v_spacing="lg")
        self.grid.addWidget(self.title, 0, 0, 1, 1)
        self.grid.addWidget(self.info, 0, 1, 1, 1)
        self.grid.addLayout(self.host, 1, 0, 1, 2)
        self.grid.addLayout(self.ports, 2, 0, 1, 2)
        self.grid.addWidget(self.packets, 3, 0, 1, 2)
        self.grid.addWidget(self.output, 4, 0, 1, 2)
        self.grid.addWidget(self.button_scan, 5, 0, 1, 1)
        self.grid.addWidget(self.button_clear, 5, 1, 1, 1)
        self.setLayout(self.grid)

    def get_host_input(self) -> str:
        return self.host.get_text()

    def get_ports_input(self) -> str:
        return self.ports.get_text()

    def get_button_scan(self) -> BasePushButtonWidget:
        return self.button_scan

    def get_button_clear(self) -> BasePushButtonWidget:
        return self.button_clear

    def get_packets_checkboxes(self) -> Dict[str, bool]:
        return self.packets.get_checkbox_values()

    def get_output(self):
        return self.output

    def set_loading(self):
        self.info.set_info()
        self.info.setText("Loading...")

    def set_success(self):
        self.info.set_success()
        self.info.setText("Scanning done!")

    def set_error(self, error: str):
        self.info.set_error()
        self.info.setText(error)

    def set_host_error(self, error: str):
        self.host.set_error(error)

    def set_ports_error(self, error: str):
        self.ports.set_error(error)

    def set_packets_error(self, error: str):
        self.packets.set_error(error)

    def clear_host_error(self):
        self.host.remove_error()

    def clear_ports_error(self):
        self.ports.remove_error()

    def clear_packets_error(self):
        self.packets.remove_error()

    def clear_errors(self):
        self.clear_host_error()
        self.clear_ports_error()
        self.clear_packets_error()

    def clear_output(self):
        self.output.clear()

    def add_output_item(self, port_scan_conclusion: PortScanConclusion):
        text = port_scan_conclusion.to_text_short()
        self.output.addItem(text)

    def set_message_box(self, port_scan_conclusion: PortScanConclusion):
        dialog = CustomPortScanDialogWidget(port_scan_conclusion)
        dialog.exec()
