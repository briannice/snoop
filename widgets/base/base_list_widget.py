from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QListWidget


class BaseListWidget(QListWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setContentsMargins(0, 0, 0, 0)

        self.font = QFont("monospace")
        self.font.setPointSize(10)
        self.setSpacing(10)
        self.setFont(self.font)
