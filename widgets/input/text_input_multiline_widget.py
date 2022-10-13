from PyQt5.QtWidgets import QPlainTextEdit


class TextInputMultilineWidget(QPlainTextEdit):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
