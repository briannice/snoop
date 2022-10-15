from ui import CustomPacketsUI
from lib.sniffing import getInterfaces
from workers import CreatePacketsWorker


class CustomPacketsView(CustomPacketsUI):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Fill interfaces
        self.fill_interfaces(getInterfaces())

        # Event handler for pushbutton
        self.pushButton_send_packets.clicked.connect(self.send_packets_handler)

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

    def send_packets_handler(self):
        self.send_packets()

    # Send ICMP packets
    def send_packets(self):

        # Worker(s)
        create_packets_worker = CreatePacketsWorker()

        # Inputs that always need to be valid
        source = self.input_source_address.text()
        dest = self.input_destination_address.text()
        inter = self.comboBox.currentText()
        cnt = int(self.input_count.text())

        # ICMP
        if self.radioButton_icmp.isChecked():
            try:
                # Inputs
                message = self.input_icmp_message.toPlainText()
                # Command
                if cnt is None:
                    cnt = 1
                if message is None:
                    message = "Hello world"
                create_packets_worker.SendICMP_worker(source, dest, inter, cnt, message)

            except ValueError:
                print("ICMP Value error")

        # TCP
        if self.radioButton_tcp.isChecked():
            try:
                # Inputs
                sport = int(self.input_port_source.text())
                dstport = int(self.input_port_destination.text())
                # Command
                create_packets_worker.SendTCP_worker(source, dest, dstport, sport, inter, cnt)
            except ValueError:
                print("TCP Value error")

        # TCP
        if self.radioButton_udp.isChecked():
            try:
                # Inputs
                sport = int(self.input_port_source.text())
                dstport = int(self.input_port_destination.text())
                # Command
                create_packets_worker.SendUDP_worker(source, dest, dstport, sport, inter, cnt)
            except ValueError:
                print("UDP Value error")

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
