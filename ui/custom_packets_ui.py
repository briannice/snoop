from widgets import ButtonWidget, LabelWidget, TabWidget, RadioButtonWidget, QRect
from widgets.input import ComboBoxWidget, TextInputWidget, TextInputMultilineWidget
from widgets.GUI import Font


class CustomPacketsUI(TabWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Title
        self.label_title = LabelWidget(self)
        self.label_title.setGeometry(QRect(40, 40, 381, 21))
        font = Font()
        font.setPointSize(12)
        self.label_title.setFont(font)

        # Combobox
        self.comboBox = ComboBoxWidget(self)
        self.comboBox.setGeometry(QRect(40, 120, 921, 22))
        self.label_choose_interface = LabelWidget(self)
        self.label_choose_interface.setGeometry(QRect(40, 90, 161, 21))

        # Radiobutton
        self.label_choose_protocol = LabelWidget(self)
        self.label_choose_protocol.setGeometry(QRect(40, 180, 181, 21))

        self.radioButton_icmp = RadioButtonWidget(self)
        self.radioButton_icmp.setGeometry(QRect(40, 210, 61, 20))
        self.radioButton_icmp.setObjectName("radioButton_icmp")

        self.radioButton_tcp = RadioButtonWidget(self)
        self.radioButton_tcp.setGeometry(QRect(120, 210, 51, 20))
        self.radioButton_tcp.setObjectName("radioButton_tcp")

        self.radioButton_udp = RadioButtonWidget(self)
        self.radioButton_udp.setGeometry(QRect(190, 210, 51, 20))
        self.radioButton_udp.setObjectName("radioButton_udp")

        # Adresses and ports
        self.label_source_address = LabelWidget(self)
        self.label_source_address.setGeometry(QRect(40, 270, 121, 21))
        self.label_choose_destination_address = LabelWidget(self)
        self.label_choose_destination_address.setGeometry(QRect(40, 300, 121, 21))

        self.input_source_address = TextInputWidget(self)
        self.input_source_address.setGeometry(QRect(170, 270, 211, 22))

        self.input_destination_address = TextInputWidget(self)
        self.input_destination_address.setGeometry(QRect(170, 300, 211, 22))

        # Ports
        self.input_port_source = TextInputWidget(self)
        self.input_port_source.setGeometry(QRect(430, 270, 51, 22))

        self.input_port_destination = TextInputWidget(self)
        self.input_port_destination.setGeometry(QRect(430, 300, 51, 22))

        self.label_port_source = LabelWidget(self)
        self.label_port_source.setGeometry(QRect(400, 270, 31, 21))

        self.label_port_destination = LabelWidget(self)
        self.label_port_destination.setGeometry(QRect(400, 300, 31, 21))

        # Custom ICMP message
        self.label_custom_message = LabelWidget(self)
        self.label_custom_message.setGeometry(QRect(40, 350, 171, 21))
        self.input_icmp_message = TextInputMultilineWidget(self)
        self.input_icmp_message.setGeometry(QRect(40, 380, 921, 151))

        # ICMP Note
        self.label_icmp_note = LabelWidget(self)
        self.label_icmp_note.setGeometry(QRect(520, 260, 431, 41))
        self.label_icmp_note.setWordWrap(True)

        # Count
        self.label_count = LabelWidget(self)
        self.label_count.setGeometry(QRect(40, 560, 161, 21))
        self.input_count = TextInputWidget(self)
        self.input_count.setGeometry(QRect(210, 560, 71, 22))

        self.pushButton_send_packets = ButtonWidget(self)
        self.pushButton_send_packets.setGeometry(QRect(40, 600, 241, 31))

        # Set text
        self.label_title.setText("Create and send your own custom packets")
        self.label_choose_interface.setText("Choose your interface: ")
        self.radioButton_icmp.setText("ICMP")
        self.label_choose_protocol.setText("Choose your desired protocol: ")
        self.radioButton_tcp.setText("TCP")
        self.radioButton_udp.setText("UDP")
        self.label_source_address.setText("Source address:")
        self.label_choose_destination_address.setText("Destination address:")
        self.label_port_source.setText("Port")
        self.label_port_destination.setText("Port")
        self.label_custom_message.setText("Custom Message (ICMP only)")
        self.label_icmp_note.setText(
            "Important note: ICMP has no concept of ports, as TCP and UDP do, but instead uses types and codes.")
        self.label_count.setText("How much packets to send:")
        self.pushButton_send_packets.setText("Send packets!")
