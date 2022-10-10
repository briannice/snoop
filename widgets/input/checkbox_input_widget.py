from PyQt5.QtWidgets import QCheckBox


class CheckboxInputWidget(QCheckBox):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
