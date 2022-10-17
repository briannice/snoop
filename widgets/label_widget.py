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
                self.setStyleSheet("color: black;")
            case "error":
                self.setStyleSheet("color: red;")
            case "section":
                self.font.setPointSize(12)
                self.setStyleSheet("font-weight: bold; color: #2F2F2F;")
            case "title":
                self.font.setPointSize(15)
                self.setStyleSheet("")
            case _:
                raise SnoopException("Invalid label type!")

        self.setFont(self.font)
