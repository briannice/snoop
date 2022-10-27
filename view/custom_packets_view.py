from ipaddress import IPv4Address
from ui import CustomPacketsUI
from lib.sniffing import get_interfaces
from workers import CustomPacketsWorker
from PyQt5.QtCore import QThreadPool


class CustomPacketsView(CustomPacketsUI):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Thread pool
        self.thread_pool = QThreadPool.globalInstance()

        # Data
        self.response = None
        self.is_sending: bool = False

        # Setup
        interfaces = get_interfaces()
        for interface in interfaces:
            self.add_interface(interface)

        # Handlers
        self.get_button_send().clicked.connect(self.handler_button_send)
        self.get_button_view().clicked.connect(self.handler_button_view)
        for protocol_button in self.get_protocol_buttons():
            protocol_button.clicked.connect(self.handler_change_protocol)

    # ------------- #
    #    HANDLERS   #
    # ------------- #

    def handler_button_send(self):
        if self.is_sending:
            return
        if not self.validate():
            return

        self.is_sending = False
        self.response = None
        self.clear_errors()
        self.set_waiting()

        protocol = self.get_protocol()
        interface = self.get_interface()
        source_ip = self.get_source_address()
        destiantion_ip = self.get_destination_address()
        source_port = self.get_source_port()
        destination_port = self.get_destination_port()
        icmp_type = None
        icmp_code = None
        payload = self.get_payload()

        worker = CustomPacketsWorker(
            protocol=protocol,
            interface=interface,
            source_ip=source_ip,
            dest_ip=destiantion_ip,
            source_port=source_port,
            dest_port=destination_port,
            icmp_type=icmp_type,
            icmp_code=icmp_code,
            payload=payload
        )
        worker.signals.packet.connect(self.handler_signal_packet)
        self.thread_pool.start(worker)

    def handler_button_view(self):
        if self.is_sending:
            return
        if self.response is None:
            return
        self.set_message_box(self.response)

    def handler_change_protocol(self):
        protocol = self.get_protocol()
        self.update_protocol(protocol)

    def handler_signal_packet(self, packet):
        self.is_sending = False
        self.response = packet
        if packet is None:
            self.set_no_response()
        else:
            self.set_received_response()

    # --------------- #
    #    VALIDATORS   #
    # --------------- #

    def validate(self) -> bool:
        v1 = self.validate_source()
        v2 = self.validate_destination()
        return v1 and v2

    def validate_source(self) -> bool:
        address = self.get_source_address()
        try:
            IPv4Address(address)
            self.clear_source_error()
            return True
        except Exception as e:
            error = str(e)
            self.set_source_error(error)
            return False

    def validate_destination(self) -> bool:
        address = self.get_destination_address()
        try:
            IPv4Address(address)
            self.clear_destination_error()
            return True
        except Exception as e:
            error = str(e)
            self.set_destination_error(error)
            return False

        # # Send ICMP packets
        # def send_packets(self):

        #     # Worker(s)
        #     create_packets_worker = CreatePacketsWorker()

        #     # Inputs that always need to be valid
        #     source = self.input_source_address.text()
        #     dest = self.input_destination_address.text()
        #     inter = self.comboBox.currentText()
        #     cnt = int(self.input_count.text())

        #     # ICMP
        #     if self.radioButton_icmp.isChecked():
        #         try:
        #             # Inputs
        #             message = self.input_icmp_message.toPlainText()
        #             # Command
        #             if cnt is None:
        #                 cnt = 1
        #             if message is None:
        #                 message = "Hello world"
        #             create_packets_worker.SendICMP_worker(source, dest, inter, cnt, message)

        #         except ValueError:
        #             print("ICMP Value error")

        #     # TCP
        #     if self.radioButton_tcp.isChecked():
        #         try:
        #             # Inputs
        #             sport = int(self.input_port_source.text())
        #             dstport = int(self.input_port_destination.text())
        #             # Command
        #             create_packets_worker.SendTCP_worker(source, dest, dstport, sport, inter, cnt)
        #         except ValueError:
        #             print("TCP Value error")

        #     # TCP
        #     if self.radioButton_udp.isChecked():
        #         try:
        #             # Inputs
        #             sport = int(self.input_port_source.text())
        #             dstport = int(self.input_port_destination.text())
        #             # Command
        #             create_packets_worker.SendUDP_worker(source, dest, dstport, sport, inter, cnt)
        #         except ValueError:
        #             print("UDP Value error")

        # # Set standards for some protocols
        # # Ex. ICMP does not use ports etc.
        # def check_protocol(self):
        #     # ICMP check
        #     if self.radioButton_icmp.isChecked():
        #         self.input_port_source.setDisabled(True)
        #         self.input_port_destination.setDisabled(True)
        #         self.input_icmp_message.setEnabled(True)

        #     # TCP check
        #     if self.radioButton_tcp.isChecked() or self.radioButton_udp.isChecked():
        #         self.input_port_source.setEnabled(True)
        #         self.input_port_destination.setEnabled(True)
        #         self.input_icmp_message.setDisabled(True)
