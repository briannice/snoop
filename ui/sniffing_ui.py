from typing import List
from widgets.base import BaseGridLayoutWidget, BaseLabelWidget, BaseListWidget, BaseRadioButtonWidget, BasePushButtonWidget, BaseTabWidget
from widgets.custom import CustomComboBoxWidget, CustomRadioButtonGroupWidget, CustomContentDialogWidget


class SniffingUI(BaseTabWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Widgets
        self.title = BaseLabelWidget(type="title", text="Sniffing")
        self.info = BaseLabelWidget(type="info", align="r")
        self.interface = CustomComboBoxWidget("Interface", "Interace on which you want to sniff packets")
        self.protocols = CustomRadioButtonGroupWidget("Protocols", ["TCP", "UDP", "ICMP", "All"])
        self.output = BaseListWidget()
        self.button_sniff = BasePushButtonWidget("Start sniffing")
        self.button_stop = BasePushButtonWidget("Stop sniffing")
        self.button_clear = BasePushButtonWidget("Clear output")

        # Layout
        self.grid = BaseGridLayoutWidget(h_spacing="lg", v_spacing="lg")
        self.grid.addWidget(self.title, 0, 0, 1, 3)
        self.grid.addWidget(self.info, 0, 3, 1, 3)
        self.grid.addLayout(self.interface, 1, 0, 1, 6)
        self.grid.addWidget(self.protocols, 2, 0, 1, 6)
        self.grid.addWidget(self.output, 3, 0, 1, 6)
        self.grid.addWidget(self.button_sniff, 4, 0, 1, 2)
        self.grid.addWidget(self.button_stop, 4, 2, 1, 2)
        self.grid.addWidget(self.button_clear, 4, 4, 1, 2)
        self.setLayout(self.grid)

    def get_interface(self) -> str:
        return self.interface.get_text()

    def get_protocol(self) -> str:
        return self.protocols.get_value()

    def get_protocol_buttons(self) -> List[BaseRadioButtonWidget]:
        return self.protocols.get_radio_buttons()

    def get_output(self):
        return self.output

    def get_button_sniff(self) -> BasePushButtonWidget:
        return self.button_sniff

    def get_button_stop(self) -> BasePushButtonWidget:
        return self.button_stop

    def get_button_clear(self) -> BasePushButtonWidget:
        return self.button_clear

    def add_interface(self, interface: str):
        self.interface.add_item(interface)

    def add_packet(self, packet):
        text = packet.to_text_short()
        self.output.addItem(text)
        self.output.scrollToBottom()

    def set_count(self, count):
        self.info.set_info()
        self.info.setText(f"Count: {count}")

    def set_stop(self):
        self.info.set_error()
        self.info.setText("Stopped sniffing")

    def clear_output(self):
        self.output.clear()

    def set_message_box(self, packet):
        title = "Packet view"
        content = packet.to_text_extended()
        dialog = CustomContentDialogWidget(title, content)
        dialog.exec()
