from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QGridLayout

from utils.spacing import get_ui_spacing


class GLayoutWidget(QGridLayout):

    def __init__(self, h_spacing="lg", v_spacing="lg", *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setHorizontalSpacing(get_ui_spacing(h_spacing))
        self.setVerticalSpacing(get_ui_spacing(v_spacing))
        self.setContentsMargins(0, 0, 0, 0)
        self.setAlignment(Qt.AlignTop)
