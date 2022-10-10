from PyQt5.QtWidgets import QSizePolicy


class SizePolicyWidget(QSizePolicy):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
