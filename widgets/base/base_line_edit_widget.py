from PyQt5.QtWidgets import QLineEdit


class BaseLineEditWidget(QLineEdit):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
