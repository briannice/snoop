from typing import Dict
from models.results import HostScanConclusion
from widgets.base import BaseGridLayoutWidget, BaseLabelWidget, BaseListWidget, BaseMessageBoxWidget, BasePushButtonWidget, BaseTabWidget
from widgets.custom import CustomCheckBoxGroupWidget, CustomContentDialogWidget, CustomTextInputWidget


class NetworkScanningUi(BaseTabWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Widgets
        self.title = BaseLabelWidget(type="title", text="Network scanning")
        self.info = BaseLabelWidget(type="info", align="r")
        self.network = CustomTextInputWidget("Network", "Example: 192.168.56.0/24")
        self.protocols = CustomCheckBoxGroupWidget("Protocols", ["Ping", "SSH", "HTTP", "HTTPS"])
        self.output = BaseListWidget()
        self.button_scan = BasePushButtonWidget("Start scan")
        self.button_clear = BasePushButtonWidget("Clear output")

        # Layout
        self.grid = BaseGridLayoutWidget(h_spacing="lg", v_spacing="lg")
        self.grid.addWidget(self.title, 0, 0, 1, 1)
        self.grid.addWidget(self.info, 0, 1, 1, 1)
        self.grid.addLayout(self.network, 1, 0, 1, 2)
        self.grid.addWidget(self.protocols, 2, 0, 1, 2)
        self.grid.addWidget(self.output, 4, 0, 1, 2)
        self.grid.addWidget(self.button_scan, 5, 0, 1, 1)
        self.grid.addWidget(self.button_clear, 5, 1, 1, 1)
        self.setLayout(self.grid)

    def get_network_input(self) -> str:
        return self.network.get_text()

    def get_button_scan(self) -> BasePushButtonWidget:
        return self.button_scan

    def get_button_clear(self) -> BasePushButtonWidget:
        return self.button_clear

    def get_protocols_checkboxes(self) -> Dict[str, bool]:
        return self.protocols.get_checkbox_values()

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

    def set_network_error(self, error: str):
        self.network.set_error(error)

    def set_protocols_error(self, error: str):
        self.protocols.set_error(error)

    def clear_network_error(self):
        self.network.remove_error()

    def clear_protocols_error(self):
        self.protocols.remove_error()

    def clear_errors(self):
        self.clear_network_error()
        self.clear_protocols_error()

    def clear_output(self):
        self.output.clear()

    def add_output_item(self, host_scan_conclusion: HostScanConclusion):
        text = host_scan_conclusion.to_text_short()
        self.output.addItem(text)

    def set_message_box(self, port_scan_conclusion: HostScanConclusion):
        host = port_scan_conclusion.host
        state = port_scan_conclusion.state

        title = f"Network scan {host}: {state}"
        content = port_scan_conclusion.to_text_extended()
        dialog = CustomContentDialogWidget(title, content)
        dialog.exec()
