from PyQt5.QtWidgets import QLineEdit


class TextInputWidget(QLineEdit):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
