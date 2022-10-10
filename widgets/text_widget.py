from PyQt5.QtWidgets import QTextBrowser


class TextWidget(QTextBrowser):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
