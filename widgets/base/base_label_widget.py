from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QLabel

from utils import SnoopException


class BaseLabelWidget(QLabel):

    def __init__(self, text: str = "", type: str = "label", *args, **kwargs):
        super().__init__(text, *args, **kwargs)

        self.font = QFont()
        self.setType(type)
        self.setFont(self.font)

    def setType(self, type):
        match type:
            case "title":
                self.set_title()
            case "subtitle":
                self.set_subtitle()
            case "label":
                self.set_label()
            case "success":
                self.set_success()
            case "error":
                self.set_error()
            case "info":
                self.set_info()
            case "help":
                self.set_help()
            case _:
                raise SnoopException("Invalid label type!")

    def set_title(self):
        self.font.setPointSize(18)
        self.setStyleSheet("color: Black;")

    def set_subtitle(self):
        self.font.setPointSize(14)
        self.setStyleSheet("color: Black;")

    def set_label(self):
        self.font.setPointSize(11)
        self.setStyleSheet("color: Black;")

    def set_success(self):
        self.font.setPointSize(11)
        self.setStyleSheet("color: Green;")

    def set_error(self):
        self.font.setPointSize(11)
        self.setStyleSheet("color: Red;")

    def set_info(self):
        self.font.setPointSize(11)
        self.setStyleSheet("color: Blue;")

    def set_help(self):
        self.font.setPointSize(9)
        self.setStyleSheet("color: DimGray;")
