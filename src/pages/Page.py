from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QColor, QPalette


class Page(QWidget):

    def __init__(self, color,   *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setFixedSize(1000, 800)
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)
