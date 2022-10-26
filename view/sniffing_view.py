from lib.sniffing import get_interfaces
from PyQt5.QtCore import QThreadPool
from workers import SniffingWorker
from ui import SniffingUI


class SniffingView(SniffingUI):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Thread pool
        self.thread_pool = QThreadPool.globalInstance()
        self.signals = None

        # Data
        self.count = 0
        self.buffer = []
        self.packets = []
        self.max_buffer = 5
        self.is_sniffing = False

        # Setup
        interfaces = get_interfaces()
        for interface in interfaces:
            self.add_interface(interface)

        # Handlers
        self.get_button_sniff().clicked.connect(self.handler_button_sniff)
        self.get_button_stop().clicked.connect(self.handler_button_stop)
        self.get_button_clear().clicked.connect(self.handler_button_clear)
        self.get_output().clicked.connect(self.handler_message_box)

        for protocol_button in self.get_protocol_buttons():
            protocol_button.clicked.connect(self.handler_change_protocol)

    # ------------- #
    #    HANDLERS   #
    # ------------- #

    def handler_button_sniff(self):
        if self.is_sniffing:
            return
        self.is_sniffing = True
        self.count = 0
        self.packets = []

        self.clear_output()
        self.set_count(0)

        interface = self.get_interface()
        protocol = self.get_protocol()

        worker = SniffingWorker(interface, protocol)
        worker.signals.packet.connect(self.handler_signals_packet)
        self.thread_pool.start(worker)
        self.signals = worker.signals

    def handler_button_stop(self):
        if not self.is_sniffing:
            return
        self.is_sniffing = False
        self.signals.stop.emit(True)

    def handler_button_clear(self):
        self.set_count(0)
        self.clear_output()
        self.packets = []

    def handler_signals_packet(self, packet):
        self.count += 1
        if len(self.buffer) < self.max_buffer:
            self.buffer.append(packet)
        else:
            for packet in self.buffer:
                self.add_packet(packet)
                self.packets.append(packet)
            self.buffer = []
        self.set_count(self.count)

    def handler_message_box(self, item):
        row = item.row()
        packet = self.packets[row]
        self.set_message_box(packet)

    def handler_change_protocol(self):
        pass
