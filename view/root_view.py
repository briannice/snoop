from PyQt5.QtWidgets import QTabWidget

from view import NetworkScanningView, PortScanningView, SniffingView, HomeView, CustomPacketsView


class RootView(QTabWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Home
        home_view = HomeView()

        # Network scanning tab
        network_scanning_view = NetworkScanningView()

        # Port scanning tab
        port_scanning_view = PortScanningView()

        # Sniffing tab
        sniffing_view = SniffingView()

        # Custom Packets Tab
        custom_packets = CustomPacketsView()

        # Setup
        self.addTab(custom_packets, "Custom packets")
        self.addTab(home_view, "Home")
        self.addTab(network_scanning_view, "Network scanning")
        self.addTab(port_scanning_view, "Port scanning")
        self.addTab(sniffing_view, "Sniffing")
