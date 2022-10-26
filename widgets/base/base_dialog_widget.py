from PyQt5.QtWidgets import QDialog

from utils import get_ui_spacing


class BaseDialogWidget(QDialog):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        margin = get_ui_spacing("lg")
        self.setContentsMargins(margin, margin, margin, margin)
        self.setMinimumSize(500, 500)
