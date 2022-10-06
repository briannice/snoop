from PyQt5.QtCore import QThreadPool
from PyQt5.QtWidgets import QWidget, QLabel, QGridLayout, QListView, QListWidgetItem, QListWidget
from PyQt5 import QtCore, QtGui, QtWidgets
from lib.sniffing import getInterfaces
from workers.sniffing_worker import SniffingWorker

itemBuffer = []
maxItemsBeforeFlush = 2


class SniffingTab(QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setObjectName("Form")
        self.resize(1000, 800)
        self.setMinimumSize(QtCore.QSize(1000, 800))
        self.label_choose_interface = QtWidgets.QLabel(self)
        self.label_choose_interface.setGeometry(QtCore.QRect(50, 80, 141, 16))
        self.label_choose_interface.setObjectName("label_choose_interface")
        self.comboBox_interfaces = QtWidgets.QComboBox(self)
        self.comboBox_interfaces.setGeometry(QtCore.QRect(50, 100, 901, 22))
        self.comboBox_interfaces.setObjectName("comboBox_interfaces")
        self.label_choose_protocol = QtWidgets.QLabel(self)
        self.label_choose_protocol.setGeometry(QtCore.QRect(50, 140, 181, 16))
        self.label_choose_protocol.setObjectName("label_choose_protocol")
        self.radioButton_TCP = QtWidgets.QRadioButton(self)
        self.radioButton_TCP.setGeometry(QtCore.QRect(50, 170, 51, 20))
        self.radioButton_TCP.setObjectName("radioButton_TCP")
        self.radioButton_UDP = QtWidgets.QRadioButton(self)
        self.radioButton_UDP.setGeometry(QtCore.QRect(110, 170, 51, 20))
        self.radioButton_UDP.setObjectName("radioButton_UDP")
        self.radioButton_both = QtWidgets.QRadioButton(self)
        self.radioButton_both.setGeometry(QtCore.QRect(170, 170, 51, 20))
        self.radioButton_both.setObjectName("radioButton_both")
        self.radioButton_both.setChecked(True)

        self.listWidget = QtWidgets.QListWidget(self)
        self.listWidget.setGeometry(QtCore.QRect(50, 230, 901, 481))
        self.listWidget.setObjectName("listWidget")

        self.label_output = QtWidgets.QLabel(self)
        self.label_output.setGeometry(QtCore.QRect(50, 210, 181, 16))
        self.label_output.setObjectName("label_output")
        self.label_title = QtWidgets.QLabel(self)
        self.label_title.setGeometry(QtCore.QRect(50, 40, 411, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_title.setFont(font)
        self.label_title.setObjectName("label_title")
        self.pushButton_start_sniffing = QtWidgets.QPushButton(self)
        self.pushButton_start_sniffing.setGeometry(QtCore.QRect(50, 720, 281, 31))
        self.pushButton_start_sniffing.setObjectName("pushButton_start_sniffing")
        self.pushButton_stop_sniffing = QtWidgets.QPushButton(self)
        self.pushButton_stop_sniffing.setGeometry(QtCore.QRect(350, 720, 281, 31))
        self.pushButton_stop_sniffing.setObjectName("pushButton_stop_sniffing")
        self.pushButton_clear_screen = QtWidgets.QPushButton(self)
        self.pushButton_clear_screen.setGeometry(QtCore.QRect(800, 720, 151, 31))
        self.pushButton_clear_screen.setObjectName("pushButton_clear_screen")
        self.label_status = QtWidgets.QLabel(self)
        self.label_status.setGeometry(QtCore.QRect(175, 210, 141, 16))
        self.label_status.setObjectName("label_status")

        # Retranslate objects
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Form"))
        self.label_choose_interface.setText(_translate("Form", "Choose your Interface:"))
        self.label_choose_protocol.setText(_translate("Form", "Choose your protocol settings:"))
        self.radioButton_TCP.setText(_translate("Form", "TCP"))
        self.radioButton_UDP.setText(_translate("Form", "UDP"))
        self.radioButton_both.setText(_translate("Form", "Both"))
        self.label_output.setText(_translate("Form", "Output packets:"))
        self.label_title.setText(_translate("Form", "Network sniffer: sniff packets on your local NIC"))
        self.pushButton_start_sniffing.setText(_translate("Form", "Start sniffing"))
        self.pushButton_stop_sniffing.setText(_translate("Form", "Stop Sniffing"))
        self.pushButton_clear_screen.setText(_translate("Form", "Clear screen"))
        self.label_status.setText(_translate("Form", "Status: stopped"))

        self.label_status.setObjectName("label_status")
        self.label_status.setStyleSheet('QLabel#label_status {color: red}')

        # Post initialization
        self.Label = QLabel("Scanning")
        self.Layout = QGridLayout()
        self.setLayout(self.Layout)

        # Default both
        self.sniffing_worker = SniffingWorker(self.comboBox_interfaces.currentText(), protocol=0)
        self.pushButton_stop_sniffing.setDisabled(True)
        self.both_button_event()
        self.udp_button_event()
        self.tcp_button_event()

        self.fill_interfaces(getInterfaces())
        self.start_sniffing_all_packets()
        self.stop_sniffing_all_packets()
        self.clear_screen_event()

    # Fill interfaces in UI combobox
    def fill_interfaces(self, interfaces):
        self.comboBox_interfaces.clear()
        self.comboBox_interfaces.addItems(interfaces)

    # For every packet that comes by
    def handle_packet(self, packet):
        # Creating item chunks before adding item to widget
        if len(itemBuffer) < maxItemsBeforeFlush:
            itemBuffer.append(packet)
        else:
            # If buffer is full:
            self.listWidget.addItems(itemBuffer)
            self.listWidget.scrollToBottom()
            itemBuffer.clear()

    # Creating worker to do packet handling
    # Wrapper function for start button
    def worker_start(self):
        # Call function "handlePacket" when clicking on start button
        self.sniffing_worker.signals.result.connect(self.handle_packet)
        # Add worker to threadpool
        QThreadPool.globalInstance().start(self.sniffing_worker)
        # User experience
        self.pushButton_start_sniffing.setDisabled(True)
        self.pushButton_stop_sniffing.setDisabled(False)
        self.label_status.setText("Status: sniffing")
        self.label_status.setStyleSheet('QLabel#label_status {color: blue}')

    # Start button function
    # Triggers wrapper function above
    def start_sniffing_all_packets(self):
        self.pushButton_start_sniffing.clicked.connect(self.worker_start)

    def worker_stop(self):
        self.sniffing_worker.stopPacket()
        # User experience
        self.pushButton_start_sniffing.setDisabled(False)
        self.pushButton_stop_sniffing.setDisabled(True)
        self.label_status.setText("Status: stopped")
        self.label_status.setStyleSheet('QLabel#label_status {color: red}')

    # Stop button function
    def stop_sniffing_all_packets(self):
        self.pushButton_stop_sniffing.clicked.connect(self.worker_stop)

    # Clear list
    def clear_screen(self):
        self.listWidget.clear()

    def clear_screen_event(self):
        self.pushButton_clear_screen.clicked.connect(self.clear_screen)

    # FILTERING ###############################
    def change_worker_to_protocol(self):
        if self.radioButton_both.isChecked():
            self.worker_stop()
            self.sniffing_worker = SniffingWorker(self.comboBox_interfaces.currentText(), protocol=0)
            print("Both")
        if self.radioButton_TCP.isChecked():
            self.worker_stop()
            self.sniffing_worker = SniffingWorker(self.comboBox_interfaces.currentText(), protocol=1)
            print("TCP")
        if self.radioButton_UDP.isChecked():
            self.worker_stop()
            self.sniffing_worker = SniffingWorker(self.comboBox_interfaces.currentText(), protocol=2)
            print("UDP")

    # Event handlers for protocol radiobutton(s)
    def both_button_event(self): self.radioButton_both.clicked.connect(self.change_worker_to_protocol)
    def tcp_button_event(self): self.radioButton_TCP.clicked.connect(self.change_worker_to_protocol)
    def udp_button_event(self): self.radioButton_UDP.clicked.connect(self.change_worker_to_protocol)
