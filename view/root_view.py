from PyQt5.QtWidgets import QTabWidget

from model import NetworkScanningModel, PortScanningModel
from presenter import NetworkScanningPresenter, PortScanningPresenter
from view import NetworkScanningView, PortScanningView


class RootView(QTabWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Network scanning tab
        network_scanning_model = NetworkScanningModel()
        network_scanning_view = NetworkScanningView()
        _ = NetworkScanningPresenter(network_scanning_view, network_scanning_model)

        # Port scanning tab
        port_scanning_model = PortScanningModel()
        port_scanning_view = PortScanningView()
        _ = PortScanningPresenter(port_scanning_view, port_scanning_model)

        # Setup
        self.addTab(network_scanning_view, "Network scanning")
        self.addTab(port_scanning_view, "Port scanning")
