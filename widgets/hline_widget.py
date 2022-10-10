from PyQt5.QtGui import QColor, QPalette
from PyQt5.QtWidgets import QFrame


class HLineWidget(QFrame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setFrameShape(QFrame.HLine)
        pal = self.palette()
        pal.setColor(QPalette.WindowText, QColor(200, 200, 200))
        self.setPalette(pal)
