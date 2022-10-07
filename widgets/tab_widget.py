from PyQt5.QtWidgets import QWidget


class TabWidget(QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setContentsMargins(10, 10, 10, 10)
