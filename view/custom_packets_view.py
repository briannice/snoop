from ipaddress import IPv4Address
from ui import CustomPacketsUI
from lib.sniffing import get_interfaces
from workers import CustomPacketsWorker
from PyQt5.QtCore import QThreadPool
from utils.validators import port_validator, icmp_code_validator, icmp_type_validator


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
        icmp_type = self.get_icmp_type()
        icmp_code = self.get_icmp_code()
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
        errors = []
        address = self.get_source_address()
        try:
            IPv4Address(address)
        except Exception as e:
            error = str(e)
            errors.append(error)
        if self.is_show_ports():
            port = self.get_source_port()
            error = port_validator(port)
            if error is not None:
                errors.append(error)
        else:
            type = self.get_icmp_type()
            error = icmp_type_validator(type)
            if error is not None:
                errors.append(error)
        if len(errors) == 0:
            self.clear_source_error()
            return True
        else:
            self.set_source_error(errors[0])
            return False

    def validate_destination(self) -> bool:
        errors = []
        address = self.get_destination_address()
        try:
            IPv4Address(address)
        except Exception as e:
            error = str(e)
            errors.append(error)
        if self.is_show_ports():
            port = self.get_destination_port()
            error = port_validator(port)
            if error is not None:
                errors.append(error)
        else:
            type = self.get_icmp_code()
            error = icmp_code_validator(type)
            if error is not None:
                errors.append(error)
        if len(errors) == 0:
            self.clear_destination_error()
            return True
        else:
            self.set_destination_error(errors[0])
            return False
