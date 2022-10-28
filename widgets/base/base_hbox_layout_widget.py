from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QHBoxLayout

from utils import get_ui_spacing


class BaseHBoxLayoutWidget(QHBoxLayout):

    def __init__(self, spacing: str = "sm", *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setAlignment(Qt.AlignTop)
        self.setContentsMargins(0, 0, 0, 0)
        self.setSpacing(get_ui_spacing(spacing))
