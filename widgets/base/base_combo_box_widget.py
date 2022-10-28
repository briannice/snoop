from PyQt5.QtWidgets import QComboBox


class BaseComboBoxWidget(QComboBox):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
