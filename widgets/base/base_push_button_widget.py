from PyQt5.QtWidgets import QPushButton


class BasePushButtonWidget(QPushButton):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setContentsMargins(0, 0, 0, 0)
