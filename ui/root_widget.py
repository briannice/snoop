from PyQt5.QtWidgets import QTabWidget


from ui.tabs import FootprintingTab, HomeTab, ScanningTab


class RootWidget(QTabWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setFixedSize(1000, 800)

        self.HomeTab = HomeTab()
        self.FootprintingTab = FootprintingTab()
        self.ScanningTab = ScanningTab()

        self.addTab(self.HomeTab, 'Home')
        self.addTab(self.FootprintingTab, 'Footprinting')
        self.addTab(self.ScanningTab, 'Scanning')
