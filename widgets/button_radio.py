from PyQt5.QtWidgets import QRadioButton


class RadioButtonWidget(QRadioButton):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
