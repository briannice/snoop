from PySide6.QtWidgets import QHBoxLayout, QStackedLayout, QVBoxLayout, QWidget

from components.buttons.HeaderButton import HeaderButton
from pages.AnalysePage import AnalysePage
from pages.CreatePage import CreatePage
from pages.SniffPage import SniffPage


class Root(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Widgets
        self.header_button_create = HeaderButton("Create")
        self.header_button_sniff = HeaderButton("Sniff")
        self.header_button_analyse = HeaderButton("Analyse")

        self.router_page_analyse = AnalysePage()
        self.router_page_create = CreatePage()
        self.router_page_sniff = SniffPage()

        # Layouts
        self.root_layout = QVBoxLayout()
        self.header_layout = QHBoxLayout()
        self.router_layout = QStackedLayout()

        self.setLayout(self.root_layout)
        self.root_layout.addLayout(self.header_layout)
        self.root_layout.addLayout(self.router_layout)

        self.header_layout.addWidget(self.header_button_create)
        self.header_layout.addWidget(self.header_button_sniff)
        self.header_layout.addWidget(self.header_button_analyse)

        self.router_layout.addWidget(self.router_page_create)
        self.router_layout.addWidget(self.router_page_sniff)
        self.router_layout.addWidget(self.router_page_analyse)

        # Signals
        self.header_button_create.pressed.connect(
            lambda: self.set_selected_page(0))
        self.header_button_sniff.pressed.connect(
            lambda: self.set_selected_page(1))
        self.header_button_analyse.pressed.connect(
            lambda: self.set_selected_page(2))

        self.router_layout.setCurrentIndex(1)

    def set_selected_page(self, i):
        self.router_layout.setCurrentIndex(i)
