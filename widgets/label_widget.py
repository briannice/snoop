from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QLabel

from utils import SnoopException


class LabelWidget(QLabel):

    def __init__(self, text, type="label", *args, **kwargs):
        super().__init__(text, *args, **kwargs)

        self.font = QFont()
        self.setType(type)
        self.setFont(self.font)

    def setType(self, type):
        match type:
            case "label":
                self.font.setPointSize(9)
                self.setStyleSheet("color: Black; font-weight: 500;")
            case "error":
                self.setStyleSheet("color: Red;")
            case "info":
                self.setStyleSheet("color: Blue;")
            case "success":
                self.setStyleSheet("color: Green;")
            case "section":
                self.font.setPointSize(12)
                self.setStyleSheet("font-weight: bold; color: Black;")
            case "title":
                self.font.setPointSize(18)
                self.setStyleSheet("")
            case "help":
                self.font.setPointSize(9)
                self.setStyleSheet("color: DimGrey;")
                self.setWordWrap(True)
                self.setFixedWidth(300)
            case _:
                raise SnoopException("Invalid label type!")
