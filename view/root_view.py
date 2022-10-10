from PyQt5.QtWidgets import QTabWidget

from view import NetworkScanningView, PortScanningView


class RootView(QTabWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Network scanning tab
        network_scanning_view = NetworkScanningView()

        # Port scanning tab
        port_scanning_view = PortScanningView()

        # Setup
        self.addTab(network_scanning_view, "Network scanning")
        self.addTab(port_scanning_view, "Port scanning")
