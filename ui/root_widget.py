from PyQt5.QtWidgets import QTabWidget

from ui.tabs.footprinting_tab import FootprintingTab
from ui.tabs.home_tab import HomeTab
from ui.tabs.network_scanning_tab import NetworkScanningTab
from ui.tabs.nslookup_tab import NslookupTab
from ui.tabs.port_scanning_tab import PortScanningTab

from ui.tabs import FootprintingTab, HomeTab, SniffingTab, NslookupTab


class RootWidget(QTabWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setMinimumWidth(800)
        #self.setFixedSize(1000, 800)
        self.setMinimumSize(1000, 800)

        self.HomeTab = HomeTab()
        self.FootprintingTab = FootprintingTab()
        self.ScanningTab = NetworkScanningTab()
        self.PortScanningTab = PortScanningTab()
        self.ScanningTab = SniffingTab()
        self.NslookupTab = NslookupTab()

        self.addTab(self.HomeTab, 'Home')
        self.addTab(self.FootprintingTab, 'Footprinting')
        self.addTab(self.ScanningTab, 'Network scanning')
        self.addTab(self.PortScanningTab, 'Port scanning')
        self.addTab(self.ScanningTab, 'Sniffing')
        self.addTab(self.NslookupTab, 'Nslookup')
