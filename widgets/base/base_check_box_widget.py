from PyQt5.QtWidgets import QCheckBox


class BaseCheckBoxWidget(QCheckBox):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
