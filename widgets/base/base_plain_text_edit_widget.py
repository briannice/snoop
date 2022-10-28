from PyQt5.QtWidgets import QPlainTextEdit


class BasePlaneTextEditWidget(QPlainTextEdit):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setContentsMargins(0, 0, 0, 0)
