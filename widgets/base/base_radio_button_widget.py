from PyQt5.QtWidgets import QRadioButton


class BaseRadioButtonWidget(QRadioButton):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setContentsMargins(0, 0, 0, 0)
