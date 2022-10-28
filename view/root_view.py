from PyQt5.QtWidgets import QTabWidget

from view import HomeView, NetworkScanningView, NsLookupView, PortScanningView, SniffingView, CustomPacketsView, WhoisView


class RootView(QTabWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Home
        home_view = HomeView()

        # Custom Packets Tab
        custom_packets = CustomPacketsView()

        # Network scanning tab
        network_scanning_view = NetworkScanningView()

        # Nslookup view
        ns_lookup_view = NsLookupView()

        # Port scanning tab
        port_scanning_view = PortScanningView()

        # Sniffing tab
        sniffing_view = SniffingView()

        # Whois tab
        whois_view = WhoisView()

        # Setup
        self.addTab(home_view, "Home")
        self.addTab(custom_packets, "Custom packets")
        self.addTab(network_scanning_view, "Network scanning")
        self.addTab(ns_lookup_view, "NS lookup")
        self.addTab(port_scanning_view, "Port scanning")
        self.addTab(sniffing_view, "Sniff packets")
        self.addTab(whois_view, "Whois lookup")
