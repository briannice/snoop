from PyQt5.QtWidgets import QMessageBox


class BaseMessageBoxWidget(QMessageBox):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
