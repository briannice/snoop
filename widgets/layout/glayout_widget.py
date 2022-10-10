from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QGridLayout


class GLayoutWidget(QGridLayout):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setSpacing(25)
        self.setAlignment(Qt.AlignTop)
