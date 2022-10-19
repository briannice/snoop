from PyQt5.QtWidgets import QWidget


class TabWidget(QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setFixedSize(1000, 800)
        self.setContentsMargins(25, 25, 25, 25)
