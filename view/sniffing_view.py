from lib.sniffing import getInterfaces
from PyQt5.QtCore import QThreadPool
from workers import SniffingWorker
from ui import SniffingUI


class SniffingView(SniffingUI):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Worker(s)
        self.sniffing_worker = SniffingWorker(self.comboBox_interfaces.currentText(), protocol=0)

        # Thread pool
        self.thread_pool = QThreadPool()

        # Handlers
        self.pushButton_start_sniffing.clicked.connect(self.worker_start)
        self.pushButton_stop_sniffing.clicked.connect(self.worker_stop)
        self.pushButton_clear_screen.clicked.connect(self.clear_screen)
        self.radioButton_both.clicked.connect(self.change_worker_to_protocol)
        self.radioButton_TCP.clicked.connect(self.change_worker_to_protocol)
        self.radioButton_UDP.clicked.connect(self.change_worker_to_protocol)
        self.radioButton_ICMP.clicked.connect(self.change_worker_to_protocol)
        self.fill_interfaces(getInterfaces())

    # Fill interfaces in UI combobox
    def fill_interfaces(self, interfaces):
        self.comboBox_interfaces.clear()
        self.comboBox_interfaces.addItems(interfaces)

    # For every packet that comes by
    def handle_packet(self, packet):
        self.count_packets += 1
        # Creating item chunks before adding item to widget
        if len(self.itemBuffer) < self.maxItems:
            self.itemBuffer.append(packet)
        else:
            # If buffer is full:
            self.listWidget.addItems(self.itemBuffer)
            self.listWidget.scrollToBottom()
            self.itemBuffer.clear()
        self.label_count.setText("Total packets: " + str(self.count_packets))

    def handle_packet_icmp(self, packet):
        self.listWidget.addItem(packet)
        self.listWidget.scrollToBottom()
        self.label_count.setText("Total packets: " + str(self.count_packets))

    # Creating worker to do packet handling
    # Wrapper function for start button
    def worker_start(self):
        # Checks for ICMP
        if self.radioButton_ICMP.isChecked():
            self.sniffing_worker.signals.result.connect(self.handle_packet_icmp)
        else:
            self.sniffing_worker.signals.result.connect(self.handle_packet)

        # Add worker to threadpool
        QThreadPool.globalInstance().start(self.sniffing_worker)
        # User experience
        self.pushButton_start_sniffing.setDisabled(True)
        self.pushButton_stop_sniffing.setDisabled(False)
        self.label_status.setText("Status: sniffing")
        self.label_status.setStyleSheet('QLabel#label_status {color: blue}')

    def worker_stop(self):
        self.sniffing_worker.stopPacket()
        # User experience
        self.pushButton_start_sniffing.setDisabled(False)
        self.pushButton_stop_sniffing.setDisabled(True)
        self.label_status.setText("Status: stopped")
        self.label_status.setStyleSheet('QLabel#label_status {color: red}')

    # Clear list
    def clear_screen(self):
        self.listWidget.clear()
        self.label_count.setText("Total packets: 0")
        self.count_packets = 0

    # FILTERING
    def change_worker_to_protocol(self):
        protocol = 0
        if self.radioButton_both.isChecked():
            protocol = 0
        if self.radioButton_TCP.isChecked():
            protocol = 1
        if self.radioButton_UDP.isChecked():
            protocol = 2
        if self.radioButton_ICMP.isChecked():
            protocol = 3
        self.worker_stop()
        self.sniffing_worker = SniffingWorker(self.comboBox_interfaces.currentText(), protocol=protocol)
