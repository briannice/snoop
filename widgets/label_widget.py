from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QLabel

from utils import SnoopException


class LabelWidget(QLabel):

    def __init__(self, text, type="label", *args, **kwargs):
        super().__init__(text, *args, **kwargs)

        self.font = QFont()

        match type:
            case "label":
                self.font.setPointSize(9)
                self.setStyleSheet("color: Black; font-weight: 500;")
            case "error":
                self.setStyleSheet("color: Red;")
            case "section":
                self.font.setPointSize(12)
                self.setStyleSheet("font-weight: bold; color: Black;")
            case "title":
                self.font.setPointSize(18)
                self.setStyleSheet("")
            case "info":
                self.font.setPointSize(9)
                self.setStyleSheet("color: DimGrey;")
                self.setWordWrap(True)
                self.setFixedWidth(300)
            case _:
                raise SnoopException("Invalid label type!")

        self.setFont(self.font)
