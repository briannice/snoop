from PyQt5.QtWidgets import QGroupBox

from .label_widget import LabelWidget
from .layout.vlayout_widget import VLayoutWidget


class GroupWidget(QGroupBox):

    def __init__(self, title, content, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setContentsMargins(50, 30, 50, 25)

        self.Title = LabelWidget(title, type="section")
        self.Content = content

        self.Layout = VLayoutWidget(spacing="lg")
        self.Layout.addWidget(self.Title)
        self.Layout.addLayout(self.Content)

        self.setLayout(self.Layout)

    def getContent(self):
        return self.Content
