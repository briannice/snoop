from widgets.base import BaseGridLayoutWidget, BaseLabelWidget, BasePushButtonWidget, BaseTabWidget
from widgets.custom import CustomRadioButtonGroupWidget, CustomComboBoxWidget, CustomTextareaInputWidget, CustomStringIntInputWidget, CustomContentDialogWidget


class CustomPacketsUI(BaseTabWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.show_port = True

        # Widgets
        self.title = BaseLabelWidget(type="title", text="Custom packets")
        self.info = BaseLabelWidget(type="info", align="r")
        self.interface = CustomComboBoxWidget("Interface", "Interace on which you want to send packets")
        self.protocols = CustomRadioButtonGroupWidget("Protocols", ["TCP", "UDP", "ICMP"])
        self.source = CustomStringIntInputWidget("Source IP", "Source port")
        self.destination = CustomStringIntInputWidget("Destination IP", "Destination port")
        self.payload = CustomTextareaInputWidget("Payload", "")
        self.button_send = BasePushButtonWidget("Send packet")
        self.button_view = BasePushButtonWidget("View response")

        # Layout
        self.grid = BaseGridLayoutWidget(h_spacing="lg", v_spacing="lg")
        self.grid.addWidget(self.title, 0, 0, 1, 1)
        self.grid.addWidget(self.info, 0, 1, 1, 1)
        self.grid.addLayout(self.interface, 1, 0, 1, 2)
        self.grid.addWidget(self.protocols, 2, 0, 1, 2)
        self.grid.addLayout(self.source, 3, 0, 1, 2)
        self.grid.addLayout(self.destination, 4, 0, 1, 2)
        self.grid.addLayout(self.payload, 5, 0, 1, 2)
        self.grid.addWidget(self.button_send, 6, 0, 1, 1)
        self.grid.addWidget(self.button_view, 6, 1, 1, 1)
        self.setLayout(self.grid)

    def get_interface(self) -> str:
        return self.interface.get_text()

    def get_protocol(self) -> str:
        return self.protocols.get_value()

    def get_protocol_buttons(self):
        return self.protocols.get_radio_buttons()

    def get_source_address(self) -> str:
        return self.source.get_str()

    def get_source_port(self) -> str | None:
        if self.show_port:
            return self.source.get_int()
        return None

    def get_destination_address(self) -> str:
        return self.destination.get_str()

    def get_destination_port(self) -> str:
        if self.show_port:
            return self.destination.get_int()
        return None

    def get_icmp_type(self) -> str:
        if not self.show_port:
            return self.source.get_int()
        return None

    def get_icmp_code(self) -> str:
        if not self.show_port:
            return self.destination.get_int()
        return None

    def get_payload(self) -> str:
        return self.payload.get_text()

    def get_button_send(self) -> BasePushButtonWidget:
        return self.button_send

    def get_button_view(self) -> BasePushButtonWidget:
        return self.button_view

    def add_interface(self, interface: str):
        self.interface.add_item(interface)

    def set_waiting(self):
        self.info.set_info()
        self.info.setText("Waiting for response...")

    def set_no_response(self):
        self.info.set_error()
        self.info.setText("No response")

    def set_received_response(self):
        self.info.set_success()
        self.info.setText("Response received")

    def set_source_error(self, error: str):
        self.source.set_error(error)

    def set_destination_error(self, error: str):
        self.destination.set_error(error)

    def clear_source_error(self):
        self.source.remove_error()

    def clear_destination_error(self):
        self.destination.remove_error()

    def clear_errors(self):
        self.clear_source_error()
        self.clear_destination_error()

    def update_protocol(self, protocol):
        if protocol in ["ICMP"]:
            self.show_port = False
            self.source.set_label_int("ICMP Type")
            self.destination.set_label_int("ICMP Code")
        elif protocol in ["TCP", "UDP"]:
            self.show_port = True
            self.source.set_label_int("Source Port")
            self.destination.set_label_int("Destination Port")

    def set_message_box(self, packet):
        title = "Packet view"
        content = packet.to_text_extended()
        dialog = CustomContentDialogWidget(title, content)
        dialog.exec()

        # # Set text
        # self.label_title.setText("Create and send your own custom packets")
        # self.label_choose_interface.setText("Choose your interface: ")
        # self.radioButton_icmp.setText("ICMP")
        # self.label_choose_protocol.setText("Choose your desired protocol: ")
        # self.radioButton_tcp.setText("TCP")
        # self.radioButton_udp.setText("UDP")
        # self.label_source_address.setText("Source address:")
        # self.label_choose_destination_address.setText("Destination address:")
        # self.label_port_source.setText("Port")
        # self.label_port_destination.setText("Port")
        # self.label_custom_message.setText("Custom Message (ICMP only)")
        # self.label_icmp_note.setText(
        #     "Important note: ICMP has no concept of ports, as TCP and UDP do, but instead uses types and codes.")
        # self.label_count.setText("How much packets to send:")
        # self.pushButton_send_packets.setText("Send packets!")

        # # Default values
        # self.input_source_address.setText("127.0.0.1")
        # self.input_destination_address.setText("127.0.0.1")
        # self.input_icmp_message.setPlainText("Hello world!")
        # self.radioButton_icmp.setChecked(True)
