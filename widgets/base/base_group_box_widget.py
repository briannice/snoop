from PyQt5.QtWidgets import QGroupBox

from utils import get_ui_spacing


class BaseGroupBoxWidget(QGroupBox):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        margin = get_ui_spacing("lg")
        self.setContentsMargins(margin, margin, margin, margin)
