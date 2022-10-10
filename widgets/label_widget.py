from mimetypes import init
from PyQt5.QtWidgets import QLabel


class LabelWidget(QLabel):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
