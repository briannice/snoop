from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QGroupBox


class GroupWidget(QGroupBox):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.font = QFont()
        self.font.setPointSize(12)
        self.setFont(self.font)
        self.setContentsMargins(50, 50, 50, 25)
