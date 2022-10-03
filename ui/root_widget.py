from PyQt5.QtWidgets import QTabWidget

from ui.tabs import FootprintingTab, HomeTab, SniffingTab, NslookupTab, PortScanningTab, NetworkScanningTab


class RootWidget(QTabWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


        self.setMinimumWidth(800)

        self.HomeTab = HomeTab()
        self.FootprintingTab = FootprintingTab()
        self.ScanningTab = NetworkScanningTab()
        self.PortScanningTab = PortScanningTab()
        self.NslookupTab = NslookupTab()
        self.SniffingTab = SniffingTab()

        self.addTab(self.HomeTab, 'Home')
        self.addTab(self.FootprintingTab, 'Footprinting')
        self.addTab(self.ScanningTab, 'Network scanning')
        self.addTab(self.PortScanningTab, 'Port scanning')
        self.addTab(self.NslookupTab, 'Nslookup')
        self.addTab(self.SniffingTab, 'Sniffing')
