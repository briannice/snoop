from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QListWidget


class ListWidget(QListWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.font = QFont("monospace")
        self.font.setPointSize(10)
        self.setSpacing(10)
        self.setFont(self.font)
