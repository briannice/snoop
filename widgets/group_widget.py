from PyQt5.QtWidgets import QGroupBox


class GroupWidget(QGroupBox):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setContentsMargins(15, 15, 15, 15)
