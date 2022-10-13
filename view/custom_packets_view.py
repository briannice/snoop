from ui import CustomPacketsUI
from lib.sniffing import getInterfaces
from lib.custom_packets import SendUDP, SendTCP, SendICMP


class CustomPacketsView(CustomPacketsUI):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Fill interfaces
        self.fill_interfaces(getInterfaces())

        # Event handler for pushbutton
        self.pushButton_send_packets.clicked.connect(self.send_packets)

        # Event handler for radiobutton
        self.radioButton_udp.clicked.connect(self.check_protocol)
        self.radioButton_tcp.clicked.connect(self.check_protocol)
        self.radioButton_icmp.clicked.connect(self.check_protocol)

        # Set checks
        self.check_protocol()

    # Fill interfaces in UI combobox
    def fill_interfaces(self, interfaces):
        self.comboBox.clear()
        self.comboBox.addItems(interfaces)

    def send_packets(self):
        self.send_icmp()

    # Send ICMP packets
    def send_icmp(self):
        try:
            source = self.input_source_address.text()
            dest = self.input_destination_address.text()
            inter = self.comboBox.currentText()
            message = self.input_icmp_message.toPlainText()

            SendICMP(source=source, destination=dest, interface=inter, message=message)
        except():
            print("Error")

    # Set standards for some protocols
    # Ex. ICMP does not use ports etc.
    def check_protocol(self):
        # ICMP check
        if self.radioButton_icmp.isChecked():
            self.input_port_source.setDisabled(True)
            self.input_port_destination.setDisabled(True)
            self.input_icmp_message.setEnabled(True)

        # TCP check
        if self.radioButton_tcp.isChecked() or self.radioButton_udp.isChecked():
            self.input_port_source.setEnabled(True)
            self.input_port_destination.setEnabled(True)
            self.input_icmp_message.setDisabled(True)
