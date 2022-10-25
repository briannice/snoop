from PyQt5.QtWidgets import QTabWidget

from view import NetworkScanningView, PortScanningView, SniffingView, HomeView, NslookpView, WhoisView


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

        # Nslookup tab
        nslookup_view = NslookpView()

        # Whois tab
        whois_view = WhoisView()

        # Setup
        self.addTab(home_view, "Home")
        self.addTab(network_scanning_view, "Network scanning")
        self.addTab(port_scanning_view, "Port scanning")
        self.addTab(sniffing_view, "Sniffing")
        self.addTab(nslookup_view, "Nslookup")
        self.addTab(whois_view, "Whois")
