from PySide6.QtWidgets import QPushButton


class HeaderButton(QPushButton):

    def __init__(self, text, *args, **kwargs):
        super().__init__(text, *args, **kwargs)
