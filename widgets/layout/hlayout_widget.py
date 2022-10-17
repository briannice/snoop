from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QHBoxLayout

from utils import get_ui_spacing


class HLayoutWidget(QHBoxLayout):

    def __init__(self, spacing="lg", *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setSpacing(get_ui_spacing(spacing))
        self.setContentsMargins(0, 0, 0, 0)
        self.setAlignment(Qt.AlignTop)
