from PyQt5.QtWidgets import QListWidget


class ListWidget(QListWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
