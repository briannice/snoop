from PyQt5.QtWidgets import (
    QWidget, QLabel, QHBoxLayout, QLineEdit, QPushButton, QVBoxLayout
)


class PortScanningTab(QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.NetworkLabel = QLabel("Network")

        self.Layout = QVBoxLayout()
        self.Header = QHBoxLayout()
        self.Content = QVBoxLayout()

        self.Layout.addLayout(self.Header)
        self.Layout.addLayout(self.Content)
        self.setLayout(self.Layout)
