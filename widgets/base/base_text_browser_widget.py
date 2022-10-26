from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QTextBrowser

from utils import get_ui_spacing


class BaseTextBrowserWidget(QTextBrowser):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        margin = get_ui_spacing("lg")
        self.setContentsMargins(margin, margin, margin, margin)
        self.font = QFont("monospace")
        self.font.setPointSize(10)
        self.setFont(self.font)
