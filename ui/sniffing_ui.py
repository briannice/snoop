from widgets import ButtonWidget, LabelWidget, TabWidget, RadioButtonWidget, ListWidget, QRect, QSize
from widgets.input import ComboBoxWidget
from widgets.layout import GLayoutWidget
from widgets.GUI import Font


class SniffingUI(TabWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Data
        self.count_packets = 0
        self.itemBuffer = []
        self.maxItems = 5

        # Init widget
        self.setObjectName("Form")
        self.resize(1000, 800)
        self.setMinimumSize(QSize(1000, 800))

        # Widgets
        self.label_choose_interface = LabelWidget(self)
        self.label_choose_interface.setGeometry(QRect(50, 80, 141, 16))
        self.label_choose_interface.setText("Choose your interface:")

        self.comboBox_interfaces = ComboBoxWidget(self)
        self.comboBox_interfaces.setGeometry(QRect(50, 100, 901, 22))

        self.label_choose_protocol = LabelWidget(self)
        self.label_choose_protocol.setGeometry(QRect(50, 140, 181, 16))
        self.label_choose_protocol.setText("Choose your desired protocol:")

        self.radioButton_TCP = RadioButtonWidget(self)
        self.radioButton_TCP.setGeometry(QRect(50, 170, 51, 20))
        self.radioButton_TCP.setText("TCP")

        self.radioButton_UDP = RadioButtonWidget(self)
        self.radioButton_UDP.setGeometry(QRect(110, 170, 51, 20))
        self.radioButton_UDP.setText("UDP")

        self.radioButton_ICMP = RadioButtonWidget(self)
        self.radioButton_ICMP.setGeometry(QRect(170, 170, 58, 20))
        self.radioButton_ICMP.setText("ICMP")

        self.radioButton_both = RadioButtonWidget(self)
        self.radioButton_both.setGeometry(QRect(235, 170, 51, 20))
        self.radioButton_both.setText("Both")
        self.radioButton_both.setChecked(True)

        self.listWidget = ListWidget(self)
        self.listWidget.setGeometry(QRect(50, 230, 901, 481))
        self.label_title = LabelWidget(self)
        self.label_title.setGeometry(QRect(50, 40, 411, 16))

        font = Font()
        font.setPointSize(11)
        self.label_title.setFont(font)
        self.label_title.setText("Network sniffer: sniff packets")

        self.pushButton_start_sniffing = ButtonWidget(self)
        self.pushButton_start_sniffing.setGeometry(QRect(50, 720, 281, 31))
        self.pushButton_start_sniffing.setText("Start sniffing")
        self.pushButton_stop_sniffing = ButtonWidget(self)
        self.pushButton_stop_sniffing.setGeometry(QRect(350, 720, 281, 31))
        self.pushButton_stop_sniffing.setText("Stop sniffing")
        self.pushButton_clear_screen = ButtonWidget(self)
        self.pushButton_clear_screen.setGeometry(QRect(800, 720, 151, 31))
        self.pushButton_clear_screen.setText("Clean output")

        self.label_status = LabelWidget(self)
        self.label_status.setGeometry(QRect(50, 210, 181, 16))
        self.label_status.setText("Status: stopped")
        self.label_status.setStyleSheet('QLabel#label_status {color: red}')
        self.label_count = LabelWidget(self)
        self.label_count.setGeometry(QRect(150, 210, 141, 16))

        # Setup
        self.Label = LabelWidget("Scanning")
        self.Layout = GLayoutWidget()
        self.setLayout(self.Layout)
