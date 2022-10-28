from typing import List
from widgets.base import BaseDialogWidget, BaseLabelWidget, BaseTextBrowserWidget, BaseVBoxLayoutWidget


class CustomContentDialogWidget(BaseDialogWidget):

    def __init__(self, title: str, content: str):
        super().__init__()

        # Widgets
        self.col = BaseVBoxLayoutWidget()
        self.title = BaseLabelWidget(type="title", text=title)
        self.content = BaseTextBrowserWidget()

        # Layout
        self.col.addWidget(self.title)
        self.col.addWidget(self.content)
        self.setLayout(self.col)

        # Styling
        self.setMinimumSize(800, 600)
        self.content.setText(content)
        self.setWindowTitle(title)
